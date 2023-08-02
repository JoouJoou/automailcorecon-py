import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage


def enviar_email(email_destinatario):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    username = "coreconpe2015@gmail.com"
    senha_app = "grna psun juzu hhol"
    assunto = "Corecon-PE: Convite para seminário em comemoração ao Dia do Economista"

    corpo_email = """\
    <html>
      <head>
        <style>
          body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 10px;
            background-color: #f0f0f0;
          }
          p {
            color: #333;
            font-size: 16px;
            line-height: 1.6;
          }
          strong {
            font-weight: bold;
          }
          em {
            font-style: italic;
          }
        </style>
      </head>
      <body>
      <p style="text-align: center;"><img style="width: 500px; height: 500px; display: block; margin: 0 auto;" src="https://i.imgur.com/A486WYG.png"></p>
        <p>O Corecon-PE convida a todos para o seminário comemorativo ao <strong>Dia do Economista 2023</strong>, que será realizado em 16 de agosto, no Auditório do Banco Central, em Recife, localizado na Rua da Aurora 1259, das 14h às 17h.</p>
        <p>Esse ano o evento conta com as palestras do Econ. Antonio Corrêa de Lacerda (PUCSP), que falará sobre <em>“O papel do Estado e do BNDES para o desenvolvimento”</em>, e do Econ. Fábio Silva, que falará sobre os <em>"Desafios do mercado de trabalho para os Economistas"</em>. As palestras serão seguidas de um debate com a Profa. Dra. Poema Souza (Vice-Presidente do Corecon-PE e Profa. Adjunta da UFRPE), que terá a moderação do Econ. André Morais (Presidente do Corecon-PE).</p>
        <p>No momento, como tradicionalmente, será realizada a cerimônia de premiação dos vencedores do <strong>XVII Prêmio Pernambuco de Economia Dirceu Pessoa</strong>.</p>
        <p>Inscreva-se em www.sympla.com.br/coreconpe</p>
        <p style="text-align: center;"><img style="width: 200px; height: 60px; display: block; margin: 0 auto;" src="https://i.imgur.com/lMh1zlt.png"></p>
        
      </body>
    </html>
    """

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, senha_app) 

        mensagem = MIMEMultipart()
        mensagem["From"] = username
        mensagem["To"] = email_destinatario
        mensagem["Subject"] = assunto

        parte_texto = MIMEText(corpo_email, "html")
        mensagem.attach(parte_texto)

        server.sendmail(username, email_destinatario, mensagem.as_string())
        print(f"E-mail enviado para {email_destinatario} com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail para {email_destinatario}: {str(e)}")
    finally:
        server.quit()
with open('emails.csv', 'r', encoding='utf-8-sig') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        email_destinatario = row['email']
        enviar_email(email_destinatario)