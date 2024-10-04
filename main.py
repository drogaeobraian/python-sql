from flask import Flask, render_template, redirect, request, flash
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LIMABRIAN'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    
    with open('usuarios.json') as usuariosTemp: 
        usuarios = json.load(usuariosTemp)
         
        cont = 0
         
        for usuario in usuarios:
            cont +=1
            
            if nome == 'adm' and senha == '000':
                return render_template("admcadastro.html")
            
            if usuario['nome'] == nome and usuario['senha'] == senha:
                 return render_template("usuario.html")
             
            if cont>=len(usuarios):
              flash('USUÁRIO INVÁLIDO')
              return render_template("/")
             
    

@app.route('/cadastro', methods=['POST'])
def cadastro():
    user = []
    cpf = request.form.get('cpf')
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    
    user = [
        {
        "cpf": cpf,
        "nome": nome,
        "email": email,
        "senha": senha
        }
    ]
    
    with open('usuarios.json') as usuariosTemp: 
        usuarios = json.load(usuariosTemp)
        
    usuarioNovo = usuarios + user    
    with open('usuarios.json', 'w') as gravarTemp: 
        json.dump(usuarioNovo, gravarTemp, indent=4)


    
    return render_template("usuario.html")
    
@app.route('/adm')
def adm(): 
    return render_template("admcadastro.html")

if __name__ in "__main__":
      app.run(debug=True)