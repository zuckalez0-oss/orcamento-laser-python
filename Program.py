import json
# Classe do orçamento --> Composto por uma lista de peças a orçar
class Orcamento:
    def __init__(self):
        self.lista_de_pecas = []
        
    def adicionar_peca(self, peca):
        self.lista_de_pecas.append(peca)

    def exibir_relatorio_final(self):
        print("\n" + "="*40)
        print("    ORÇAMENTO FINAL - CORTE LASER    ")
        print("="*40)
        tempo_total_do_orcamento = 0
        for indice, peca in enumerate(self.lista_de_pecas, start=1):
            print(f"\nPeça {indice}:")
            print(f"  Tipo: {peca.tipo}")
            print(f"  Medida A: {peca.medida_a:.2f} mm")
            print(f"  Medida B: {peca.medida_b:.2f} mm")
            print(f"  Espessura: {peca.esp:.2f} mm")
            print(f"  Quantidade: {peca.qtd}")
            print(f"  Quantidade de pierces: {peca.qtd_furos}")
            print(f"  Quantidade de furos: {peca.qtd_furos}")
            print(f"  Diâmetro dos furos: {peca.diam_furos:.2f} mm")
            print(f"  Área total: {peca.area_total:.2f} mm²")
            print(f"  Perímetro total: {peca.perimetro_total:.2f} mm")

            print(f"  Velocidade de usada: {peca.velocidade} mm/min")
            print(f"  Tempo de unitario: {peca.tempo_unitario_real:.2f} minutos")
            print(f"  Tempo total do lote: {peca.tempo_total_lote:.2f} minutos")

            tempo_total_do_orcamento += peca.tempo_total_lote
        print("\n" + "-"*40)
        print(f"⏱️ TEMPO TOTAL DE MÁQUINA: {tempo_total_do_orcamento:.2f} minutos")
        print("-"*40 + "\n")


class PecaLaser:
    def __init__(self, tipo, qtd, esp, medida_a, medida_b, qtd_furos, diam_furos):
        #Variaveis de entrada
        self.tipo = tipo
        self.qtd = qtd
        self.esp = esp
        self.medida_a = medida_a
        self.medida_b = medida_b
        self.qtd_furos = qtd_furos
        self.diam_furos = diam_furos
        #Vaviaveis calculadas 
        self.area_total = 0
        self.perimetro_total = 0
        #Variaveis para tempo e velocidade
        self.velocidade = 0
        self.tempo_total_lote = 0 
        self.tempo_corte_puro = 0 
        self.tempo_pierce = 0 # new
        self.tempo_unitario_real = 0 # tempo corte puro + tempo pierce
        self.qtd_pierces =0
        



# Calculo de geometrias com base no tipo da peca
class CalculadoraOrcamento:
    def tabela_velocidade_por_espessura(self, esp):
        tabela = {
            0.90:22100,
            2.00: 21250,
            3.00: 12750
        }
        return tabela.get(esp, "Espessura não encontrada na tabela")
    def tabela_tempo_pierce_por_espessura(self, esp):
        tabela = {
            0.90:0.6,
            1.20:0.6,
            1.25:0.6,
            1.50:0.6,
            2.00:0.6,
            2.25:0.6,
            2.65:0.6,
            3.00:0.9,
            3.35:0.9,
            3.75:0.9,
            4.25:0.9,
            4.75:0.9,
            6.35:1.5, # A partir da 6.35, se usa oxigennio no laser
            7.94:1.5,
            9.53:2.2,
            12.70:3,
            15.88:3,
            19.04:3,
            22.22:3,
            25.40:3
        }
        return tabela.get(esp, "Espessura não encontrada na tabela") # vai retornar o valor da tabela, se nao encontrar, retorna uma exesão

    def calcular_geometria(self, peca):
        if peca.tipo == "r":
            peca.area_total = peca.medida_a * peca.medida_b
            peca.perimetro_total = 2 * (peca.medida_a + peca.medida_b)
        elif peca.tipo == "c":
            peca.area_total = 3.14 * (peca.medida_a ** 2)
            peca.perimetro_total = 2 * 3.14 * peca.medida_a
        elif peca.tipo == "t":
            peca.area_total = 0.5 * peca.medida_a * peca.medida_b
            peca.perimetro_total = peca.medida_a + peca.medida_b + (peca.medida_a**2 + peca.medida_b**2)**0.5

    def calcular_furos(self, peca):
        if peca.qtd_furos >0:
            perimetro_um_furo = 3.14 * peca.diam_furos
            peca.perimetro_total += perimetro_um_furo * peca.qtd_furos * 1.2
        

    def calcular_tempo(self, peca):
        velocidade_maq = self.tabela_velocidade_por_espessura(peca.esp)
        tempo_pierce = self.tabela_tempo_pierce_por_espessura(peca.esp)
        peca.velocidade_maq = velocidade_maq
        peca.tempo_pierce = tempo_pierce
        
        if isinstance(velocidade_maq, (int, float)):
            peca.tempo_corte_puro = peca.perimetro_total / velocidade_maq
            peca.tempo_total_lote = peca.tempo_corte_puro * peca.qtd   
        else:
            print(f"Erro de velocidade na peça tipo {peca.tipo}: {velocidade_maq}")
            peca.tempo_corte_puro = 0
            peca.tempo_total_lote = 0
            
        peca.tempo_unitario_real = (peca.tempo_pierce * peca.qtd_furos) + peca.tempo_corte_puro
        
#instanciando os objetos
calculadora = CalculadoraOrcamento()
meu_orcamento = Orcamento()
#carregando o json
with open ('lote_pecas.json', 'r', encoding='utf-8') as arquivo:
    dados_das_pecas = json.load(arquivo)

for dados_item in dados_das_pecas:
    nova_peca = PecaLaser(**dados_item)

    calculadora.calcular_geometria(nova_peca)
    calculadora.calcular_furos(nova_peca)
    calculadora.calcular_tempo(nova_peca)
    meu_orcamento.adicionar_peca(nova_peca)

meu_orcamento.exibir_relatorio_final()