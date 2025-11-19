import streamlit as st

st.title("EcoAprende 🌱")

# -----------------------------------------
#     PROGRESO DE LOS JUEGOS
# -----------------------------------------
progreso = {
    "Solar": {"completado": False, "puntaje": 0},
    "Eolica": {"completado": False, "puntaje": 0},
    "Hidraulica": {"completado": False, "puntaje": 0},
    "Biomasa": {"completado": False, "puntaje": 0}
}

st.subheader("Juegos disponibles")

# Lista de juegos
juegos = ["Solar", "Eolica", "Hidraulica", "Biomasa"]

# Inicializar estado en session_state
for j in juegos:
    if f"mostrar_{j}" not in st.session_state:
        st.session_state[f"mostrar_{j}"] = False

# -----------------------------------------
#     TARJETAS DE CADA JUEGO
# -----------------------------------------
for juego in juegos:
    estado = "✔️" if progreso[juego]["completado"] else ""
    if st.button(f"{juego} {estado}"):
        st.session_state[f"mostrar_{juego}"] = not st.session_state.get(f"mostrar_{juego}", False)

    if st.session_state.get(f"mostrar_{juego}", False):
        st.header(f"🎮 Juego: Energía {juego}")
        st.write("Responde las preguntas:")

        # PREGUNTAS DE CADA JUEGO
        if juego == "Solar":
            p1 = st.radio(
                "¿Qué energía solar genera electricidad?",
                ["Solar Térmica", "Solar Fotovoltaica", "Solar Geotérmica"],
                key=f"{juego}_p1")

            p2 = st.radio(
                "¿Cuál es el principal beneficio ambiental?",
                ["Genera pocos residuos", "Reduce CO2", "Funciona de noche"],
                key=f"{juego}_p2")

            respuestas_correctas = {
                "p1": "Solar Fotovoltaica",
                "p2": "Reduce CO2"
            }

        elif juego == "Eolica":
            p1 = st.radio(
                "¿Qué dispositivo convierte el viento en energía?",
                ["Turbina eólica", "Motor de vapor", "Panel solar"],
                key=f"{juego}_p1")

            p2 = st.radio(
                "¿Dónde funcionan mejor los aerogeneradores?",
                ["En zonas con mucho viento", "En bosques", "En ciudades"],
                key=f"{juego}_p2")

            respuestas_correctas = {
                "p1": "Turbina eólica",
                "p2": "En zonas con mucho viento"
            }

        elif juego == "Hidraulica":
            p1 = st.radio(
                "¿Qué se utiliza para generar energía hidráulica?",
                ["El viento", "La fuerza del agua", "La luz solar"],
                key=f"{juego}_p1")

            p2 = st.radio(
                "Una ventaja de la energía hidráulica es:",
                ["No usa agua", "Es renovable", "Depende del petróleo"],
                key=f"{juego}_p2")

            respuestas_correctas = {
                "p1": "La fuerza del agua",
                "p2": "Es renovable"
            }

        elif juego == "Biomasa":
            p1 = st.radio(
                "¿Qué es la biomasa?",
                ["Material orgánico", "Energía del viento", "Gas natural"],
                key=f"{juego}_p1")

            p2 = st.radio(
                "¿Qué se puede obtener de la biomasa?",
                ["Biogás", "Luz solar", "Minerales"],
                key=f"{juego}_p2")

            respuestas_correctas = {
                "p1": "Material orgánico",
                "p2": "Biogás"
            }

        # Botón enviar
        if st.button(f"Enviar respuestas {juego}"):
            puntaje = 0

            if locals()['p1'] == respuestas_correctas["p1"]:
                puntaje += 5
            if locals()['p2'] == respuestas_correctas["p2"]:
                puntaje += 5

            progreso[juego]["completado"] = True
            progreso[juego]["puntaje"] = puntaje

            st.success(f"¡Completado {juego}! Puntaje: {puntaje} ⭐")
            st.balloons()


