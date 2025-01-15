from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

# Fazendo Página Estática e styles.css
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dynamic/<name>')
def dynamic(name):
    current_date = datetime.now().strftime('%d/%m/%Y')
    return render_template('dynamic.html', name=name, current_date=current_date)

# Executa o aplicativo LOCALMENTE (localhost) na porta 5000
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)