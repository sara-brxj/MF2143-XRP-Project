from machine import UART, Pin
import time

# UART setup for Coral communication [cite: 35, 61]
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

def get_ml_signal():
    if uart.any():
        signal = uart.read(1).decode('utf-8')
        if signal == 'bucketnoheld': 
            return "bucket"
    return None

def wait_for_keyword(target):
    print(f"Listening for: {target}")
    while True:
        if uart.any():
            word = uart.readline().decode('utf-8').strip()
            if word == target:
                return True
        time.sleep(0.1)
