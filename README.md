# Flask To-Do App

Este é um aplicativo simples de lista de tarefas (To-Do List) construído com o framework Flask e utilizando SQLite como banco de dados para armazenar as tarefas.

## Funcionalidades

- Adicionar novas tarefas à lista.
- Exibir todas as tarefas pendentes.
- Remover tarefas da lista.

## Tecnologias utilizadas

- **Flask**: Framework web leve em Python.
- **Flask-SQLAlchemy**: Extensão para integrar o banco de dados SQLite.
- **HTML/CSS**: Interface simples para interação do usuário.
- **SQLite**: Banco de dados embutido para armazenar as tarefas.

## Como rodar o projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/flask-todo-app.git
   ```
   
2. **Acesse o diretório do projeto**:
   ```bash
   cd flask-todo-app
   ```

3. **Crie um ambiente virtual** (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate   # Windows
   ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute o aplicativo**:
   ```bash
   python app.py
   ```

6. **Abra o navegador** e acesse:
   ```
   http://127.0.0.1:5000
   ```

## Estrutura do projeto

```plaintext
├── app.py              # Arquivo principal do Flask
├── todo.db             # Banco de dados SQLite (gerado automaticamente)
├── static/             # Arquivos estáticos (CSS, JS)
│   ├── css/
│   │   └── styles.css  # Estilos da interface
│   └── js/
│       └── scripts.js  # Arquivo JavaScript (opcional)
├── templates/          # Templates HTML
│   └── index.html      # Página principal do app
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
```

## Como contribuir

1. Faça um fork do projeto.
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-feature`).
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Sinta-se à vontade para utilizá-lo e modificá-lo conforme necessário.
