from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()

def obter_credenciais(empresa):
    usuario = os.getenv(f"{empresa}_USUARIO")
    senha = os.getenv(f"{empresa}_SENHA")

    if not usuario or not senha:
        raise Exception(f"Credenciais não encontradas para {empresa}")

    return usuario, senha