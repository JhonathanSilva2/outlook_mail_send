# Outlook Mail Send
Script em python para enviar email pelo outlook

A função realiza as seguintes etapas:
<p>Cria uma instância do objeto SMTP para se conectar ao servidor SMTP do Outlook.</p>
<ul>
<li>Chama os métodos ehlo() e starttls() para configurar a conexão segura.</li>
</ul>
<li>
Faz login no servidor SMTP com um nome de usuário e senha (é necessário substituir 'Digite o seu email aqui' e 'Digite sua senha aqui' pelos valores corretos).
</li>
<li>
Cria um objeto MIMEText com a mensagem em formato HTML.
</li>
<li>
Define o destinatário e o assunto do email no cabeçalho da mensagem.  
</li>
<li>
Envia o email usando o método sendmail() do servidor SMTP, passando o remetente, destinatário e a mensagem em formato string.  
</li>
<li>
Finaliza a conexão com o servidor SMTP usando o método quit().
</li>
<li>
Imprime "Email enviado com sucesso" se o email for enviado com êxito, ou imprime uma mensagem de erro se ocorrer uma exceção durante o envio.
</li>
<li>
  No final do código, a função enviar_email é chamada com os valores do destinatário (dest), assunto (sub) e mensagem (msg) para enviar o email. 
</li>
