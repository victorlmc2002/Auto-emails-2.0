from pathlib import Path
from dotenv import load_dotenv
import os


# Carrega variáveis do arquivo .env
load_dotenv()

# Caminhos da pasta base
BASE_PATH = Path('C:/Users/victo/Desktop/teste/boletos')


# Caminho para imagem da logo
LOGO_PATH = BASE_PATH / "assets/lg.png"

# Caminhos para arquivos de entrada
TXT_ENDERECOS = BASE_PATH / "assets/enderecos.txt"
TXT_NOMES_INQUILINOS = BASE_PATH / "assets/nomes_inquilinos.txt"
TXT_EMAILS_INQUILINOS = BASE_PATH / "assets/emails_inquilinos.txt"
TXT_EMAILS_PROP = BASE_PATH / "assets/emails_prop.txt"
TXT_NOMES_PROP = BASE_PATH / "assets/nomes_prop.txt"
TXT_MES = BASE_PATH / "assets/mês_vigente.txt"

# Configurações de mês e e-mails
with open(TXT_MES, "r", encoding="utf-8") as arquivo:
    MES_ANTERIOR = arquivo.readline().strip()
    MES = arquivo.readline().strip()
    
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO_PROP = os.getenv("EMAIL_TO_PROP")
EMAIL_TO_INQUILINO = os.getenv("EMAIL_TO_INQUILINO")

# Caminhos para pastas de PDF e Excel
PASTA_BOLETOS = BASE_PATH / MES / 'Boletos'
PASTA_CONDOMINIO = BASE_PATH / MES / 'Taxa de Condomínio'
PASTA_REPASSES = BASE_PATH / MES / 'Repasses'
ARQ_EXCEL = BASE_PATH / 'Planilha nova 2025.xlsx'