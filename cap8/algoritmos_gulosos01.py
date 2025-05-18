'''
Algoritmos Gulosos:
Objetivo: Dado um conjunto de aulas com horários de início e
fim, selecione o maior número de aulas que não se sobrepõem.
'''

aulas = {
    ('geo', 9, 10),
    ('hist', 9.5, 11),
    ('port', 10, 11),
    ('mat', 11, 12),
    ('socio', 11.5, 13),
    ('ing', 13, 14)
}

def agendar_aulas(aulas):
    aulas_ordenadas = sorted(aulas, key=lambda x: x[2])
    agenda = []
    fim_anterior = 0
    
    for aula in aulas_ordenadas:
        if aula[1] >= fim_anterior:
            agenda.append(aula[0])
            fim_anterior = aula[2]
        
    return agenda

print("Aulas agendadas: ", agendar_aulas(aulas))
