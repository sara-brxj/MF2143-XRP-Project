from machine import UART, Pin 
import time

uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1)) 

def get_ml_signal(): 
    if uart.any():
        line = uart.readline().decode('utf-8').strip() 
        if "bucketnoheld" in line:
            return "bucket"
    return None 

def get_voice_command(): 
    if uart.any(): 
        word = uart.readline().decode('utf-8').strip().lower()
        if word in ["go", "left", "right"]:
            return word 
    return None 
