from core.interfaces import RelatorioService
from playwright.sync_api import Page
from domain.relatorio import Relatorio
from abc import ABC, abstractmethod

class AmilRelatorioBase(RelatorioService, ABC):
    @abstractmethod
    def _obter_codigo_relatorio(self) -> int:
        pass

    def baixar(self, page: Page, relatorio: Relatorio):
        if not relatorio.esta_valido():
            raise ValueError("Relatório inválido.")

        codigo = self._obter_codigo_relatorio()
        url = f"https://www.amil.com.br/bioperadora/Relatorios/Telas.aspx?rel={codigo}"
        page.goto(url)

        self._adicionar_apolices(page, relatorio.empresas_apolices, relatorio.delay_ms)
        self._configurar_e_baixar_arquivo(page)

    def _adicionar_apolices(self, page: Page, empresas_apolices: dict[int, list[int]], delay_ms: int):
        page.wait_for_selector('xpath=//*[@id="ctl00_ContentPlaceHolder1_lbEscolherEmpresa"]', timeout=10000)
        page.locator('xpath=//*[@id="ctl00_ContentPlaceHolder1_lbEscolherEmpresa"]').click()
        page.wait_for_timeout(2000)

        for empresa_id, linhas in empresas_apolices.items():
            for linha in linhas:
                linha_formatada = f"{linha:02}"
                checkbox_xpath = f'xpath=//*[@id="ctl00_ContentPlaceHolder1_gvEmpresa_ctl{linha_formatada}_cbHolding"]'
                botao_adicionar_xpath = f'xpath=//*[@id="ctl00_ContentPlaceHolder1_gvEmpresa_ctl{linha_formatada}_btnAdicionar"]'

                try:
                    page.wait_for_selector(checkbox_xpath, timeout=10000)
                    page.locator(checkbox_xpath).click()

                    page.wait_for_selector(botao_adicionar_xpath, timeout=10000)
                    page.locator(botao_adicionar_xpath).click()

                    print(f"✅ Apólice da linha {linha} da empresa {empresa_id} adicionada.")
                except Exception as e:
                    print(f"⚠️ Erro na empresa {empresa_id}, linha {linha}: {e}")

                page.wait_for_timeout(delay_ms)

        try:
            page.locator('xpath=//*[@id="ctl00_ContentPlaceHolder1_btnAtualizarRelatorio"]').click()
            page.wait_for_load_state("networkidle", timeout=120000)
            print("🔄 Relatório atualizado com sucesso.")
        except Exception as e:
            print(f"⚠️ Erro ao atualizar relatório: {e}")

    def _configurar_e_baixar_arquivo(self, page: Page):
        # Implementar depois — pode ser sobrescrito se os relatórios forem muito diferentes
        pass
