# WordList Black (v1.2)

![ASCII Art da Caveira com cifrões no terminal]

Gerador de wordlists modular, rápido e eficiente, construído em Python. O "WordList Black" utiliza permutações (combinações sem repetição) dos elementos fornecidos pelo usuário para criar dicionários personalizados, ideais para testes de segurança (auditoria de senhas) ou estudo de criptografia.

---

## 💻 Funcionalidades Principais

* **Geração Otimizada (Não Repetição):** Utiliza o módulo `itertools.permutations` do Python para garantir que cada elemento da lista seja usado apenas uma vez em cada senha gerada, focando em combinações únicas.
* **Controle de Entrada:** Permite que o usuário insira de 1 a 5 elementos-chave (palavras, números, símbolos) para gerar a wordlist.
* **Salva Automaticamente:** O arquivo final (`WordList Black.txt`) é salvo automaticamente na Área de Trabalho (Desktop) do usuário (com fallback para o diretório atual em caso de falha na detecção).

---

## ⚙️ Requisitos

* **Python:** Versão 3.x (o script foi testado com Python 3.9+).
* **Sistema Operacional:** Compatível com Linux, macOS e Windows.

O script utiliza apenas módulos nativos do Python (`os`, `sys`, `itertools`), **não sendo necessária a instalação de bibliotecas externas.**

---

## ▶️ Como Usar

### 1. Preparação

1.  Baixe o arquivo chamado `wordblack.py`.
2.  (Opcional, mas recomendado no Linux/macOS) Dê permissão de execução ao script:
    ```bash
    chmod +x wordblack.py
    ```

### 2. Execução

Abra o terminal na pasta onde você salvou o arquivo e execute o script usando o interpretador Python:

```bash
python wordblack.py
# OU, se estiver usando Python 3:
python3 wordblack.py
