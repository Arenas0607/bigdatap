from flask import Flask, render_template

app = Flask(__name__)

# Página principal
@app.route('/')
def home():
    return render_template('page1.html')

# Página de resumen
@app.route('/presumen')
def presumen():
    return render_template('presumen.html')

# Página de objetivo
@app.route('/pobjetivo')
def pobjetivo():
    return render_template('pobjetivo.html')

# Página de sistema
@app.route('/psistema')
def psistema():
    return render_template('psistema.html')

# Página de componentes
@app.route('/pcompo')
def pcompo():
    return render_template('pcompo.html')

if __name__ == '__main__':
    app.run(debug=True)
