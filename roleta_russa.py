import random
import time

def roleta_russa():
    print("---------------------")
    print("=== ROULETA RUSSA ===")
    print("---------------------")
    print("Regras:")
    print("- O revólver tem 6 capsulas, uma com uma bala.")
    print("- Você gira o tambor, aperta o gatilho e torce para não cair no com a bala.")
    print("- Como toda rodada a bala é ralocada você pode sobreviver mesmo jogando até 6 vezes.\n")
    
    input("Pressione Enter para começar...")
    
    bala_pos = random.randint(1, 6)
    tambor_pos = 1
    
    for tentativa in range(1, 7):
        print(f"\nRodada {tentativa}")
        print("Girando o tambor...")
        time.sleep(1)
        
        tambor_pos = random.randint(1, 6)
        print(f"Posição do tambor: {tentativa}")
        
        print("Apertando o gatilho...")
        time.sleep(3)
        
        if tambor_pos == bala_pos:
            print("\nBANG! 💀")
            print("Você perdeu!")
            return
        else:
            print("*click*")
            print("Você sobreviveu... por enquanto.")
            
        if tentativa < 6:
            continuar = input("\ndeseja continuar? (s/n): ").lower()
            if continuar != 's':
                print("\nVocê desistiu. um verdadeiro covarde!")
                return
    
    print("\nVocê sobreviveu a todas as rodadas! Parabéns!")

if __name__ == "__main__":
    roleta_russa()