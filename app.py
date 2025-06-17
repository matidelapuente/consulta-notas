from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

df_notas = pd.read_excel('notas.xlsx')

@app.route('/', methods=['GET', 'POST'])
def index():
    mensaje = None
    if request.method == 'POST':
        dni_ingresado = request.form['dni']
        resultado = df_notas[df_notas['dni'].astype(str) == dni_ingresado]
        if not resultado.empty:
            nota_valor = resultado.iloc[0]['nota']
            if pd.isna(nota_valor):
                mensaje = "No ha rendido el parcial."
            else:
                try:
                    nota_num = float(nota_valor)
                    if nota_num < 4:
                        mensaje = "Desaprobado"
                    else:
                        mensaje = f"Tu nota es: {nota_num}"
                except ValueError:
                    mensaje = "ValueError"
        else:
            mensaje = "DNI no encontrado."
    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)