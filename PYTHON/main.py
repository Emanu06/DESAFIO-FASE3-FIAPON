# main.py
from data import colonia
from decision import tomar_decisao
from regression import prever_energia
from energy_analysis import analisar_energia
from utils import (
    calcular_energia_total,
    calcular_consumo_total,
    exibir_status,
    gerar_relatorio_simples
)


exibir_status(colonia)

energia_total = calcular_energia_total(colonia)

consumo_total = calcular_consumo_total(colonia)

decisao = tomar_decisao(
    energia_total,
    consumo_total
)

print(f"\nDecisão: {decisao}")


vento = colonia["clima"]["vento"]

previsao = prever_energia(vento)

print(f"Previsão de energia eólica: {previsao}")


analise = analisar_energia(
    energia_total,
    consumo_total,
    colonia["energia"]["reserva"]
)

print(f"Análise: {analise}")


relatorio = gerar_relatorio_simples(
    energia_total,
    consumo_total,
    previsao,
    decisao
)

print(relatorio)