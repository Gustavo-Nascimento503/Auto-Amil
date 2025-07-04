# 🩺 Automação Portal Amil — Relatórios via Playwright

Projeto de automação de extração de relatórios do portal Amil, com login automático, seleção de apólices por empresa e suporte a múltiplos tipos de relatórios (prêmio, gerencial). Estrutura baseada nos princípios SOLID e programação orientada a objetos (POO).

---

## 🚀 Tecnologias

- Python 3.12
- Playwright
- dotenv
- Estrutura SOLID (POO)
- pytest (FUTURO)

---

## 🗂️ Estrutura do Projeto

```
autoamilSolid/
│
├── core/                  # Núcleo da aplicação (fluxo e interfaces)
│   └── automation_flow.py # Coordena o fluxo de login + relatório
│   └── interfaces.py      # Define contratos para serviços
│
├── services/              # Implementações específicas dos serviços
│   └── amil_login.py
    └── factory.py
│   └── relatorios/
│       ├── amil_relatorio_premio.py
│       └── amil_relatorio_gerencial.py
│
├── domain/                # Modelos de domínio
│   └── relatorio.py       # Classe Relatorio (tipo, apólices, validação)
│
├── config/                # Configurações e leitura de .env
│   └── apolices_por_empresa.py
│   └── credenciais.py     # Função obter_credenciais
│
├── helpers/               # Funções utilitárias (futuro)
│
├── tests/                 # Testes com pytest (em breve)
│
├── .env                   # Variáveis sensíveis (não versionado)
├── .gitignore             # Ignora .env, __pycache__, etc.
└── main.py                # Ponto de entrada da aplicação
```

---

## 🧠 Camadas explicadas

### ✅ `core/`
Contém a **lógica central da automação**, desacoplada de implementações específicas:

- `automation_flow.py`: define a função `executar_fluxo()`, que orquestra login, abertura de aba, e o processo de baixar relatórios.
- `interfaces.py`: define interfaces abstratas (`LoginService`, `RelatorioService`) para aplicar o princípio da **inversão de dependência (D - SOLID)**.

---

### ✅ `services/`
Implementações específicas para o portal Amil.

- `amil_login.py`: implementa `LoginService` com login no site da Amil.
- `relatorios/amil_relatorio_premio.py`: implementa `RelatorioService` para relatório de prêmio.
- `relatorios/amil_relatorio_gerencial.py`: implementação específica para relatório gerencial.
- `factory.py`: função obter_servico_relatorio que retorna o serviço de relatório correto (AmilRelatorioPremio ou AmilRelatorioGerencial) conforme o tipo do relatório recebido, garantindo a separação de responsabilidades.

---

### ✅ `domain/`
Modelos que representam o domínio da aplicação.

- `relatorio.py`: classe `Relatorio` com tipo (`premio`, `gerencial`), empresas e delay. Possui método de validação.

---

### ✅ `config/`
Centraliza configurações e dados variáveis:

- `credenciais.py`: função `obter_credenciais(empresa_id)` que carrega dados do `.env`.
- `apolices_por_empresa.py`: mapeamento de empresas para suas linhas de apólice no relatório.

---

### ✅ `helpers/`
Camada opcional para funções auxiliares reutilizáveis (ex: conversores, validadores).

---

## 💻 Como rodar

1. Instale as dependências:
```bash
pip install -r requirements.txt
playwright install
```

2. Configure seu arquivo `.env`:
```env
1234_USUARIO=seu_usuario 1234 = IDEMPRESA
1234_SENHA=sua_senha
```

3. Rode a automação:
```bash
python main.py
```

---

## ✨ Exemplo de uso

```python
relatorio = Relatorio(
    tipo="premio",
    empresas_apolices={
        1234: [2, 3, 4],
        8872: [5, 6]
    },
    delay_ms=2000
)
```

---

## 🧪 Testes

> A camada de testes com `pytest` será adicionada em breve, com mocks das interfaces.

---

## 🔒 Segurança

- As credenciais são lidas do `.env` via `dotenv` e **nunca são versionadas** (ver `.gitignore`).
- O projeto está pronto para expansão com múltiplas operadoras e tipos de relatório.

---

## 📌 Status

✔️ Login e seleção de empresas/apólices  
✔️ Suporte a tipos de relatório: prêmio e gerencial  
🛠️ Em desenvolvimento: filtros e download final  
🧪 Em breve: cobertura de testes