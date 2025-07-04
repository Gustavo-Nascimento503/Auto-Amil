from services.relatorios.amil_relatorio_base import AmilRelatorioBase

class AmilRelatorioPremio(AmilRelatorioBase):
    def _obter_codigo_relatorio(self) -> int:
        return 31

class AmilRelatorioGerencial(AmilRelatorioBase):
    def _obter_codigo_relatorio(self) -> int:
        return 5