from pathlib import Path
from dotenv import load_dotenv
import os


# Carrega variáveis do arquivo .env
load_dotenv()

# Configurações de mês e e-mails
MES_ANTERIOR = "Maio"
MES = "06 - Junho"
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO_PROP = os.getenv("EMAIL_TO_PROP")
EMAIL_TO_INQUILINO = os.getenv("EMAIL_TO_INQUILINO")

# Quantidade de imóveis a processar
QTD = 57

# Caminhos das pastas
BASE_PATH = Path('C:/Users/victo/Desktop/teste/boletos')
PASTA_BOLETOS = BASE_PATH / MES / 'Boletos'
PASTA_CONDOMINIO = BASE_PATH / MES / 'Taxa de Condomínio'
PASTA_REPASSES = BASE_PATH / MES / 'Repasses'
ARQ_EXCEL = BASE_PATH / 'Planilha nova 2025.xlsx'

# Caminho para imagem da logo
LOGO_PATH = BASE_PATH / "assets/lg.png"

# Caminhos para arquivos de entrada
TXT_ENDERECOS = BASE_PATH / "assets/enderecos.txt"
TXT_NOMES = BASE_PATH / "assets/nomes_inquilinos.txt"
TXT_EMAILS = BASE_PATH / "assets/emails_inquilinos.txt"