from flask import Flask, render_template, request
import re

app = Flask(__name__)

def validate_password(password):
    if len(password) < 8:
        return "❌ La contraseña debe tener al menos 8 caracteres."
    if not re.search(r"[A-Z]", password):
        return "❌ Debe contener al menos una letra mayúscula."
    if not re.search(r"[a-z]", password):
        return "❌ Debe contener al menos una letra minúscula."
    if not re.search(r"[0-9]", password):
        return "❌ Debe contener al menos un número."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "❌ Debe contener al menos un símbolo especial."
    return "✅ La contraseña es válida."

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        password = request.form['password']
        result = validate_password(password)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
