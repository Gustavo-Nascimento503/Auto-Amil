from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Relatorio:
    tipo: str  # Ex: "premio"
    empresas_apolices: Dict[int, List[int]]  # {empresa_id: [linhas de apólice]}
    delay_ms: int = 2000

    def esta_valido(self) -> bool:
        return bool(self.empresas_apolices) and self.tipo in ["premio", "gerencial"]