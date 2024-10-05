'''1)Dada uma função f(x) qualquer, calcule a área aproximada 
entre o gráfico e o eixo X e entre os valores x1 e x2.
•Dica: Utilize a soma dos retângulos internos da área (exemplo).'''

#resolvi calcular usando a área de um semi-cículo e cheguei ao raio 4
#ps:Não entendi essa questão completamente

import math

# Raio do semicírculo com base nas infos da prova
raio = 4

# Cálculo da área do semicírculo
area_semicirculo = (math.pi * raio**2) / 2

print("Área do semicírculo:", area_semicirculo)