from pathlib import Path

# Configurações de mês e e-mails
MES_ANTERIOR = "Maio"
MES = "06 - Junho"
EMAIL_FROM = 'vigor.imob@gmail.com'
#EMAIL_PASSWORD = 'uryt lswm ptkb kuwq' #Vigor
EMAIL_PASSWORD = 'qzls bxhy uiei mtiv'
EMAIL_TO_PROP = 'victorlmc2002@gmail.com'
EMAIL_TO_INQUILINO = 'suporte@vigornegocios.com.br'

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