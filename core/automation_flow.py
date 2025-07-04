from core.interfaces import LoginService, RelatorioService
from playwright.sync_api import BrowserContext
from domain.relatorio import Relatorio

def executar_fluxo(
    login_service: LoginService,
    relatorio_service: RelatorioService,
    context: BrowserContext,
    usuario: str,
    senha: str,
    relatorio: Relatorio
):
    aba_login = context.new_page()
    login_service.login(aba_login, usuario, senha)

    with context.expect_page() as nova_aba_evento:
        aba_login.locator('xpath=//*[@id="app"]/div[2]/div[1]/div/div[3]/div[2]/nav/div/ul/div[9]/a').click()

    nova_aba = nova_aba_evento.value
    aba_login.close()

    relatorio_service.baixar(nova_aba, relatorio)