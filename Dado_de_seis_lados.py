import random

def rolar_dado():
    return random.randint(1, 6)
def main():
    print("Dado de 6 Lados")
    print("----------------------------")
    
    while True:
        input("Pressione Enter para rolar o dado")
        resultado = rolar_dado()
        print(f"Resultado: {resultado}\n")
        
        continuar = input("Deseja rolar novamente? (s/n): ").lower()
        if continuar != 's':
            print("Fim do Jogo")
            break
if __name__ == "__main__":
    main()