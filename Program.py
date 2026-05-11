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
            print(f"  Quantidade de furos: {peca.qtd_furos}")
            print(f"  Diâmetro dos furos: {peca.diam_furos:.2f} mm")
            print(f"  Área total: {peca.area_total:.2f} mm²")
            print(f"  Perímetro total: {peca.perimetro_total:.2f} mm")
            print(f"  Velocidade de corte: {peca.velocidade} mm/min")
            print(f"  Tempo de corte: {peca.tempo_corte:.2f} minutos")

            tempo_total_do_orcamento += peca.tempo_corte
        print("\n" + "-"*40)
        print(f"⏱️ TEMPO TOTAL DE MÁQUINA: {tempo_total_do_orcamento:.2f} minutos")
        print("-"*40 + "\n")


class PecaLaser:
    def __init__(self, tipo, qtd, esp, medida_a, medida_b, qtd_furos, diam_furos):
        self.tipo = tipo
        self.qtd = qtd
        self.esp = esp
        self.medida_a = medida_a
        self.medida_b = medida_b
        self.qtd_furos = qtd_furos
        self.diam_furos = diam_furos
        #Variaveis iniciadas
        self.area_total = 0
        self.perimetro_total = 0
        self.tempo_corte = 0
        self.velocidade = 0
# Calculo de geometrias com base no tipo da peca
class CalculadoraOrcamento:
    def tabela_velocidade_por_espessura(self, esp):
        tabela = {
            0.90:22100,
            2.00: 21250,
            3.00: 12750
        }
        return tabela.get(esp, "Espessura não encontrada na tabela")

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
        velocidade = self.tabela_velocidade_por_espessura(peca.esp)
        if isinstance(velocidade, (int, float)):
            peca.tempo_corte = (peca.perimetro_total * peca.qtd) / velocidade
        else:
            print(velocidade)
            peca.tempo_corte = 0
    
    
calculadora = CalculadoraOrcamento()
meu_orcamento = Orcamento()

peca1 = PecaLaser("r", 1, 2.00, 200, 200, 10, 15)
peca2 = PecaLaser("c", 2, 0.90, 100, 0, 5, 10)
peca3 = PecaLaser("t", 3, 3.00, 150, 100, 0, 0)

calculadora.calcular_geometria(peca1)
calculadora.calcular_furos(peca1)
calculadora.calcular_tempo(peca1)

calculadora.calcular_geometria(peca2)
calculadora.calcular_furos(peca2)
calculadora.calcular_tempo(peca2)

calculadora.calcular_geometria(peca3)
calculadora.calcular_furos(peca3)
calculadora.calcular_tempo(peca3)

meu_orcamento.adicionar_peca(peca1)
meu_orcamento.adicionar_peca(peca2)
meu_orcamento.adicionar_peca(peca3)

meu_orcamento.exibir_relatorio_final()