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
    escuela1 = Escuela(nombre="Atanacio Riera", departamento="Alto Paraná", ciudad="Ciudad del Este", barrio="Área 1", cantidad_alumnos=250, cantidad_alumnas=350)
    escuela2 = Escuela(nombre="Colegio San Francisco", departamento="Asunción", ciudad="Asunción", barrio="Centro", cantidad_alumnos=200, cantidad_alumnas=150)
    escuela3 = Escuela(nombre="Colegio Santa Clara", departamento="Caaguazú", ciudad="Coronel Oviedo", barrio="San Blas",cantidad_alumnos=250, cantidad_alumnas=200)



    ### cargar docentes ###
    # docentes de la escuela 1
    docente1_1 = Docente(nombre= 'Javier', apellido='Acosta', edad= 33, materia='Matematica', grado='3er', turno='tarde', antiguedad='4 años',escuela_id=1)
    docente1_2 = Docente(nombre= 'Rosana', apellido='Gonzalez', edad= 32, materia='Comunicacion', grado='4to', turno='tarde', antiguedad='10 años', escuela_id=1)
    docente1_3 = Docente(nombre= 'Cristian', apellido='Gimenez', edad=24, materia='Informatica', grado='5to', turno='mañana', antiguedad='6 años', escuela_id=1)
    docente1_4 = Docente(nombre= 'Pedro', apellido='Espinoza', edad= 26, materia='Ingles', grado='1er', turno='tarde', antiguedad='5 años', escuela_id=1)
    docente1_5 = Docente(nombre= 'Susana', apellido='Gutierrez', edad= 31, materia='Trabajo y Tecnologia', grado='2do', turno='tarde', antiguedad='8 años', escuela_id=1)
    docente1_6 = Docente(nombre= 'Gabriel', apellido='Parades', edad= 30, materia='Frances', grado='7mo', turno='mañana', antiguedad='6 años', escuela_id=1)
    # docentes de la escuela 2
    docente2_1 = Docente(nombre= 'Franco', apellido='Boggiano', edad= 23, materia='Educacion Fisica', grado='2do', turno='tarde', antiguedad='1 año',escuela_id=2)
    docente2_2 = Docente(nombre= 'Natasha', apellido='Fernandez', edad= 31 , materia='Musica', grado='1er', turno='manaña', antiguedad='5 años',escuela_id=2)
    docente2_3 = Docente(nombre= 'Oscar', apellido='Rivas', edad= 24 , materia='Ciencias', grado='6to', turno='tarde', antiguedad='3 años',escuela_id=2)
    docente2_4 = Docente(nombre= 'Leticia', apellido='Romero', edad= 45, materia='Matematica', grado='3ero', turno='tarde', antiguedad='16 años', escuela_id=2)
    docente2_5 = Docente(nombre= 'Eduardo', apellido='Ruiz', edad= 38, materia='Comunicacion', grado='4to', turno='mañana', antiguedad=' 11 años', escuela_id=2)
    docente2_6 = Docente(nombre= 'Gimena', apellido='Zarate', edad= 22, materia='Informatica', grado='6to', turno='mañana', antiguedad='3 años', escuela_id=2)
    # docentes de la escuela 3
    docente3_1 = Docente(nombre= 'Alexis', apellido='Echeverria', edad= 40 , materia='Artes Plasticas', grado='7mo', turno='tarde', antiguedad='15 años',escuela_id=3)
    docente3_2 = Docente(nombre= 'Rosa', apellido='Ferreira', edad= 25 , materia='Guarani', grado='8vo', turno='mañana', antiguedad='4 años',escuela_id=3)
    docente3_3 = Docente(nombre= 'Jazmin', apellido='Velazquez', edad= 32 , materia='Trabajo y Tecnologia', grado='9no', turno='tarde', antiguedad='7 años',escuela_id=3)
    docente3_4 = Docente(nombre= 'Raul', apellido='Galvan', edad= 37, materia='Matematica', grado='3ero', turno='tarde', antiguedad='7 años', escuela_id=3)
    docente3_5 = Docente(nombre= 'Roberto', apellido='Vaesken', edad= 31, materia='Religion', grado='1ero', turno='tarde', antiguedad='5 años', escuela_id=3)
    docente3_6 = Docente(nombre= 'Maria', apellido='Baez', edad= 26, materia='Salud', grado='5to', turno='mañana', antiguedad='4 años', escuela_id=3)

    ### Kit Escolar ###
    # kit escolar de la escuela 1
    kit_escolar1 = Kit_escolar(kit_entregado="455", kit_en_falta=145, fecha_entrega="23/01/2023", fecha_en_falta="10/06/2023", presupuesto_real=54300000, presupuesto_mec=70800000, escuela_id=1)
   
    # kit escolar de la escuela 2
    kit_escolar2 = Kit_escolar(kit_entregado="300", kit_en_falta=50, fecha_entrega="28/01/2023", fecha_en_falta="18/07/2023", presupuesto_real=31675000, presupuesto_mec=31900000, escuela_id=2)
    
    # kit escolar de la escuela 3
    kit_escolar3 = Kit_escolar(kit_entregado="380", kit_en_falta=70, fecha_entrega="15/01/2023", fecha_en_falta="21/08/2023", presupuesto_real=40725000, presupuesto_mec=40680000, escuela_id=3)

    ### Merienda Escolar ###
    # merienda escolar de la escuela 1
    merienda_escolar1 = Merienda_escolar(merienda_entregado="750", merienda_en_falta=450, fecha_entrega="20/02/2023", fecha_en_falta="10/06/2023", presupuesto_real=10200000, presupuesto_mec=12000000, escuela_id=1)

    # merienda escolar de la escuela 2
    merienda_escolar2 = Merienda_escolar(merienda_entregado="365", merienda_en_falta=335, fecha_entrega="17/02/2023", fecha_en_falta="15/06/2023", presupuesto_real=6100000, presupuesto_mec=6100000, escuela_id=2)

    # merienda escolar de la escuela 3
    merienda_escolar3 = Merienda_escolar(merienda_entregado="450", merienda_en_falta=450, fecha_entrega="19/02/2020", fecha_en_falta="1/07/2023", presupuesto_real=7470000, presupuesto_mec=7200000, escuela_id=3)


    ### Sala de Clase ###
    # sala de clase de la escuela 1
    sala_clase1 = Sala_clase(grado="5to", turno="Mañana", alumnos=30, alumnas=12, zurdos=2, diestros=28, pupitres_zurdos=2, pupitres_diestros=28, escuela_id=1)
    sala_clase2 = Sala_clase(grado="6to", turno="Tarde", alumnos=30, alumnas=12, zurdos=2, diestros=28, pupitres_zurdos=2, pupitres_diestros=28, escuela_id=1)
    sala_clase3 = Sala_clase(grado="7mo", turno="Mañana", alumnos=30, alumnas=12, zurdos=2, diestros=28, pupitres_zurdos=2, pupitres_diestros=28, escuela_id=1)

    # sala de clase de la escuela 2
    sala_clase4 = Sala_clase(grado="5to", turno="Mañana", alumnos=30, alumnas=12, zurdos=2, diestros=28, pupitres_zurdos=2, pupitres_diestros=28, escuela_id=2)
    sala_clase5 = Sala_clase(grado="6to", turno="Tarde", alumnos=30, alumnas=12, zurdos=2, diestros=28, pupitres_zurdos=2, pupitres_diestros=28, escuela_id=2)
    sala_clase6 = Sala_clase(grado="7mo", turno="Mañana", alumnos=30, alumnas=12, zurdos=2, diestros=28, pupitres_zurdos=2, pupitres_diestros=28, escuela_id=2)

    # sala de clase de la escuela 3
    sala_clase7 = Sala_clase(grado="5to", turno="Mañana", alumnos=30, alumnas=12, zurdos=2, diestros=28, pupitres_zurdos=2, pupitres_diestros=28, escuela_id=3)
    sala_clase8 = Sala_clase(grado="6to", turno="Tarde", alumnos=30, alumnas=12, zurdos=2, diestros=28, pupitres_zurdos=2, pupitres_diestros=28, escuela_id=3)
    sala_clase9 = Sala_clase(grado="7mo", turno="Mañana", alumnos=30, alumnas=12, zurdos=2, diestros=28, pupitres_zurdos=2, pupitres_diestros=28, escuela_id=3)



    # agregar a la base de datos
    db.session.add(escuela1)
    db.session.add(escuela2)
    db.session.add(escuela3)
    db.session.add(docente1_1)
    db.session.add(docente1_2)
    db.session.add(docente1_3)
    db.session.add(docente1_4)
    db.session.add(docente1_5)
    db.session.add(docente1_6)
    db.session.add(docente2_1)
    db.session.add(docente2_2)
    db.session.add(docente2_3)
    db.session.add(docente2_4)
    db.session.add(docente2_5)
    db.session.add(docente2_6)
    db.session.add(docente3_1)
    db.session.add(docente3_2)
    db.session.add(docente3_3)
    db.session.add(docente3_4)
    db.session.add(docente3_5)
    db.session.add(docente3_6)
    db.session.add(kit_escolar1)
    db.session.add(kit_escolar2)
    db.session.add(kit_escolar3)
    db.session.add(merienda_escolar1)
    db.session.add(merienda_escolar2)
    db.session.add(merienda_escolar3)
    db.session.add(sala_clase1)
    db.session.add(sala_clase2)
    db.session.add(sala_clase3)
    db.session.add(sala_clase4)
    db.session.add(sala_clase5)
    db.session.add(sala_clase6)
    db.session.add(sala_clase7)
    db.session.add(sala_clase8)
    db.session.add(sala_clase9)
    db.session.commit()