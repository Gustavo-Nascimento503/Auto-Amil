from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from core.automation_flow import executar_fluxo
from services.amil_login import AmilLogin
from services.relatorios.amil_relatorio import *
from config import obter_credenciais  # certifique-se que essa função está nesse arquivo
from domain.relatorio import Relatorio
from config_apolices import EMPRESAS_APOLICES

load_dotenv()

empresa_id = 987
usuario, senha = obter_credenciais(str(empresa_id))

relatorio = Relatorio(
    tipo="gerencial",
    empresas_apolices={empresa_id: EMPRESAS_APOLICES[empresa_id]},
    delay_ms=2000
)

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    contexto = navegador.new_context()

    login_service = AmilLogin()
    relatorio_service = AmilRelatorioGerencial()

    

    executar_fluxo(login_service, relatorio_service, contexto, usuario, senha, relatorio)
