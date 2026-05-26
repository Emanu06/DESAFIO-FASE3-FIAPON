def analisar_energia(geracao, consumo, reserva):

    if consumo > geracao:
        return "ALERTA: consumo maior que geração"

    elif geracao > consumo:
        excedente = geracao - consumo

        if excedente > 20:
            return "SUGESTÃO: armazenar energia excedente"

        return "Energia estável"

    elif reserva < 10:
        return "ALERTA: reserva crítica"

    return "Sistema equilibrado"