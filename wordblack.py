import itertools
import os
import sys

# ASCII Art da Caveira
# Fonte: Customizada para o projeto.
CAVEIRA_ASCII = r"""
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/
"""

# Informações do Criador (limpas)
INFO_CRIADOR = """
==============================================
[ WordList Black - Gerador de Wordlists ]
[ Versão: 1.0 | Por Gemini ]
==============================================
"""

def mostrar_tela_inicial():
    """Exibe o ASCII Art e as informações do criador."""
    print("\n" * 2)
    print(CAVEIRA_ASCII) # Agora exibe a caveira
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
            i -= 1 # Repete a iteração
            
    return elementos

def encontrar_caminho_area_trabalho():
    """Tenta encontrar o caminho da Área de Trabalho ou usa o diretório atual."""
    desktop_paths = [
        os.path.join(os.path.expanduser('~'), 'Desktop'),
        os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop') # Para alguns PCs Windows
    ]
    for path in desktop_paths:
        if os.path.isdir(path):
            return path
    
    # Fallback: se não encontrar, usa o diretório atual
    return os.getcwd()

def gerar_wordlist_e_salvar(elementos):
    """Gera as combinações e salva no arquivo 'WordList Black.txt'."""
    if not elementos:
        print("ERRO: Lista de elementos vazia.")
        return

    caminho_desktop = encontrar_caminho_area_trabalho()
    nome_arquivo = "WordList Black.txt"
    caminho_completo = os.path.join(caminho_desktop, nome_arquivo)
    
    # Tamanhos de 1 a 7 (ajustável)
    tamanho_min = 1
    tamanho_max = 7
    
    contador = 0
    print(f"\nGerando wordlist ({len(elementos)} itens, tam. {tamanho_min}-{tamanho_max})...")

    try:
        with open(caminho_completo, 'w') as arquivo:
            for tamanho in range(tamanho_min, tamanho_max + 1):
                # Mensagem de progresso mínima
                sys.stdout.write(f"\rProcessando tamanho {tamanho}...")
                sys.stdout.flush() 
                
                for senha_tuple in itertools.product(elementos, repeat=tamanho):
                    senha = "".join(senha_tuple)
                    arquivo.write(senha + '\n')
                    contador += 1
        
        # Mensagem final de sucesso
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