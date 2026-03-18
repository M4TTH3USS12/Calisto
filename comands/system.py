from colors import *
from time import sleep
import os
import platform
from datetime import datetime

def mensagem(texto):
    print(f"{green}CALISTO:{reset} {texto}")

def exit_system():
    mensagem(f"{yellow}Encerrando...{reset}")
    sleep(1)
    exit()

def limpar_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def hora_atual():
    horaAtual = datetime.now()
    mensagem(f"Agora são {horaAtual.strftime('%H:%M')}")

def data_atual():
    dataAtual = datetime.now()
    mensagem(f"Hoje é dia {dataAtual.strftime('%d/%m/%y')}")

def info_system():
    print(f'''\n----------- INFORMAÇÕES SISTEMA ----------
    Sistema: {platform.system()}
    Versão: {platform.version()}
    Arquitetura: {platform.machine()}
    Processador: {platform.processor()}
    Usuário: {os.getlogin()}
    Nome do PC: {platform.node()}
    Versão python: {platform.python_version()}
    Plataforma completa: {platform.platform()}
    ''')
    
def ping():
    mensagem("Calisto online")

def repetir():
    frase = input("Digite algo: ")
    mensagem(f"{frase}")

def status():
    mensagem(" ")
    print("---------- STATUS ----------")
    hora_atual()
    data_atual()
    info_system()