from dataclasses import dataclass
import matplotlib.pyplot as plt

aceleracao_gravidade = -9.8

perguntas = ["Tempo da simulação(em segundos): ",
             "Massa do objeto(em Kilograma): ",
             "Velocidade inicial do objeto(em metros por segundo): ",
             "Altura que o objeto será lançado em relação ao chão(em metros): "]

respostas = []
pergunta_atual = 0
positivo = True

while pergunta_atual < len(perguntas):

    try:
        resp = input(perguntas[pergunta_atual])

        if pergunta_atual not in (2, 3) and int(resp) < 0:
            raise ValueError()

        respostas.append(int(resp))
        pergunta_atual += 1

    except ValueError:
        print("Não pode ser menor que zero ou nulo!")

@dataclass
class Objeto:
    massa_kg: int
    velocidade: float
    altura_m: float
    metros_andados: float = 0

def main():
    
    bola = Objeto(respostas[1], respostas[2], respostas[3])
    resultado_vel = []
    resultado_pos = []

    for i in range(respostas[0]):
        variacao_t = (i+1) - i

        velocidade_media = bola.velocidade
        bola.velocidade += aceleracao_gravidade
        velocidade_media = (velocidade_media + bola.velocidade)/2


        bola.altura_m += velocidade_media * variacao_t
        bola.metros_andados -= velocidade_media * variacao_t

        resultado_vel.append(bola.velocidade)
        resultado_pos.append(bola.altura_m)

    eixo_y = []
    for i in range(respostas[0]):
        eixo_y.append(i)

    plt.plot(eixo_y, resultado_pos)
    plt.show()


    for i in range(len(resultado_vel)):
        print(f"{i+1}° segundo:")
        print(f"Velocidade: {round(resultado_vel[i], 2)} ")
        print(f"Posição atual: {round(resultado_pos[i], 2)}\n")
        

if __name__ == "__main__":
    main()