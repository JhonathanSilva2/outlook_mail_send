import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, mensagem):
    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.ehlo()
        server.starttls()
        server.login('Digite o seu email aqui', 'Digite sua senha aqui')
        message = MIMEText(mensagem,'html')
        message['to'] = destinatario
        message['subject'] = assunto
        server.sendmail('email que seria usado para enviar email', destinatario, message.as_string())
        server.quit()
        print ('Email enviado com sucesso')
    except Exception as e:
        print ('Erro ao enviar o email:', e)    

dest='Digite o email destinatário aqui'

sub = 'Digite o titulo do emal'

msg = """
A mensagem será digitada aqui
"""
enviar_email(dest,sub,msg)
