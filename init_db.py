from modelos import db, Escuela, Docente, Kit_escolar, Merienda_escolar, Sala_clase
from flask import Flask 


# Crear aplicacion flask 
app = Flask(__name__)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "escuelas"

db.init_app(app)

# Crear tablas en la base de datos
with app.app_context():
    db.create_all()

# Cargamos los datos en la base de datos
with app.app_context():

    ### cargar escuelas ###
    escuela1 = Escuela(nombre="Virgen del Rosario", departamento="Alto Parana", ciudad="Hernandarias", barrio="Las Americas", cantidad_alumnos=150)
    escuela2 = Escuela(nombre="Atanacio Riera", departamento="Alto Parana", ciudad="CDE", barrio="Area 1", cantidad_alumnos=200)
    escuela3 = Escuela(nombre="San Jose School", departamento="Alto Parana", ciudad="CDE", barrio="San Jose", cantidad_alumnos=300)


    ### cargar docentes ###
    # docentes de la escuela 1
    docente1_1 = Docente(nombre="Juan", apellido="Perez", edad=30, materia="Matematicas", grado="5to", turno="Mañana", antiguedad='10 anhos', escuela_id=1)
    docente1_2 = Docente(nombre="Maria", apellido="Gonzalez", edad=30, materia="Lengua", grado="6to", turno="Tarde", antiguedad='7 anhos', escuela_id=1)
    docente1_3 = Docente(nombre="Pedro", apellido="Gimenez", edad=30, materia="Ciencias", grado="7mo", turno="Mañana", antiguedad='5 anhos', escuela_id=1)

    # docentes de la escuela 2
    docente2_1 = Docente(nombre="Marcos", apellido="Acunha", edad=30, materia="Matematicas", grado="5to", turno="Mañana", antiguedad='10 anhos', escuela_id=2)
    docente2_2 = Docente(nombre="Roberto", apellido="Muriel", edad=30, materia="Lengua", grado="6to", turno="Tarde", antiguedad='7 anhos', escuela_id=2)
    docente2_3 = Docente(nombre="Mariza", apellido="Gamarra", edad=30, materia="Ciencias", grado="7mo", turno="Mañana", antiguedad='5 anhos', escuela_id=2)

    # docentes de la escuela 3
    docente3_1 = Docente(nombre="Monse", apellido="Aranda", edad=30, materia="Matematicas", grado="5to", turno="Mañana", antiguedad='10 anhos', escuela_id=3)
    docente3_2 = Docente(nombre="Lujan", apellido="Aranda", edad=30, materia="Lengua", grado="6to", turno="Tarde", antiguedad='7 anhos', escuela_id=3)
    docente3_3 = Docente(nombre="Tutu", apellido="Fer", edad=30, materia="Ciencias", grado="7mo", turno="Mañana", antiguedad='5 anhos', escuela_id=3)

    ### Kit Escolar ###
    # kit escolar de la escuela 1
    kit_escolar1 = Kit_escolar(kit_entregado="Si", kit_en_falta=0, fecha_entrega="10/10/2020", fecha_en_falta="N/A", presupuesto_real="1000000", presupuesto_mec="1000000", escuela_id=1)
   
    # kit escolar de la escuela 2
    kit_escolar2 = Kit_escolar(kit_entregado="Si", kit_en_falta=0, fecha_entrega="10/10/2020", fecha_en_falta="N/A", presupuesto_real="1000000", presupuesto_mec="1000000", escuela_id=2)
    
    # kit escolar de la escuela 3
    kit_escolar3 = Kit_escolar(kit_entregado="Si", kit_en_falta=0, fecha_entrega="10/10/2020", fecha_en_falta="N/A", presupuesto_real="1000000", presupuesto_mec="1000000", escuela_id=3)

    ### Merienda Escolar ###
    # merienda escolar de la escuela 1
    merienda_escolar1 = Merienda_escolar(merienda_entregado="Si", merienda_en_falta=0, fecha_entrega="10/10/2020", fecha_en_falta="N/A", presupuesto_real="1000000", presupuesto_mec="1000000", escuela_id=1)

    # merienda escolar de la escuela 2
    merienda_escolar2 = Merienda_escolar(merienda_entregado="Si", merienda_en_falta=0, fecha_entrega="10/10/2020", fecha_en_falta="N/A", presupuesto_real="1000000", presupuesto_mec="1000000", escuela_id=2)

    # merienda escolar de la escuela 3
    merienda_escolar3 = Merienda_escolar(merienda_entregado="Si", merienda_en_falta=0, fecha_entrega="10/10/2020", fecha_en_falta="N/A", presupuesto_real="1000000", presupuesto_mec="1000000", escuela_id=3)


    ### Sala de Clase ###
    # sala de clase de la escuela 1
    sala_clase1 = Sala_clase(grado="5to", turno="Mañana", alumnos=30, alumnas=12, zurdos=2, diestros=28, pupitres_zurdos=2, pupitres_diestros=28, escuela_id=1)


    # agregar a la base de datos
    db.session.add(escuela1)
    db.session.add(escuela2)
    db.session.add(escuela3)
    db.session.add(docente1_1)
    db.session.add(docente1_2)
    db.session.add(docente1_3)
    db.session.add(docente2_1)
    db.session.add(docente2_2)
    db.session.add(docente2_3)
    db.session.add(docente3_1)
    db.session.add(docente3_2)
    db.session.add(docente3_3)
    db.session.add(kit_escolar1)
    db.session.add(kit_escolar2)
    db.session.add(kit_escolar3)
    db.session.add(merienda_escolar1)
    db.session.add(merienda_escolar2)
    db.session.add(merienda_escolar3)
    db.session.add(sala_clase1)
    db.session.commit()
