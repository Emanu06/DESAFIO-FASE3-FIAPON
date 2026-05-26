def tomar_decisao(energia_total, consumo_total):

    if energia_total < 50 and consumo_total > 60:
        return "MODO ECONOMIA ATIVADO"

    elif energia_total < 50:
        return "ALERTA: reduzir consumo"

    elif consumo_total > energia_total:
        return "ALERTA: consumo maior que geração"

    else:
        return "SISTEMA OPERANDO NORMALMENTE"