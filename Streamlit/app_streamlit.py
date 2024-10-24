import streamlit as st
import requests

# Endpoint base de la API Flask
API_BASE_URL = "http://127.0.0.1:5000"

# Variable para almacenar el token JWT
jwt_token = ""

# Función para registrar un nuevo usuario
def registrar_usuario():
    st.title("Registrar Usuario")
    username = st.text_input("Nombre de usuario", key="username_register")  # Agregar key único
    password = st.text_input("Contraseña", type="password", key="password_register")  # Agregar key único
    
    if st.button("Registrar Usuario"):
        data = {
            "username": username,
            "password": password
        }
        response = requests.post(f"{API_BASE_URL}/auth/register", json=data)

        if response.status_code == 201:
            st.success("Usuario registrado exitosamente")
        else:
            st.error("Hubo un error al registrar el usuario")

# Función para iniciar sesión y obtener el token JWT
def login():
    if "jwt_token" not in st.session_state:
        st.session_state["jwt_token"] = ""
    
    st.sidebar.header("Iniciar sesión")
    
    # Credenciales de usuario
    username = st.sidebar.text_input("Usuario", key="login_username")
    password = st.sidebar.text_input("Contraseña", type="password", key="login_password")
    
    if st.sidebar.button("Iniciar sesión"):
        login_data = {
            "username": username,
            "password": password
        }
        response = requests.post(f"{API_BASE_URL}/auth/login", json=login_data)
        
        if response.status_code == 200:
            st.session_state["jwt_token"] = response.json()['token']  # Guardar el token en session_state
            st.sidebar.success("Sesión iniciada correctamente")
        else:
            st.sidebar.error("Credenciales inválidas")

# Función para registrar ingreso
def registrar_ingreso():
    st.header("Registrar Ingreso")

    # Verificar si se ha iniciado sesión
    if not jwt_token:
        st.error("Debes iniciar sesión primero.")
        return

    # Formulario para ingreso de datos
def registrar_ingreso():
    st.header("Registrar Ingreso")

    # Verificar si se ha iniciado sesión
    if "jwt_token" not in st.session_state or not st.session_state["jwt_token"]:
        st.error("Debes iniciar sesión primero.")
        return

    # Formulario para ingreso de datos
    fecha = st.date_input("Fecha del ingreso")
    concepto = st.text_input("Concepto")
    valor = st.number_input("Valor", min_value=0)
    tipo = st.selectbox("Tipo de ingreso", ["Ingreso operativo", "Ingreso pasivo", "Otro"])
    metodo = st.selectbox("Método de pago", ["Efectivo", "Nequi", "DaviPlata", "Falabella"])
    
    if st.button("Registrar Ingreso"):
        # Crear el payload
        ingreso_data = {
            "fecha": fecha.strftime("%Y-%m-%d"),
            "concepto": concepto,
            "valor": valor,
            "tipo": tipo,
            "metodo": metodo
        }

        # Incluir el token en los headers
        headers = {
            "Authorization": f"Bearer {st.session_state['jwt_token']}"
        }

        # Hacer la solicitud POST a la API Flask
        response = requests.post(f"{API_BASE_URL}/ingresos", json=ingreso_data, headers=headers)

        if response.status_code == 201:
            st.success("Ingreso registrado exitosamente")
        else:
            st.error("Hubo un error al registrar el ingreso")

# Función para registrar gasto
def registrar_gasto():
    st.header("Registrar Gasto")

    # Verificar si se ha iniciado sesión
    if "jwt_token" not in st.session_state or not st.session_state["jwt_token"]:
        st.error("Debes iniciar sesión primero.")
        return

    # Formulario para gasto
    fecha = st.date_input("Fecha del gasto")
    concepto = st.text_input("Concepto")
    valor = st.number_input("Valor", min_value=0)
    tipo = st.selectbox("Tipo de gasto", ["Gasto fijo", "Gasto variable", "Gasto de emergencia", "Gasto operacional", "Préstamo"])
    metodo = st.selectbox("Método de pago", ["Efectivo", "Nequi", "DaviPlata", "Falabella"])
    
    if st.button("Registrar Gasto"):
        # Crear el payload
        gasto_data = {
            "fecha": fecha.strftime("%Y-%m-%d"),
            "concepto": concepto,
            "valor": valor,
            "tipo": tipo,
            "metodo": metodo
        }

        # Incluir el token en los headers
        headers = {
            "Authorization": f"Bearer {st.session_state['jwt_token']}"
        }

        # Hacer la solicitud POST a la API Flask
        response = requests.post(f"{API_BASE_URL}/gastos", json=gasto_data, headers=headers)

        if response.status_code == 201:
            st.success("Gasto registrado exitosamente")
        else:
            st.error("Hubo un error al registrar el gasto")

# Función para generar reportes
def generar_reporte():
    st.header("Generar Reporte")

    # Verificar si se ha iniciado sesión
    if "jwt_token" not in st.session_state or not st.session_state["jwt_token"]:
        st.error("Debes iniciar sesión primero.")
        return

    # Formulario de filtros
    categoria = st.selectbox("Categoría", ["Ingreso operativo", "Ingreso pasivo", "Otro", "Gasto fijo", "Gasto variable", "Otro"])
    metodo = st.selectbox("Método de pago", ["Todos", "Efectivo", "Nequi", "DaviPlata", "Falabella"])
    fecha_inicio = st.date_input("Fecha inicio")
    fecha_fin = st.date_input("Fecha fin")

    if st.button("Generar Reporte"):
        # Preparar los parámetros de la solicitud
        params = {
            "categoria": categoria,
            "metodo": metodo,
            "fecha_inicio": fecha_inicio.strftime("%Y-%m-%d"),
            "fecha_fin": fecha_fin.strftime("%Y-%m-%d")
        }

        # Incluir el token en los headers
        headers = {
            "Authorization": f"Bearer {st.session_state['jwt_token']}"
        }

        # Hacer la solicitud GET para generar el reporte
        response = requests.get(f"{API_BASE_URL}/reportes", params=params, headers=headers)

        if response.status_code == 200:
            # Mostrar el gráfico en la interfaz
            st.image(response.content)
        else:
            st.error("No se pudo generar el reporte")

# Llamar a la función de inicio de sesión
login()

# Lógica para mostrar las opciones del menú
menu = st.sidebar.selectbox("Selecciona una opción", ["Registrar Usuario", "Registrar Ingreso", "Registrar Gasto", "Generar Reporte"])

if menu == "Registrar Usuario":
    registrar_usuario()
elif menu == "Registrar Ingreso":
    registrar_ingreso()
elif menu == "Registrar Gasto":
    registrar_gasto()
elif menu == "Generar Reporte":
    generar_reporte()
