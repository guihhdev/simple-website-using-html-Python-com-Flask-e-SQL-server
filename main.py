from flask import Flask, request, render_template, redirect
import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-H8DS6M0\TEW_SQLEXPRESS;"
    "Database=DP2;"
)
conexao = pyodbc.connect(dados_conexao)
print("Conexao Bem Sucedida")
cursor = conexao.cursor()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Gui'


@app.route('/')       #/home
def home():
    return render_template('home.html')


@app.route('/cadastro')                  #('/')
def form():
    return render_template('login.html')             #'(login.html')

@app.route('/login', methods=['POST'])
def login():

    codigo = request.form.get("codigo") 
    nome = request.form.get("nome")
    idade = request.form.get("idade")

    print(codigo)
    print(nome)
    print(idade)

    comando = """INSERT INTO cadastro (codigo, nome, idade) VALUES (?, ?, ?);"""
    cursor.execute(comando, (codigo, nome, idade))
    conexao.commit()  # Não se esqueça de cometer as alterações
    print("Dados inseridos com sucesso.")

    return redirect('/')          #return redirect ('/')


if __name__ == '__main__':
    app.run(debug=True)






   
 
    

