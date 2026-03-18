from colors import *
from comands import *

comandos = {
    "ajuda" : ajuda,
    "sair" : exit_system,
    "limpar terminal": limpar_terminal,
    "hora" : hora_atual,
    "data" : data_atual,
    "informações sistema" : info_system,
    "ping" : ping,
    "repetir": repetir,
    "status" : status
}

print(f"\n{green}Calisto{reset} {yellow}- v0.1 iniciado{reset}")
print("\nDigite um comando ou digite 'sair' para encerrar.\n")
while True:
    comando = input(f"{blue}USUÁRIO:{reset} ").strip().lower()
    if not comando:
        mensagem("Comando vazio, tente novamente...")
    elif comando in comandos:
        try:
            comandos[comando]()
        except Exception as erro:
            mensagem(f"ocorreu um erro ({erro})")
    else:
        mensagem("Comando inválido, digite 'ajuda' para exibir lista de comandos.")
