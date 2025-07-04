from playwright.sync_api import Page
from dotenv import load_dotenv
import os
load_dotenv()

from core.interfaces import LoginService
from playwright.sync_api import Page

class AmilLogin(LoginService):
    def login(self, page: Page, usuario: str, senha: str):
        print(f"Iniciando login para {usuario}")

        page.goto("https://www.amil.com.br/empresa/#/login")

        page.fill('xpath=//*[@id="login"]/div/div/section/section/form/div/div[1]/div/div/div/div/input', usuario)
        page.fill('xpath=//*[@id="login"]/div/div/section/section/form/div/div[2]/div[1]/div/div/div/div/input', senha)
        page.locator('xpath=//*[@id="login"]/div/div/section/section/form/div/div[3]/div[1]/div/div/button').click()
        
        page.wait_for_url("https://www.amil.com.br/empresa/#/")

        print("Login realizado com sucesso.")

