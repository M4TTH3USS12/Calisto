from colors import *
from time import sleep
from comands.help import ajuda
import comands
print(f"\n{green}Calisto{reset} {yellow}- v0.1 iniciado{reset}")
print("\nDigite um comando ou digite 'sair' para encerrar.\n")
while True:
    comando = input(f"{blue}Usuário:{reset} ").strip().lower()
    if not comando.strip():
        print(f"{green}Calisto:{reset} Comando vazio, tente novamente...")
    elif comando == "sair":
        print(f"{green}Calisto:{reset} {yellow}encerrando...{reset}")
        sleep(1)
        exit()
    elif comando == "ajuda":
        ajuda()
