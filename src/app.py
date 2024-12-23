from flask import Flask, render_template, url_for, request, flash, redirect, jsonify
from src.models.models import *
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        asunto = request.form['asunto']
        mensaje = request.form['mensaje']

        try:
            with sql.connect('formulario.db') as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    INSERT INTO formulario (nombre, correo, asunto, mensaje)
                    VALUES (?, ?, ?, ?)
                    """,
                    (nombre, correo, asunto, mensaje),
                )
                conn.commit()
            
            return redirect('/')  # Redirige después del submit
        except Exception as e:
            flash("Error: Faltan datos obligatorios", "danger")  # Mensaje de error
            return redirect('/')
    return "Método no permitido."







if __name__ == '__main__':
    # create_db()
    # create_table()
    # delete_rows('Mauro')
    app.run(debug = True)
