import random

# Escolhe uma palavra
palavra = random.choice(["for_code", "python", "fantasma", "ferrari", "lobo"])
descobertas = ["_"] * len(palavra)
tentativas = 6

print("Bem-vindo ao Jogo da Forca!")

# Loop principal do jogo
while tentativas > 0 and "_" in descobertas:
    print("\nPalavra:", " ".join(descobertas))
    print(f"Tentativas restantes: {tentativas}")
    
    letra = input("Digite uma letra: ").lower()
    
    if letra in palavra:
        # letras descobertas
        for i, l in enumerate(palavra):
            if l == letra:
                descobertas[i] = letra
    else:
        tentativas -= 1
    
# Resultado final
if "_" not in descobertas:
    print("\nParabéns! Você adivinhou a palavra:", palavra)
else:
    print("\nVocê perdeu! A palavra era:", palavra)
