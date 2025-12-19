from machine import UART, Pin
import time

# UART setup for Coral communication [cite: 35, 61]
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

def get_ml_signal():
    """Checks for Object Detection signals from the Coral board"""
    if uart.any():
        signal = uart.read(1).decode('utf-8')
        if signal == 'bucketnoheld': 
            return "BUCKET"
    return None

def wait_for_keyword(target):
    """Blocks until the VSC-modified KWS model detects the keyword """
    print(f"Listening for: {target}")
    while True:
        if uart.any():
            word = uart.readline().decode('utf-8').strip()
            if word == target:
                return True
        time.sleep(0.1)
