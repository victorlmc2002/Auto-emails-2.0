import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from pathlib import Path
from config import EMAIL_TO_PROP, EMAIL_PASSWORD, LOGO_PATH, MES_ANTERIOR
from email_utils.formatadores import formatar_texto_inquilino, formatar_texto_proprietario


def extrair_mensagem_assunto(caminho_arquivo):
    if isinstance(caminho_arquivo, list):
        caminho_arquivo = caminho_arquivo[0]
    nome_arquivo = Path(caminho_arquivo).stem
    partes = nome_arquivo.split(" - ", 1)[1]
    return partes.rsplit(" - ", 1)[0] if " - " in partes else partes


def criar_email(devedor, texto_formatado, anexos):
    msg = MIMEMultipart('related')
    msg['Subject'] = extrair_mensagem_assunto(anexos[0])
    msg['From'] = EMAIL_TO_PROP
    email_inquilino = devedor._email_inquilino
    if isinstance(email_inquilino, list):
        msg['To'] = email_inquilino[0]
        if len(email_inquilino) > 1:
            msg['Cc'] = ', '.join(email_inquilino[1:])
    else:
        msg['To'] = email_inquilino

    saudacao = f"Boa tarde, {devedor._nome_inquilino.split()[0].capitalize()}<br>"

    if devedor._cond is None:
        introducao = f"Segue o boleto referente ao aluguel do mês de {MES_ANTERIOR} e taxa de condomínio referente ao mês vigente em anexo"
    else:
        introducao = f"Segue o boleto referente ao mês de {MES_ANTERIOR} em anexo"

    corpo_email = f"""
        <p></p>
        {saudacao}
        {introducao}<br>
        <p><b>Valores:</b><br></p>
        {texto_formatado}  
    """

    if LOGO_PATH:
        corpo_email += '<br><img src="cid:imagem1"><br>'

    msg_alt = MIMEMultipart('alternative')
    msg.attach(msg_alt)
    msg_alt.attach(MIMEText(corpo_email, 'html'))

    if LOGO_PATH:
        with open(LOGO_PATH, 'rb') as img:
            mime_img = MIMEImage(img.read())
            mime_img.add_header('Content-ID', '<imagem1>')
            mime_img.add_header('Content-Disposition', 'inline', filename=Path(LOGO_PATH).name)
            msg.attach(mime_img)

    for anexo in anexos:
        if anexo:
            with open(anexo, 'rb') as f:
                part = MIMEApplication(f.read(), _subtype='pdf')
                part.add_header('Content-Disposition', 'attachment', filename=Path(anexo).name)
                msg.attach(part)

    return msg


def enviar_email(msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        s.starttls()
        s.login(msg['From'], EMAIL_PASSWORD)
        s.send_message(msg)
    print(f'Email enviado para {msg["To"]}')


def enviar_email_inquilino(devedor):
    if not devedor._pdfboleto:
        return

    anexos = [devedor._pdfboleto]
    if devedor._pdfcond:
        anexos.append(devedor._pdfcond)

    msg = criar_email(devedor, formatar_texto_inquilino(devedor), anexos)
    enviar_email(msg)


def enviar_email_proprietario(devedor):
    if not devedor._pdfrepasse:
        return

    msg = criar_email(
        devedor,
        formatar_texto_proprietario(devedor),
        [devedor._pdfrepasse] if isinstance(devedor._pdfrepasse, str) else devedor._pdfrepasse
    )
    enviar_email(msg)
