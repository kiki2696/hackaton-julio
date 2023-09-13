from flask_sqlalchemy import SQLAlchemy


# crear objeto SQLAlchemy
db = SQLAlchemy()

### MODELOS ###

# Crear modelo de escuela
class Escuela(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    departamento = db.Column(db.String(100), nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    barrio = db.Column(db.String(100), nullable=False)
    cantidad_alumnos = db.Column(db.Integer, nullable=False)
    cantidad_alumnas = db.Column(db.Integer, nullable = False)
    # relaciones con otras tablas
    docente = db.relationship('Docente', backref='escuela', lazy=True)
    kit_escolar = db.relationship('Kit_escolar', backref='escuela', lazy=True)
    merienda_escolar = db.relationship('Merienda_escolar', backref='escuela', lazy=True)
    sala_clase = db.relationship('Sala_clase', backref='escuela', lazy=True)

class Docente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    grado = db.Column(db.String(100), nullable=False)
    turno = db.Column(db.String(100), nullable=False)
    antiguedad = db.Column(db.String(100), nullable=False)
    # relacionamos docente con escuela
    escuela_id = db.Column(db.Integer, db.ForeignKey('escuela.id'), nullable=False)

class Kit_escolar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kit_entregado = db.Column(db.String(100), nullable=False)
    kit_en_falta = db.Column(db.Integer)
    fecha_entrega = db.Column(db.String(100), nullable=False)
    fecha_en_falta = db.Column(db.String(100), nullable=False) 
    presupuesto_real = db.Column(db.String(100), nullable=False)
    presupuesto_mec = db.Column(db.String(100), nullable=False)
    # relacionamos kit_escolar con escuela
    escuela_id = db.Column(db.Integer, db.ForeignKey('escuela.id'), nullable=False)


class Merienda_escolar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    merienda_entregado = db.Column(db.String(100), nullable=False)
    merienda_en_falta = db.Column(db.Integer)
    fecha_entrega = db.Column(db.String(100), nullable=False)
    fecha_en_falta = db.Column(db.String(100), nullable=False) 
    presupuesto_real = db.Column(db.Integer, nullable=False)
    presupuesto_mec = db.Column(db.Integer, nullable=False)
    # relacionamos merienda_escolar con escuela
    escuela_id = db.Column(db.Integer, db.ForeignKey('escuela.id'), nullable=False)


class Sala_clase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grado = db.Column(db.String(100), nullable=False)
    turno = db.Column(db.String(100))
    alumnos = db.Column(db.Integer, nullable=False) 
    alumnas = db.Column(db.Integer, nullable=False) 
    zurdos = db.Column(db.Integer, nullable=False)
    diestros = db.Column(db.Integer, nullable=False)
    pupitres_zurdos = db.Column(db.Integer, nullable=False)
    pupitres_diestros = db.Column(db.Integer, nullable=False)
    # relacionamos sala_clase con escuela
    escuela_id = db.Column(db.Integer, db.ForeignKey('escuela.id'), nullable=False)