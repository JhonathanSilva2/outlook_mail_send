# outlool_mail_send
Script em python para enviar email pelo outlook

A função realiza as seguintes etapas:
<p>Cria uma instância do objeto SMTP para se conectar ao servidor SMTP do Outlook.</p>
* Chama os métodos ehlo() e starttls() para configurar a conexão segura.
* Faz login no servidor SMTP com um nome de usuário e senha (é necessário substituir 'Digite o seu email aqui' e 'Digite sua senha aqui' pelos valores corretos).
* Cria um objeto MIMEText com a mensagem em formato HTML.
* Define o destinatário e o assunto do email no cabeçalho da mensagem.
* Envia o email usando o método sendmail() do servidor SMTP, passando o remetente, destinatário e a mensagem em formato string.
*Finaliza a conexão com o servidor SMTP usando o método quit().
* Imprime "Email enviado com sucesso" se o email for enviado com êxito, ou imprime uma mensagem de erro se ocorrer uma exceção durante o envio.
* No final do código, a função enviar_email é chamada com os valores do destinatário (dest), assunto (sub) e mensagem (msg) para enviar o email.
