 import os

import pyaes


# --- Configurações ---

file_name = "teste.txt.ransomwaretroll"

chave = b"testeransomwares" # A mesma chave usada para criptografar


# --- Função Principal ---

def descriptografar_arquivo():

    try:

        # 1. Lê o arquivo criptografado

        with open(file_name, "rb") as file:

            file_data = file.read()


        # 2. Descriptografa

        aes = pyaes.AESModeOfOperationCTR(chave)

        decrypt_data = aes.decrypt(file_data)


        # 3. Remove o arquivo malicioso

        os.remove(file_name)


        # 4. Restaura o arquivo original

        original_file = "teste.txt"

        with open(original_file, "wb") as new_f:

            new_f.write(decrypt_data)


        print(f"[SUCESSO] Arquivo restaurado: {original_file}")


    except FileNotFoundError:

        print(f"Erro: O arquivo criptografado {file_name} não existe.")


if __name__ == "__main__":

    descriptografar_arquivo() 
