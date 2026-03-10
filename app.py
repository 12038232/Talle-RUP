from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

proyectos = []
usuarios = []
Estudiantes = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proyectos')
def lista_proyectos():
    return render_template('proyectos.html', proyectos=proyectos)

@app.route('/proyectos/nuevo', methods=['GET','POST'])
def nuevo_proyecto():
    if request.method == 'POST':
        proyecto = {
            'id': len(proyectos)+1,
            'nombre': request.form['nombre'],
            'descripcion': request.form['descripcion'],
            'estado': request.form['estado']
        }
        proyectos.append(proyecto)
        return redirect(url_for('lista_proyectos'))

    return render_template('nuevo_proyecto.html')

@app.route('/proyectos/eliminar/<int:id>')
def eliminar(id):
    global proyectos
    proyectos = [p for p in proyectos if p['id'] != id]
    return redirect(url_for('lista_proyectos'))

@app.route('/registrar', methods=['GET','POST'])
def registrar():
    mensaje = None

    if request.method == 'POST':
        usuario = {
            'nombre': request.form['nombre'],
            'email': request.form['email']
        }

        usuarios.append(usuario)
        mensaje = "Usuario registrado correctamente"

        

    return render_template('Estudiantes.html', mensaje=mensaje)
@app.route('/Estudiantes')
def lista_Estudiantes():
    return render_template('Estudiantes.html', Estudiantes=Estudiantes)

@app.route('/Estudiantes/nuevo', methods=['GET','POST'])
def nuevo_Estudiantes():
    if request.method == 'POST':
        Estudiantes = {
            'id': len(Estudiantes)+1,
            'nombre': request.form['nombre']
        }
        Estudiantes.append(Estudiantes)
        return redirect(url_for('lista_Estudiantes'))

    return render_template('Estudiantes.html')

@app.route('/Estudiantes/eliminar/<int:id>')
def eliminar(id):
    global Estudiantes
    Estudiantes = [p for p in Estudiantes if p['id'] != id]
    return redirect(url_for('lista_Estudiantes'))

if __name__ == '__main__':
    app.run(debug=True)