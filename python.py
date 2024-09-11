from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Configurações de e-mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'kadjanascimento58@gmail.com'  # Insira seu e-mail
app.config['MAIL_PASSWORD'] = 'kadja123.!'  # Insira sua senha de app
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    assunto = request.form.get('assunto')
    mensagem = request.form.get('mensagem')

    # Criando a mensagem de e-mail
    msg = Message(subject=f"Mensagem de {nome}: {assunto}",
                  sender='kadjanascimento58@gmail.com',  # O e-mail remetente (o mesmo das configurações)
                  recipients=['destinatario@gmail.com'])  # E-mail(s) destinatário(s)
    msg.body = f"""
    Nome: {nome}
    Email: {email}
    Telefone: {telefone}
    
    Mensagem:
    {mensagem}
    """

    # Enviando o e-mail
    mail.send(msg)

    return 'Sua mensagem foi enviada com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
