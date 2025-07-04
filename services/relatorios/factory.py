from domain.relatorio import Relatorio
from services.relatorios.amil_relatorio import *
from core.interfaces import RelatorioService

def obter_servico_relatorio(relatorio: Relatorio) -> RelatorioService:
    if relatorio.tipo == "premio":
        return AmilRelatorioPremio()
    elif relatorio.tipo == "gerencial":
        return AmilRelatorioGerencial()
    else:
        raise NotImplementedError(f"Tipo de relatório não suportado: {relatorio.tipo}")