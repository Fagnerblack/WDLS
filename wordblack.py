import itertools
import os
import sys

CAVEIRA_ASCII = r"""
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶_______________¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶______________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶________________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶__________________________¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶_____¶____________________¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶_¶______________________¶_¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶__¶_______________________¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶_¶____________________¶__¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶_¶___¶¶¶_________¶¶___¶__¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶_____¶¶¶¶¶__¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶____¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶______¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶________¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶¶________¶¶¶¶¶¶¶¶¶¶___¶¶¶
¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶
¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶____¶_¶¶_____¶¶¶¶¶¶¶¶¶¶¶_¶¶__¶¶¶
¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________¶¶¶¶¶¶¶¶__¶¶¶¶___¶¶
¶¶___¶¶¶_¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶_¶_¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶___¶
¶¶__¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶____¶_¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶___
¶___¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶____
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶
__¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶_¶¶¶__¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶__¶¶¶__¶¶¶¶¶¶__¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶__¶¶¶¶_¶_¶¶¶¶¶__¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶__¶¶_¶¶¶¶¶_¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶_¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶_¶¶¶¶¶___¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶__¶¶__¶¶_¶¶¶¶¶_¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶__¶__¶_¶¶¶¶¶¶¶¶¶¶¶__¶__¶¶_¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶_¶__¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶__¶¶_¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶__¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶__¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶
¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
-----------------Fagner_Santos--------------------
"""


INFO_CRIADOR = """
==============================================
[ WordList Black - Gerador de Wordlists ]
[ Versão: 1.2 | By FagnerSantos ]
==============================================
"""

def mostrar_tela_inicial():
    """Exibe o ASCII Art e as informações do criador."""
    print("\n" * 2)
    print(CAVEIRA_ASCII)
    print(INFO_CRIADOR)

def obter_elementos():
    """Obtém o número e as palavras/elementos do usuário."""
    while True:
        try:
            num_palavras = int(input("Quantos elementos deseja colocar (1 a 5)? "))
            if 1 <= num_palavras <= 5:
                break
            else:
                print("Escolha um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    elementos = []
    print("\n--- Digite seus Elementos ---")
    for i in range(1, num_palavras + 1):
        palavra = input(f"Elemento [{i}/{num_palavras}]: ").strip()
        if palavra:
            elementos.append(palavra)
        else:
            print("Elemento não pode ser vazio.")
            i -= 1
            
    return elementos

def encontrar_caminho_area_trabalho():
    """Tenta encontrar o caminho da Área de Trabalho ou usa o diretório atual."""
    desktop_paths = [
        os.path.join(os.path.expanduser('~'), 'Desktop'),
        os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop')
    ]
    for path in desktop_paths:
        if os.path.isdir(path):
            return path
    

    return os.getcwd()

def gerar_wordlist_e_salvar(elementos):
    """Gera as permutações e salva no arquivo 'WordList Black.txt'."""
    if not elementos:
        print("ERRO: Lista de elementos vazia.")
        return

    caminho_desktop = encontrar_caminho_area_trabalho()
    nome_arquivo = "WordList Black.txt"
    caminho_completo = os.path.join(caminho_desktop, nome_arquivo)
    
    
    tamanho_min = 1
    tamanho_max = len(elementos) 
    
    contador = 0
    print(f"\nGerando wordlist sem repetição ({len(elementos)} itens, tam. {tamanho_min}-{tamanho_max})...")

    try:
        with open(caminho_completo, 'w') as arquivo:
            for tamanho in range(tamanho_min, tamanho_max + 1):
                
                sys.stdout.write(f"\rProcessando tamanho {tamanho}...")
                sys.stdout.flush() 
                
                
                for senha_tuple in itertools.permutations(elementos, r=tamanho):
                    senha = "".join(senha_tuple)
                    arquivo.write(senha + '\n')
                    contador += 1
        
        
        print(f"\r\n--- SUCESSO! ---")
        print(f"Senhas geradas: {contador}. Salvo em: {caminho_completo}")

    except Exception as e:
        print(f"\r\nERRO: Falha ao salvar o arquivo.")
        print(f"Detalhes: {e}")

def main():
    """Função principal que executa o loop do programa."""
    while True:
        mostrar_tela_inicial()
        
        elementos = obter_elementos()
        
        gerar_wordlist_e_salvar(elementos)
        
        while True:
            continuar = input("\nDeseja criar mais uma wordlist? (Y/N): ").upper()
            if continuar in ['Y', 'N']:
                break
            else:
                print("Opção inválida.")

        if continuar == 'N':
            print("\nEncerrando...")
            sys.exit(0)

if __name__ == "__main__":
    main()