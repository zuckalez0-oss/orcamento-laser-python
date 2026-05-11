def tabela_velocidade_por_espessura(espessura):
    tabela = {
        0.90:22100,
        2.00: 21250,
        3.00: 12750
    }
    return tabela.get(espessura, "Espessura não encontrada na tabela")

def pecas_orcamento(tipo, qtd, esp, medida_a, medida_b, qtd_furos, diam_furos):
    area = 0
    perimetro_base = 0
    tempo_minutos = 0
    # RECTANGLE
    if tipo == "r": 
        area = medida_a * medida_b
        perimetro_base = 2 * (medida_a + medida_b)
        #velocidade_encontrada = tabela_velocidade_por_espessura(esp)
    # CIRCLE 
    elif tipo == "c":
        area = 3.14 * (medida_a ** 2)
        perimetro_base = 2 * 3.14 * medida_a  
    elif tipo == "t":
        area = 0.5 * medida_a * medida_b
        perimetro_base = medida_a + medida_b + (medida_a**2 + medida_b**2)**0.5
        
    perimetro_total = perimetro_base
    if qtd_furos > 0:
            perimetro_total += (3.14 * diam_furos) * qtd_furos * 1.2
    velocidade = tabela_velocidade_por_espessura(esp)
    if isinstance(velocidade, (int, float)):
        tempo_minutos = (perimetro_total * qtd) / velocidade 
    else:
        tempo_minutos = 0

    return {"tipo_peca": tipo,
                "medida_a": medida_a,
                "medida_b": medida_b,
                "espessura": esp,
                "qtd_furos": qtd_furos,
                "qtd" : qtd,
                "diam_furos": diam_furos,
                "area_total": area,
                "perimetro_total" : perimetro_total,
                "velocidade" : velocidade,
                "tempo_minutos" : tempo_minutos}    
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
