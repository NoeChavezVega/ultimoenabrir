import streamlit as st
st.title("🌱 EcoAprende de Energías🔌")
progreso = {
    "Solar": {"completado": False, "puntaje": 0},
    "Eolica": {"completado": False, "puntaje": 0},
    "Hidraulica": {"completado": False, "puntaje": 0},
    "Biomasa": {"completado": False, "puntaje": 0},}
def mostrar_dashboard():
    st.header("Tipos de energías")
    st.subheader("Selecciona una energía:")
    for juego, data in progreso.items():
        nombre_mostrar = f"{juego} {'✔️' if data['completado'] else ''}"
        if st.button(nombre_mostrar, key=f"boton_{juego}"):
            st.session_state["pantalla"] = juego

def mostrar_preguntas(preguntas, juego):
    st.header(f"Juego: {juego}")
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

        st.success(f"Juego completado. Ganaste {puntaje} puntos 🎉")
        st.balloons()

        if juego == "Solar":
            st.markdown("### ☀️ Información sobre la energía solar")
            st.write("""En el estado de Chihuahua, las energías renovables aportan una variedad de beneficios importantes gracias a las características propias del territorio. 
            La energía solar destaca especialmente porque el estado recibe una de las radiaciones solares más altas del país, 
            lo que permite que los paneles generen electricidad de manera muy eficiente. Esto se traduce en ahorros económicos para hogares y empresas, 
            reducción considerable de emisiones de CO₂ y atracción de inversiones para granjas solares que han impulsado el empleo local. Además, 
            ha permitido llevar energía a comunidades rurales que antes no contaban con servicio eléctrico, 
            mejorando su calidad de vida y fortaleciendo la independencia energética del estado..""")

        elif juego == "Eolica":
            st.markdown("### 🌬️ Información sobre la energía eólica")
            st.write("""La energía eólica también ofrece ventajas relevantes, particularmente en regiones donde los vientos son constantes y adecuados para instalar aerogeneradores. El aprovechamiento del viento no solo contribuye a diversificar la matriz energética, sino que también atrae inversión, genera empleos y reduce el impacto ambiental al no depender de combustibles fósiles. 
            En Chihuahua incluso se analiza su potencial para producir hidrógeno verde, 
            lo cual posicionaría al estado como un referente en tecnologías limpias emergentes.""")

        elif juego == "Hidraulica":
            st.markdown("### 💧 Información sobre la energía hidráulica")
            st.write("""En cuanto a la energía hidráulica, especialmente en su modalidad de mini-hidroeléctricas, 
            permite aprovechar el flujo de agua en presas y canales ya existentes sin necesidad de construir grandes represas.
            Esto brinda una fuente de energía constante y confiable con un impacto ambiental reducido.
            Además, contribuye a fortalecer las comunidades cercanas mediante empleo, 
            infraestructura y la oportunidad de generar electricidad de manera más local y sostenible..""")

        elif juego == "Biomasa":
            st.markdown("### 🌿 Información sobre la biomasa")
            st.write("""Finalmente, la energía de biomasa tiene un papel relevante en zonas forestales y ganaderas del estado. Chihuahua cuenta con abundantes residuos de aserraderos, 
            madera y actividad forestal que pueden transformarse en energía en lugar de desperdiciarse o aumentar el riesgo de incendios. 
            También existe potencial para producir biogás a partir de residuos ganaderos, lo que permite capturar metano —un gas de efecto invernadero— y convertirlo en electricidad o calor útil. 
            Este aprovechamiento de residuos genera beneficios económicos para comunidades rurales, 
            fomenta la autosuficiencia energética y reduce la contaminación, impulsando a la vez empleos verdes y nuevos modelos de economía circular..""")

        st.info("Pícale de nuevo a enviar si quieres volver al menú.")
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
     "correcta":"Verdadero"},
    {"pregunta":"¿La temperatura afecta el rendimiento de una celda fotovoltaica?",
     "opciones":["Verdadero","Falso"],
     "correcta":"Falso"},
    {"pregunta":"¿Por qué las celdas solares de silicio tienen mayor eficiencia que las policristalinas?",
     "opciones":["Tienen mayor grosor", 
                 "Poseen una estructura uniforme que reduce la recombinación electrónica",
                 "Reflejan más luz",
                 "Operan a más temperatura"],
     "correcta":"Poseen una estructura uniforme que reduce la recombinación electrónica"},
    {"pregunta":"¿Por qué se considera una energía renovable?",
     "opciones":["porque es económica","tiene un menor impacto ambiental","su tecnología es de mejor calidad","puede usarse en diferentes ámbitos"],
     "correcta":"tiene un menor impacto ambiental"},
    {"pregunta":"¿Qué factor aumenta la eficiencia de un panel solar?",
     "opciones":["Acumulación de polvo","Alta temperatura","Buena orientación al Sol","Sombra parcial"],
     "correcta":"Buena orientación al Sol"},
    {"pregunta":"¿Cuál es una desventaja de la energía solar?",
     "opciones":["Produce gases","Depende de la radiación solar","Emite ruido","Usa combustibles"],
     "correcta":"Depende de la radiación solar"},]

preguntas_eolica = [
    {"pregunta":"¿Qué energía aprovechan los aerogeneradores?",
     "opciones":["Solar","Viento","Hidráulica","Geotérmica"],
     "correcta":"Viento"},
    {"pregunta":"¿Qué parte recibe la fuerza del viento?",
     "opciones":["Torre","Palas","Generador","Anemómetro"],
     "correcta":"Palas"},
    {"pregunta":"¿Qué mide un anemómetro?",
     "opciones":["Presión","Temperatura","Velocidad del viento","Humedad"],
     "correcta":"Velocidad del viento"},
    {"pregunta":"¿Cuál es un beneficio de la energía eólica?",
     "opciones":["Gases tóxicos","Usa combustibles","Es renovable","Consume mucha agua"],
     "correcta":"Es renovable"},
    {"pregunta":"¿Cómo se genera electricidad en un aerogenerador?",
     "opciones":["Combustión","Vibración","Rotación de un eje","Reacciones químicas"],
     "correcta":"Rotación de un eje"},
    {"pregunta":"¿Cuál es una desventaja?",
     "opciones":["Requiere petróleo","Depende del viento","Produce CO₂","Solo funciona de noche"],
     "correcta":"Depende del viento"},
    {"pregunta":"¿Qué hace el generador?",
     "opciones":["Controla palas","Convierte energía mecánica en eléctrica","Mide viento","Detiene sistema"],
     "correcta":"Convierte energía mecánica en eléctrica"},
    {"pregunta":"¿Qué energía tiene el viento antes de mover palas?",
     "opciones":["Química","Térmica","Cinética","Sonora"],
     "correcta":"Cinética"},
    {"pregunta":"¿Cómo se orientan al viento?",
     "opciones":["Manual","Sensores con sistema automático","Brújula","Por gravedad"],
     "correcta":"Sensores con sistema automático"},
    {"pregunta":"¿Qué países tienen mayor potencial eólico?",
     "opciones":["Sin costas","Con viento constante","Desérticos","Muy húmedos"],
     "correcta":"Con viento constante"},]

preguntas_hidraulica = [
    {"pregunta":"¿Qué energía aprovechan las hidroeléctricas?",
     "opciones":["Térmica","Movimiento del agua","Solar","Química"],
     "correcta":"Movimiento del agua"},
    {"pregunta":"¿Qué estructura almacena agua?",
     "opciones":["Pozo","Tubería","Embalse","Sifón"],
     "correcta":"Embalse"},
    {"pregunta":"¿Qué convierte energía del agua en mecánica?",
     "opciones":["Transformador","Turbina","Motor","Condensador"],
     "correcta":"Turbina"},
    {"pregunta":"¿Qué se genera al girar el generador?",
     "opciones":["Calor","Sonido","Electricidad","Aire"],
     "correcta":"Electricidad"},
    {"pregunta":"Beneficio de la hidráulica:",
     "opciones":["Produce gases","Es renovable","Requiere petróleo","No almacena energía"],
     "correcta":"Es renovable"},
    {"pregunta":"Desventaja:",
     "opciones":["Residuos tóxicos","Depende del caudal","Requiere combustible","No renovable"],
     "correcta":"Depende del caudal"},
    {"pregunta":"Nombre de la caída de agua:",
     "opciones":["Captación","Precipitación","Salto hidráulico","Evaporación"],
     "correcta":"Salto hidráulico"},
    {"pregunta":"Energía antes de mover turbina:",
     "opciones":["Sonora","Química","Potencial y cinética","Térmica"],
     "correcta":"Potencial y cinética"},
    {"pregunta":"Controla el flujo de agua:",
     "opciones":["Alternador","Compuerta","Transformador","Generador"],
     "correcta":"Compuerta"},
    {"pregunta":"¿Dónde se instalan?",
     "opciones":["Sin agua","Montañas sin ríos","Ríos o presas","Desiertos"],
     "correcta":"Ríos o presas"},]

preguntas_biomasa = [
    {"pregunta":"¿Qué es la biomasa?",
     "opciones":["Energía solar","Materia orgánica como energía","Energía eólica","Rocas energéticas"],
     "correcta":"Materia orgánica como energía"},
    {"pregunta":"Ejemplo de biomasa:",
     "opciones":["Carbón","Aceite vegetal usado","Gas natural","Arena"],
     "correcta":"Aceite vegetal usado"},
    {"pregunta":"¿Qué energía se obtiene al quemarla?",
     "opciones":["Eléctrica","Térmica","Nuclear","Eólica"],
     "correcta":"Térmica"},
    {"pregunta":"¿Cuál es una ventaja del uso de biomasa?:",
     "opciones":["CO₂ fósil alto","Es renovable","Se agota rápido","Requiere petróleo"],
     "correcta":"Es renovable"},
    {"pregunta":"Gas producido en digestión anaerobia:",
     "opciones":["Nitrógeno","Oxígeno","Metano","Ozono"],
     "correcta":"Metano"},
    {"pregunta":"¿Cuál de los siguientes recursos NO es biomasa?",
     "opciones":["Residuos agrícolas","Madera","Restos de comida","Hierro mineral"],
     "correcta":"Hierro mineral"},
    {"pregunta":"¿Qué proceso convierte residuos orgánicos húmedos en biogás?",
     "opciones":["Evaporación","Digestión anaerobia","Destilación","Pirólisis"],
     "correcta":"Digestión anaerobia"},
    {"pregunta":"¿Qué combustible se obtiene de algunos cultivos como el maíz o la caña de azúcar?",
     "opciones":["Diesel fósil","Etanol","Propano","Gasolina"],
     "correcta":"Etanol"},
    {"pregunta":"¿Qué tipo de energía tiene la biomasa abans de ser procesada?",
     "opciones":["química almacenada","sonora","lumínica","cinética"],
     "correcta":"química almacenada"},
    {"pregunta":"¿Qué impacto ambiental puede tener el uso excesivo de biomasa?",
     "opciones":["Desaparición del viento","Deforestación","Aumento del gas ozono","Contaminación radiactiva"],
     "correcta":"Deforestación"},
    {"pregunta":"¿Qué dispositivo se utiliza para producir biogás?",
     "opciones":["Caldera","Aerogenerador","Biodigestor","Transformador"],
     "correcta":"Biodigestor"},]


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

