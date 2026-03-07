from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

proyectos = []
usuarios = []

@app.route('/')
def index():
    return render_template('index.html', proyectos=proyectos)

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
            'estado': request.form['estado'],
            'fecha': request.form['fecha']
        }
        proyectos.append(proyecto)
        return redirect(url_for('lista_proyectos'))
    return render_template('nuevo_proyecto.html')

@app.route('/proyectos/eliminar/<int:id>')
def eliminar_proyecto(id):
    global proyectos
    proyectos = [p for p in proyectos if p['id'] != id]
    return redirect(url_for('lista_proyectos'))

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    mensaje = None
    if request.method == 'POST':
        usuario = {
            'id': len(usuarios) + 1,
            'nombre': request.form['nombre'],
            'email': request.form['email'],
            'password': request.form['password']
        }
        usuarios.append(usuario)
        mensaje = f"¡Usuario {usuario['nombre']} registrado con éxito!"
    return render_template('registrar.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)