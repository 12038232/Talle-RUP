from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

proyectos = []
Estudiantes = []

# -------------------------
# PAGINA PRINCIPAL
# -------------------------

@app.route('/')
def index():
    return render_template('index.html')


# -------------------------
# PROYECTOS
# -------------------------

@app.route('/proyectos')
def lista_proyectos():
    return render_template('proyectos.html', proyectos=proyectos)


@app.route('/proyectos/nuevo', methods=['GET', 'POST'])
def nuevo_proyecto():

    if request.method == 'POST':

        proyecto = {
            'id': len(proyectos) + 1,
            'nombre': request.form['nombre'],
            'descripcion': request.form['descripcion'],
            'estado': request.form['estado']
        }

        proyectos.append(proyecto)

        return redirect(url_for('lista_proyectos'))

    return render_template('nuevo_proyecto.html')


@app.route('/proyectos/eliminar/<int:id>')
def eliminar_proyecto(id):

    global proyectos
    proyectos = [p for p in proyectos if p['id'] != id]

    return redirect(url_for('lista_proyectos'))


# -------------------------
# ESTUDIANTES
# -------------------------

@app.route('/estudiantes')
def lista_estudiantes():
    return render_template('Estudiantes.html', Estudiantes=Estudiantes)


@app.route('/estudiantes/registrar', methods=['GET', 'POST'])
def registrar_estudiante():

    if request.method == 'POST':

        estudiante = {
            'id': len(Estudiantes) + 1,
            'nombre': request.form['nombre'],
            'correo': request.form['correo']
        }

        Estudiantes.append(estudiante)

        return redirect(url_for('lista_estudiantes'))

    return render_template('registrar_estudiante.html')


@app.route('/estudiantes/eliminar/<int:id>')
def eliminar_estudiante(id):

    global Estudiantes
    Estudiantes = [e for e in Estudiantes if e['id'] != id]

    return redirect(url_for('lista_estudiantes'))


if __name__ == '__main__':
    app.run(debug=True)