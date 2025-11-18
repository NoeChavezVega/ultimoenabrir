import streamlit as st
st.title("EcoAprende 🌱")
progreso = {"Solar": {"completado": False, "puntaje": 0}}
st.subheader("Juegos disponibles")
juego = "Solar"

estado = "✔️" if progreso[juego]["completado"] else ""
if st.button(f"{juego} {estado}"):
    st.session_state["mostrar_solar"] = not st.session_state.get("mostrar_solar", False)
if st.session_state.get("mostrar_solar", False):
    st.header("🌞 Juego: Energía Solar")
    st.write("Responde las preguntas:")
    p1 = st.radio(
        "¿Qué energía solar genera electricidad?",
        ["Solar Térmica", "Solar Fotovoltaica", "Solar Geotérmica"],
        key="p1")
    p2 = st.radio(
        "¿Cuál es el principal beneficio ambiental?",
        ["Genera pocos residuos", "Reduce CO2", "Funciona de noche"],
        key="p2")
    if st.button("Enviar respuestas"):
        puntaje = 0
        if p1 == "Solar Fotovoltaica":
            puntaje += 5
        if p2 == "Reduce CO2":
            puntaje += 5
        progreso["Solar"]["completado"] = True
        progreso["Solar"]["puntaje"] = puntaje
        st.success(f"¡Completado! Puntaje: {puntaje} ⭐")
        st.balloons()


