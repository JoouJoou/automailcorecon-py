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
    assunto = "Economista: seja o rosto da nossa campanha"

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
          button {
          width: 40%;
          background-color: #78A680;
          border-radius: 50px;
          margin: 0 auto;
          border: none; 
          display: block; 
          margin: 0 auto;
          }
          .button-bottom {
          width:30%;
          }
          a p {
          text-decoration: none;
          color: white;
          font-size: 14px;
          }
          
        </style>
      </head>
      <body>
      <button><a href="https://docs.google.com/forms/d/e/1FAIpQLSfGSJO3LNB-q3Nd-tSgjzIS5DAHQuaEr9W32QVj8LcZ9ObQJw/viewform" style="text-decoration: none; color: inherit;"><p>Clique AQUI e participe. Juntos fortalecemos a profissão!</p></a></button>
      <a href="https://docs.google.com/forms/d/e/1FAIpQLSfGSJO3LNB-q3Nd-tSgjzIS5DAHQuaEr9W32QVj8LcZ9ObQJw/viewform" style="text-align: center;"><img style="width: 530px; height: 600px; display: block; margin: 10px auto 10px auto;" src="https://i.imgur.com/RmUttWk.jpg"></a>
        <button class="button-bottom"><a href="https://docs.google.com/forms/d/e/1FAIpQLSfGSJO3LNB-q3Nd-tSgjzIS5DAHQuaEr9W32QVj8LcZ9ObQJw/viewform" style="text-decoration: none; color: inherit;"><p>13 de agosto: Dia do Economista</p></a></button>
        <p>Contamos com você!</p>
        <p>Sistema Cofecon/Corecons</p>
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