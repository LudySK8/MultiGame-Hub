def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vencedor(tabuleiro, jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    jogador_atual = 0

    for _ in range(9):
        exibir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogadores[jogador_atual]}, escolha a linha (0, 1, 2): "))
        coluna = int(input("Agora escolha a coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogadores[jogador_atual]
            if verificar_vencedor(tabuleiro, jogadores[jogador_atual]):
                exibir_tabuleiro(tabuleiro)
                print(f"Parabéns! Jogador {jogadores[jogador_atual]} venceu!")
                break
            jogador_atual = (jogador_atual + 1) % 2
        else:
            print("Essa posição já está ocupada. Tente novamente.")

    else:
        exibir_tabuleiro(tabuleiro)
        print("O jogo terminou em empate.")

if __name__ == "__main__":
    jogo_da_velha()