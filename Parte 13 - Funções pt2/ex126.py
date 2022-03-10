def notas(*nota, sit=False):
    if sit is False:
        listanotas = dict()
        listanotas['quant'] = len(nota)
        listanotas['maior'] = max(nota)
        listanotas['menor'] = min(nota)
        soma = 0
        for c in nota:
            soma = soma + c
        media = soma/len(nota)
        listanotas['media'] = media
        print(listanotas)
    if sit is True:
        listanotas = dict()
        listanotas['quant'] = len(nota)
        listanotas['maior'] = max(nota)
        listanotas['menor'] = min(nota)
        soma = 0
        for c in nota:
            soma = soma + c # para soma poderia ter usado sum(nota)
        media = soma / len(nota)
        listanotas['media'] = media
        if media >= 9:
            listanotas['situação'] = "Ótima"
        elif (media >= 7) and (media < 9):
            listanotas['situação'] = "Boa"
        elif (media < 7) and (media >= 5):
            listanotas['situação'] = "Razoável"
        elif (media < 5) and (media >= 2):
            listanotas['situação'] = "Ruim"
        elif media < 2:
            listanotas['situação'] = "Péssima"
        print(listanotas)


notas(2, 1.5, 2, 1, sit=True)


