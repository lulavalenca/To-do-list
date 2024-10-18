from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo para tarefas (Todo)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Rota para exibir a lista de tarefas
@app.route('/')
def index():
    todos = Todo.query.all()  # Busca todas as tarefas do banco de dados
    return render_template('index.html', todos=todos)

# Rota para adicionar uma nova tarefa
@app.route('/add', methods=['POST'])
def add_todo():
    todo_title = request.form.get('todo')
    if todo_title:
        new_todo = Todo(title=todo_title, completed=False)
        db.session.add(new_todo)
        db.session.commit()  # Salva a nova tarefa no banco de dados
    return redirect(url_for('index'))

# Rota para deletar uma tarefa
@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()  # Remove a tarefa do banco de dados
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Cria a tabela 'todos' no banco de dados, se ainda não existir
    app.run(debug=True)