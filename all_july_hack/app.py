from flask import Flask, render_template, request, redirect, url_for, flash, session
from modelos import db, Escuela, Docente, Merienda_escolar, Kit_escolar, Sala_clase


# Crear aplicacion flask 
app = Flask(__name__)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "escuelas"

# Inicializar la base de datos
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/tutu')
def tutu():
    escuela = Escuela.query.all()

    print(type(escuela))

    return render_template('tutu.html', escuela=escuela)



# TODAS LAS ESCUELAS
@app.route('/homepage')
def homepage():

    # Obtener la consulta de búsqueda desde los parámetros de la URL
    search_query = request.args.get('buscador', '')

    # Realizar la consulta de Escuelas con filtro por nombre, departamento y ciudad solo si hay una consulta de búsqueda
    if search_query:
        escuelas = Escuela.query.filter(
            (Escuela.nombre.ilike(f'%{search_query}%')) |
            (Escuela.departamento.ilike(f'%{search_query}%')) |
            (Escuela.ciudad.ilike(f'%{search_query}%'))
        ).all()
    else:
        # Si no hay consulta de búsqueda, mostrar todas las escuelas (sin filtrar)
        escuelas = Escuela.query.all()

    return render_template('homepage.html', escuelas=escuelas)




# ESCUELAS
@app.route('/escuela/<id>')
def escuela(id):
    
        # Escuelas 
        escuelas = Escuela.query.get(id)
    
    
        return render_template('escuela.html', escuelas=escuelas, id=id)

# MERIENDA ESCOLAR
@app.route('/escuela/kit/<id>')
def escuela_kit(id):

    # Supongamos que tienes el ID de la escuela para la que deseas obtener la información de merienda escolar
    # escuela_id = 1  # Reemplaza 1 con el ID de la escuela que desees

    # Realizar la consulta de Merienda Escolar
    merienda_escolar = Merienda_escolar.query.filter_by(id=id).all()

    # Realizar la consulta de Kit Escolar
    kit_escolar = Kit_escolar.query.filter_by(id=id).all()

    return render_template('escuela_kit.html', merienda_escolar=merienda_escolar, kit_escolar=kit_escolar, id=id)

# Colegios Docentes
@app.route('/colegios/docente/<id>')
def colegios_docente(id):
    
        # # Realizar la consulta de Merienda Escolar
        # docentes = Docente.query.filter_by(escuela_id=id).all()

    # Obtener la consulta de búsqueda desde los parámetros de la URL
    search_query = request.args.get('buscador', '')

    # Realizar la consulta de Merienda Escolar con filtros (materia, grado, turno) solo si hay una consulta de búsqueda
    if search_query:
        docentes = Docente.query.filter(
            (Docente.escuela_id == id) &
            ((Docente.materia.ilike(f'%{search_query}%')) |
             (Docente.grado.ilike(f'%{search_query}%')) |
             (Docente.nombre.ilike(f'%{search_query}%')) |
             (Docente.apellido.ilike(f'%{search_query}%')) |
             (Docente.turno.ilike(f'%{search_query}%')))
        ).all()
    else:
        # Si no hay consulta de búsqueda, mostrar todos los profesores de la escuela (sin filtrar)
        docentes = Docente.query.filter_by(escuela_id=id).all()

    
    return render_template('colegios_docente.html', docentes=docentes, id=id)

# Colegios Sala de Clases
@app.route('/colegios/sala/<id>')
def colegios_sala(id):
     
     # Realizar consulta de Sala de Clases
    salas = Sala_clase.query.filter_by(escuela_id=id).all()

    return render_template('colegios_sala.html',salas=salas, id=id)











### BREAKPOINT ###
if __name__ == '__main__':
    app.run(debug=True)