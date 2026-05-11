def pecas_orcamento(tipo, qtd, esp, medida_a, medida_b, qtd_furos, diam_furos):
    if tipo == "r":
        #===========Calculo de dimensões===========
        tempo_minutos = 0
        area = medida_a * medida_b
        perimetro = 2 * (medida_a + medida_b)
        velocidade_encontrada = tabela_velocidade_por_espessura(esp)
        
        #===========Calculo de furos===========
        if qtd_furos > 0:
            perimetro_furos = 3.14 * diam_furos
            perimetro += perimetro_furos * qtd_furos * 1.2
        if velocidade_encontrada == "Espessura não encontrada na tabela":
            print("Espessura não encontrada na tabela de velocidades.")
        else:
            tempo_minutos = (perimetro * qtd) / velocidade_encontrada
        calculos = {"tipo_peca": tipo,
                    "medida_a": medida_a,
                    "medida_b": medida_b,
                    "espessura": esp,
                    "qtd_furos": qtd_furos,
                    "qtd" : qtd,
                    "diam_furos": diam_furos,
                    "area_total": area,
                    "perimetro_total" : perimetro,
                    "velocidade" : velocidade_encontrada,
                    "tempo_minutos" : tempo_minutos}
        
        return calculos 
    elif tipo == "c":
        area = 3.14 * medida_a ** 2
        return area
    elif tipo == "t":
        area = 0.5 * medida_a * medida_b
        return area
def tabela_velocidade_por_espessura(espessura):
    tabela = {
        0.90:22100,
        2.00: 21250,
        3.00: 12750
    }
    return tabela.get(espessura, "Espessura não encontrada na tabela")
# Calculos de tempo / velocidade de corte
calculos = pecas_orcamento("r", 1, 2.00, 200, 200, 10, 15)
# Impressão dos resultados formatados.
def imprimir_calculos(calculos):
    print("--- RESUMO DO ORÇAMENTO ---")
    print(f"Tipo da peça: {calculos['tipo_peca']}")
    print(f"Medida A: {calculos['medida_a']:.2f}")
    print(f"Medida B: {calculos['medida_b']:.2f}")
    print(f"Espessura: {calculos['espessura']:.2f}")
    print(f"Quantidade de Peças: {calculos['qtd']}")
    print(f"Quantidade de furos: {calculos['qtd_furos']}")
    print(f"Diâmetro dos furos: {calculos['diam_furos']:.2f}")
    print(f"Área por peça: {calculos['area_total']:.2f}")
    print(f"Perímetro por peça: {calculos['perimetro_total']:.2f}")
    print(f"Velocidade de corte: {calculos['velocidade']} mm/min")
    print(f"Tempo total de corte: {calculos['tempo_minutos']:.2f} minutos")
imprimir_calculos(calculos)
