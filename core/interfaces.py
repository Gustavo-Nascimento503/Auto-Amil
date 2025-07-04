from abc import ABC, abstractmethod
from playwright.sync_api import Page
from domain.relatorio import Relatorio

class LoginService(ABC):
    @abstractmethod
    def login(self, page: Page, usuario: str, senha: str):
        pass

class RelatorioService(ABC):
    @abstractmethod
    def baixar(self, page: Page, relatorio: Relatorio):
        pass