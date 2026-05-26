def calcular_energia_total(colonia):
  
    solar = colonia["energia"]["solar"]["geracao"]
    eolica = colonia["energia"]["eolica"]["geracao"]
    reserva = colonia["energia"]["reserva"]

    return solar + eolica + reserva


def calcular_consumo_total(colonia):


    return sum(colonia["consumo"].values())


def exibir_status(colonia):

    

    energia_total = calcular_energia_total(colonia)
    consumo_total = calcular_consumo_total(colonia)

    print("\n===== STATUS DA COLÔNIA =====")

    print(f"Energia Total: {energia_total}")
    print(f"Consumo Total: {consumo_total}")

    print("\n--- Sistemas de Consumo ---")

    for sistema, valor in colonia["consumo"].items():
        print(f"{sistema}: {valor}")

    print("\n--- Clima ---")

    for dado, valor in colonia["clima"].items():
        print(f"{dado}: {valor}")


def gerar_relatorio_simples(
    energia_total,
    consumo_total,
    previsao,
    decisao
):

    
    relatorio = f"""


Energia Total: {energia_total}
Consumo Total: {consumo_total}

Previsão Eólica: {previsao}

Decisão do Sistema:
{decisao}

    """
    return relatorio