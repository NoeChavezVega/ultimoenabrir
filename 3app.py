import streamlit as st
st.title("🌱 EcoAprende de Energías")
progreso = {"Solar": {"completado": False, "puntaje": 0},
    "Eolica": {"completado": False, "puntaje": 0},
    "Hidraulica": {"completado": False, "puntaje": 0},
    "Biomasa": {"completado": False, "puntaje": 0},}

def mostrar_dashboard():
    st.header("Dashboard de Juegos")
    st.subheader("Selecciona un juego:")
    for juego, data in progreso.items():
        nombre_mostrar = f"{juego} {'✔️' if data['completado'] else ''}"
        if st.button(nombre_mostrar, key=f"boton_{juego}"):
            st.session_state["pantalla"] = juego
            
def mostrar_preguntas(preguntas, juego):
    st.header(f"🎮 Juego: {juego}")
    puntaje = 0
    respuestas_usuario = {}
    for i, item in enumerate(preguntas):
        pregunta = item["pregunta"]
        opciones = item["opciones"]
        key_radio = f"{juego}_{i}"
        respuesta_usuario = st.radio(pregunta, opciones, key=key_radio)
        respuestas_usuario[i] = respuesta_usuario
    if st.button("Enviar respuestas", key=f"enviar_{juego}"):
        for i, item in enumerate(preguntas):
            if respuestas_usuario[i] == item["correcta"]:
                puntaje += 1
        progreso[juego]["completado"] = True
        progreso[juego]["puntaje"] = puntaje
        st.success(f"Juego completado. Ganaste {puntaje} puntos.")
        st.balloons()
        st.session_state["pantalla"] = "dashboard"

preguntas_solar = [
    {"pregunta":"¿Qué tipo de tecnología utiliza la energía solar?",
     "opciones":["pirolisis y carbonización","multiplicadora","mecánica","fotovoltaica"],
     "correcta":"fotovoltaica"},
    {"pregunta":"¿Qué hacen los electrones liberados en las placas?",
     "opciones":["se almacenan","generan una corriente alterna","luego de ser captados se dispersan","fluyen a través de la placa"],
     "correcta":"generan una corriente alterna"},
    {"pregunta":"¿La energía termo solar requiere de espejos para funcionar?",
     "opciones":["Verdadero","Falso"],
     "correcta":"Verdadero"},
    {"pregunta":"¿Cuál es el componente principal de los materiales que necesita la energía solar?",
     "opciones":["acero","aluminio","silicio","hierro"],
     "correcta":"silicio"},
    {"pregunta":"¿Cuándo los fotones golpean la placa, liberan electrones?",
     "opciones":["Verdadero","Falso"],
     "correcta":"Verdadero"},]

preguntas_eolica = [{"pregunta":"¿Qué tipo de energía aprovechan los aerogeneradores?",
     "opciones":["Energía solar","Energía del viento","Energía hidráulica","Energía geotérmica"],
     "correcta":"Energía del viento"},
    {"pregunta":"¿Qué parte del aerogenerador recibe directamente la fuerza del viento?",
     "opciones":["Torre","Palas","Generador","Anemómetro"],
     "correcta":"Palas"},
    {"pregunta":"¿Qué mide un anemómetro en un parque eólico?",
     "opciones":["La presión atmosférica","La temperatura","La velocidad del viento","La humedad"],
     "correcta":"La velocidad del viento"},]

preguntas_hidraulica = [
    {"pregunta":"¿Qué tipo de energía aprovechan las plantas hidroeléctricas?",
     "opciones":["Energía térmica","Energía del movimiento del agua","Energía solar","Energía química"],
     "correcta":"Energía del movimiento del agua"},
    {"pregunta":"¿Qué estructura se utiliza para almacenar grandes volúmenes de agua?",
     "opciones":["Pozo","Tubería","Embalse","Sifón"],
     "correcta":"Embalse"},]

preguntas_biomasa = [
    {"pregunta":"¿Qué es la biomasa?",
     "opciones":["Energía del Sol","Materia orgánica utilizada como fuente de energía","Energía del viento","Rocas con minerales energéticos"],
     "correcta":"Materia orgánica utilizada como fuente de energía"},
    {"pregunta":"¿Cuál de los siguientes es un ejemplo de biomasa?",
     "opciones":["Carbón mineral","Aceite vegetal usado","Gas natural","Arena"],
     "correcta":"Aceite vegetal usado"},]

if "pantalla" not in st.session_state:
    st.session_state["pantalla"] = "dashboard"
if st.session_state["pantalla"] == "dashboard":
    mostrar_dashboard()
elif st.session_state["pantalla"] == "Solar":
    mostrar_preguntas(preguntas_solar, "Solar")
elif st.session_state["pantalla"] == "Eolica":
    mostrar_preguntas(preguntas_eolica, "Eolica")
elif st.session_state["pantalla"] == "Hidraulica":
    mostrar_preguntas(preguntas_hidraulica, "Hidraulica")
elif st.session_state["pantalla"] == "Biomasa":
    mostrar_preguntas(preguntas_biomasa, "Biomasa")

