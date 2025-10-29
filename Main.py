import os
import requests

def print_banner():
    banner = """
 ███▄    █  ▒█████  ▒██   ██▒     █████▒██▀███   ▒█████   ███▄ ▄███▓
 ██ ▀█   █ ▒██▒  ██▒▒▒ █ █ ▒░   ▓██   ▒▓██ ▒ ██▒▒██▒  ██▒▓██▒▀█▀ ██▒
▓██  ▀█ ██▒▒██░  ██▒░░  █   ░   ▒████ ░▓██ ░▄█ ▒▒██░  ██▒▓██    ▓██░
▓██▒  ▐▌██▒▒██   ██░ ░ █ █ ▒    ░▓█▒  ░▒██▀▀█▄  ▒██   ██░▒██    ▒██ 
▒██░   ▓██░░ ████▓▒░▒██▒ ▒██▒   ░▒█░   ░██▓ ▒██▒░ ████▓▒░▒██▒   ░██▒
░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░    ▒ ░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ░  ░
░ ░░   ░ ▒░  ░ ▒ ▒░ ░░   ░▒ ░    ░       ░▒ ░ ▒░  ░ ▒ ▒░ ░  ░      ░
   ░   ░ ░ ░ ░ ░ ▒   ░    ░      ░ ░     ░░   ░ ░ ░ ░ ▒  ░      ░   
         ░     ░ ░   ░    ░               ░         ░ ░         ░   
                                                                     """
    print(banner)

def extract_web_code(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        with open("NoxFrom.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("\n[+] Archivo 'NoxFrom.html' Se Ha Guardado en La Misma Carpeta Del el Script.")
    except Exception as e:
        print(f"\n[-] Error al extraer el código: {e}")

def main():
    print_banner()
    print("\n1. Extract all the code from a website")
    print("Not Responsible for Use/nMisuse of this tool")
    
    option = input("Seleccione una opción (1): ")
    if option == "1":
        url = input("\nColoca La Url Que Quieres Copiar: ")
        if url.startswith("http://") or url.startswith("https://"):
            extract_web_code(url)
        else:
            print("\n[-] Incorrecto, Debes Colocar una Url Como http:// o https://).")
    else:
        print("\n[-] es del 1 Oiste Idiota .")

if __name__ == "__main__":
    main()