import os
import platform
from datetime import datetime

def limpar_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def hora_atual():
    horaAtual = datetime.now()
    print(f"Agora são {horaAtual.strftime('%H:%M')}")

def data_atual():
    dataAtual = datetime.now()
    print(f"Hoje é dia {dataAtual.strftime("%d/%m/%y")}")

hora_atual()
data_atual()
input("Digite para limpar")
limpar_terminal()