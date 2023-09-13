from flask import Flask, render_template, request, redirect, url_for, flash, session
from modelos import db, Docente, Escuela, Kit_escolar, Merienda_escolar, Sala_clase


# Crear aplicacion flask 
app = Flask(__name__)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "escuelas"


# Inicializar la base de datos
db.init_app(app)

## RUTAS ###

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el template base
@app.route('/base')
def base():
    return render_template('base.html')


### CRUD DEL DIRECTOR  - INICIO ###

# read del director
@app.route('/pedidos')
def pedidos():
    pedidos = Direccion.query.all()
    return render_template('pedidos.html', pedidos=pedidos)

# create del director
@app.route('/pedidos/nuevo', methods=['GET', 'POST'])
def nuevo_pedido():
    if request.method == 'POST':

        # recibimos datos que necesitamos del front
        merienda_escolar_fecha = request.form['merienda_escolar_fecha']
        merienda_escolar_cantidad = request.form['merienda_escolar_cantidad']
        merienda_escolar_precio_presupuesto = request.form['merienda_escolar_precio_presupuesto']
        merienda_escolar_precio_real = request.form['merienda_escolar_precio_real']
        merienda_escolar_obs = request.form['merienda_escolar_obs']
        kit_escolar_fecha = request.form['kit_escolar_fecha']
        kit_escolar_cantidad = request.form['kit_escolar_cantidad']
        kit_escolar_precio_presupuesto = request.form['kit_escolar_precio_presupuesto']
        kit_escolar_precio_real = request.form['kit_escolar_precio_real']
        kit_escolar_obs = request.form['kit_escolar_obs']

        # instanciamos un objeto de la clase Direccion
        direccion = Direccion(merienda_escolar_fecha=merienda_escolar_fecha, merienda_escolar_cantidad=merienda_escolar_cantidad, merienda_escolar_precio_presupuesto=merienda_escolar_precio_presupuesto, merienda_escolar_precio_real=merienda_escolar_precio_real, merienda_escolar_obs=merienda_escolar_obs, kit_escolar_fecha=kit_escolar_fecha, kit_escolar_cantidad=kit_escolar_cantidad, kit_escolar_precio_presupuesto=kit_escolar_precio_presupuesto, kit_escolar_precio_real=kit_escolar_precio_real, kit_escolar_obs=kit_escolar_obs)

        # agregamos el objeto a la base de datos
        db.session.add(direccion)

        # guardamos o confirmamos los cambios
        db.session.commit()

        # direccionamos de nuevo a pedidos
        return redirect(url_for('pedidos'))
    
# update del director
@app.route('/pedidos/editar/<id>', methods=['GET', 'POST'])
def editar_pedido(id):

    # buscamos el pedido en la base de datos
    pedido = Direccion.query.filter_by(id=id).first()

    if request.method == 'POST':
        # recibimos datos que necesitamos del front
        merienda_escolar_fecha = request.form['merienda_escolar_fecha']
        merienda_escolar_cantidad = request.form['merienda_escolar_cantidad']
        merienda_escolar_precio_presupuesto = request.form['merienda_escolar_precio_presupuesto']
        merienda_escolar_precio_real = request.form['merienda_escolar_precio_real']
        merienda_escolar_obs = request.form['merienda_escolar_obs']
        kit_escolar_fecha = request.form['kit_escolar_fecha']
        kit_escolar_cantidad = request.form['kit_escolar_cantidad']
        kit_escolar_precio_presupuesto = request.form['kit_escolar_precio_presupuesto']
        kit_escolar_precio_real = request.form['kit_escolar_precio_real']
        kit_escolar_obs = request.form['kit_escolar_obs']

        # actualizamos o editamos los datos del pedido
        pedido.merienda_escolar_fecha = merienda_escolar_fecha
        pedido.merienda_escolar_cantidad = merienda_escolar_cantidad
        pedido.merienda_escolar_precio_presupuesto = merienda_escolar_precio_presupuesto
        pedido.merienda_escolar_precio_real = merienda_escolar_precio_real
        pedido.merienda_escolar_obs = merienda_escolar_obs
        pedido.kit_escolar_fecha = kit_escolar_fecha
        pedido.kit_escolar_cantidad = kit_escolar_cantidad
        pedido.kit_escolar_precio_presupuesto = kit_escolar_precio_presupuesto
        pedido.kit_escolar_precio_real = kit_escolar_precio_real
        pedido.kit_escolar_obs = kit_escolar_obs

        # guardamos o confirmamos los cambios
        db.session.commit()

        # direccionamos de nuevo a pedidos
        return redirect(url_for('pedidos'))
    
    return render_template('editar_pedido.html', pedido=pedido, id=id)

# delete del director
@app.route('/pedidos/eliminar/<id>')
def eliminar_pedido(id):
    # buscamos el pedido en la base de datos
    pedido = Direccion.query.filter_by(id=id).first()
    
    # eliminamos el pedido de la base de datos
    db.session.delete(pedido)

    # guardamos o confirmamos los cambios
    db.session.commit()

    # direccionamos de nuevo a pedidos
    return redirect(url_for('pedidos'))

### CRUD DEL DIRECTOR  - FIN ###

### RUTAS ###
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/escuelas')
def escuelas():
    return render_template('escuelas.html')

@app.route('/docentes')
def docentes():
    return render_template('docentes.html')

@app.route('/kit/escolar')
def kit_escolar():
    return render_template('kit_escolar.html')

@app.route('/infraestructura')
def infraestructura():
    return render_template('infraestructura.html')

@app.route('/sala/clases')
def sala_clases():
    return render_template('sala_clases.html')






















### BREAKPOINT ###
if __name__ == '__main__':
    app.run(debug=True)