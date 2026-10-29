import streamlit as st
import pandas as pd

st.set_page_config(page_title="Energías renovables y desarrollo sustentable", page_icon="🌱", layout="wide")

st.markdown("""
<style>
.stApp {background: #f5f8f5;}
.hero {padding: 2rem; border-radius: 18px; background: linear-gradient(115deg,#123b32,#237b58); color:white;}
.hero h1 {color:white;}
.hero p {color:#e6f4eb;font-size:1.08rem;}
div[data-testid="stMetric"] {background:white;padding:1rem;border-radius:12px;border:1px solid #dce9df;}
</style>
""", unsafe_allow_html=True)

secciones = ["Inicio", "Conceptos básicos", "Tipos de energías", "Economía y sustentabilidad",
             "Argentina: oportunidades y desafíos", "Simulador económico", "Actividades y evaluación",
             "Proyecto integrador"]
with st.sidebar:
    st.title("🌱 Energía sustentable")
    st.caption("Economía · 5.º año · Nivel secundario")
    pagina = st.radio("Navegación", secciones)
    st.divider()
    st.markdown("**Pregunta guía**")
    st.info("¿Cómo producir energía y crecer económicamente sin comprometer los recursos de las próximas generaciones?")

if pagina == "Inicio":
    st.markdown('<div class="hero"><h1>Energías renovables y desarrollo sustentable</h1><p>La energía como recurso estratégico para la economía, la sociedad y el ambiente.</p><b>ECONOMÍA · 5.º AÑO</b></div>', unsafe_allow_html=True)
    st.subheader("Bienvenidos")
    st.write("La energía es indispensable para producir bienes y servicios, transportarnos, comunicarnos y desarrollar nuestra vida cotidiana. Las formas tradicionales de producirla pueden generar contaminación y contribuir al cambio climático. Las energías renovables ofrecen alternativas que aprovechan recursos naturales que se regeneran, como el sol, el viento y el agua.")
    a,b,c = st.columns(3)
    a.info("☀️ **Ambiente**\n\nReducir impactos y cuidar los recursos naturales.")
    b.info("📈 **Economía**\n\nAnalizar costos, inversiones, productividad y empleo.")
    c.info("🤝 **Sociedad**\n\nPromover el acceso a la energía y una transición justa.")
    st.subheader("Objetivos de aprendizaje")
    st.markdown("- Reconocer fuentes de energía renovable y no renovable.\n- Relacionar energía, producción y desarrollo económico.\n- Analizar costos, beneficios, externalidades e inversiones.\n- Identificar oportunidades y desafíos de Argentina.\n- Elaborar propuestas sustentables para la comunidad.")
    st.success("El desarrollo sustentable busca satisfacer las necesidades actuales sin comprometer las posibilidades de las generaciones futuras.")

elif pagina == "Conceptos básicos":
    st.title("¿Qué son las energías renovables?")
    st.write("Son fuentes de energía que provienen de recursos naturales capaces de renovarse continuamente o en períodos relativamente cortos.")
    st.subheader("Comparación de fuentes")
    st.dataframe(pd.DataFrame({"Renovables":["Solar","Eólica","Hidráulica","Biomasa","Geotérmica"],"No renovables":["Petróleo","Gas natural","Carbón","Uranio (nuclear)","—"]}), hide_index=True, use_container_width=True)
    st.subheader("¿Por qué son importantes?")
    st.markdown("**Diversificación energética:** reducen la dependencia de una sola fuente.\n\n**Inversión productiva:** requieren capital, infraestructura y tecnología.\n\n**Empleo:** generan puestos de trabajo en construcción, instalación y mantenimiento.\n\n**Competitividad:** pueden ofrecer costos operativos convenientes a largo plazo.\n\n**Externalidades:** una menor contaminación puede reducir costos sociales y ambientales.")
    st.warning("Una externalidad ocurre cuando una actividad económica genera costos o beneficios sobre terceros que no quedan completamente reflejados en el precio.")

elif pagina == "Tipos de energías":
    st.title("Tipos de energías renovables")
    datos = {
      "☀️ Solar":("Transforma la radiación solar en electricidad mediante paneles fotovoltaicos o en calor mediante sistemas térmicos.","Viviendas, escuelas, industrias y parques solares.","Depende de la radiación solar y requiere inversión en equipos y, en ciertos casos, almacenamiento."),
      "🌬️ Eólica":("Utiliza la fuerza del viento para mover aerogeneradores que producen electricidad.","Parques eólicos y sistemas de pequeña escala.","Necesita zonas con vientos adecuados, conexión a la red e inversión."),
      "💧 Hidráulica":("Aprovecha el movimiento o la caída del agua para generar electricidad.","Centrales hidroeléctricas.","Las obras pueden modificar ecosistemas y usos del territorio."),
      "🌿 Biomasa":("Obtiene energía a partir de materia orgánica y residuos agrícolas, forestales o urbanos.","Biogás, calor y electricidad.","Requiere gestión responsable para evitar competir con alimentos o degradar suelos."),
      "🌋 Geotérmica":("Aprovecha el calor interno de la Tierra.","Calefacción y centrales geotérmicas.","Depende de las características geológicas y de los costos de exploración.")
    }
    elegida = st.selectbox("Seleccioná una fuente", list(datos))
    descripcion, usos, desafio = datos[elegida]
    st.subheader(elegida); st.write(descripcion); st.markdown(f"**Aplicaciones:** {usos}"); st.markdown(f"**Desafío:** {desafio}")
    st.divider()
    st.dataframe(pd.DataFrame([["Solar","Sol","Paneles y almacenamiento"],["Eólica","Viento","Aerogeneradores y redes"],["Hidráulica","Agua en movimiento","Obras e infraestructura"],["Biomasa","Materia orgánica","Recolección y procesamiento"],["Geotérmica","Calor terrestre","Exploración especializada"]],columns=["Fuente","Recurso","Infraestructura"]), hide_index=True, use_container_width=True)

elif pagina == "Economía y sustentabilidad":
    st.title("Economía y sustentabilidad")
    st.write("La transición energética transforma la producción, el empleo, las inversiones y las decisiones del Estado.")
    conceptos = {
      "Inversión":"Destinar recursos hoy para obtener beneficios futuros, por ejemplo instalar paneles solares.",
      "Costo de oportunidad":"Valor de la mejor alternativa a la que se renuncia al elegir un proyecto.",
      "Externalidad positiva":"Beneficio para terceros, como una mejora en la calidad del aire.",
      "Externalidad negativa":"Costo impuesto a terceros, como determinados daños ambientales.",
      "Empleo verde":"Trabajo que contribuye a preservar o restaurar el ambiente o mejorar el uso de recursos.",
      "Desarrollo sustentable":"Integra las dimensiones económica, social y ambiental."
    }
    for titulo, texto in conceptos.items():
        with st.expander(titulo): st.write(texto)
    st.subheader("Para debatir")
    st.write("¿Alcanza con que una energía sea renovable? También hay que evaluar dónde se instala la infraestructura, cómo se financia, qué impactos produce, quiénes reciben los beneficios y si las comunidades participan.")
    st.warning("Una transición energética justa debe considerar el acceso, el precio de la energía, el empleo y la distribución de costos y beneficios.")

elif pagina == "Argentina: oportunidades y desafíos":
    st.title("Argentina: oportunidades y desafíos")
    st.write("Argentina cuenta con recursos naturales diversos: vientos intensos en la Patagonia, radiación solar elevada en el NOA y Cuyo, recursos hídricos y biomasa vinculada a actividades agropecuarias y forestales.")
    col1,col2=st.columns(2)
    with col1:
        st.subheader("Oportunidades")
        st.markdown("- Inversiones en parques solares y eólicos.\n- Empleo técnico y profesional.\n- Desarrollo de proveedores nacionales.\n- Diversificación de la matriz energética.\n- Actividad económica en distintas provincias.")
    with col2:
        st.subheader("Desafíos")
        st.markdown("- Financiar inversiones de largo plazo.\n- Modernizar redes de transporte y distribución.\n- Incorporar almacenamiento.\n- Asegurar reglas claras y continuidad de políticas.\n- Evaluar impactos sociales y ambientales.")
    respuesta=st.text_area("¿Qué ventajas económicas podría obtener una provincia si desarrolla un parque solar o eólico?")
    if st.button("Ver orientación"): st.info("Considerá inversión, empleo directo e indirecto, proveedores, infraestructura, ingresos locales, diversificación energética y también los costos ambientales y económicos.")

elif pagina == "Simulador económico":
    st.title("Simulador: inversión en energía solar")
    st.write("Ejemplo simplificado con valores hipotéticos para aprender a analizar una inversión. No representa una cotización ni una evaluación técnica real.")
    c1,c2=st.columns(2)
    with c1:
        inversion=st.number_input("Inversión inicial ($)",min_value=0,value=12000000,step=500000)
        ahorro=st.number_input("Ahorro estimado por mes ($)",min_value=0,value=350000,step=25000)
    with c2:
        mantenimiento=st.number_input("Mantenimiento anual ($)",min_value=0,value=300000,step=25000)
        anios=st.slider("Período de análisis (años)",1,25,10)
    ahorro_anual=ahorro*12
    beneficio=ahorro_anual-mantenimiento
    saldo=beneficio*anios-inversion
    recuperacion=inversion/beneficio if beneficio>0 else None
    x,y,z=st.columns(3)
    x.metric("Ahorro anual",f"$ {ahorro_anual:,.0f}")
    y.metric("Beneficio anual neto",f"$ {beneficio:,.0f}")
    z.metric("Saldo acumulado",f"$ {saldo:,.0f}")
    if recuperacion is not None: st.write(f"**Plazo simple estimado de recuperación:** {recuperacion:.1f} años.")
    else: st.write("Con estos datos no se obtiene un beneficio anual neto positivo.")
    st.caption("No contempla inflación, financiamiento, impuestos, variación de tarifas, degradación de equipos, valor residual ni tasa de descuento.")
    if saldo>0: st.success("En este escenario, los ahorros netos acumulados superan la inversión inicial.")
    elif saldo<0: st.warning("En este escenario, los ahorros netos acumulados todavía no cubren la inversión inicial.")
    else: st.info("En este escenario, los ahorros netos acumulados igualan la inversión inicial.")
    st.write("**Para pensar:** ¿qué cambiaría si aumenta el costo de la energía convencional o si la inversión se financia con un crédito?")

elif pagina == "Actividades y evaluación":
    st.title("Actividades y evaluación")
    preguntas=[
      ("¿Cuál es una fuente renovable?",["Petróleo","Carbón","Energía solar","Gas natural"],"Energía solar","Aprovecha la radiación del Sol."),
      ("¿Qué concepto describe un beneficio social por menor contaminación?",["Externalidad positiva","Costo fijo","Déficit fiscal","Costo de oportunidad"],"Externalidad positiva","La mejora ambiental beneficia también a terceros."),
      ("¿Qué representa invertir en un parque eólico?",["Un gasto sin finalidad","Recursos aplicados para beneficios futuros","Un impuesto","Una transferencia"],"Recursos aplicados para beneficios futuros","La inversión crea capital e infraestructura."),
      ("¿Cuál es un desafío de la transición energética?",["Eliminar infraestructura","Evitar inversiones","Modernizar redes y desarrollar almacenamiento","Garantizar viento constante"],"Modernizar redes y desarrollar almacenamiento","Las fuentes variables requieren planificación."),
      ("¿Qué dimensiones integra el desarrollo sustentable?",["Solo económica","Solo ambiental","Económica, social y ambiental","Solo tecnológica"],"Económica, social y ambiental","La sustentabilidad integra las tres dimensiones.")
    ]
    respuestas=[]
    for i,(q,ops,correcta,explica) in enumerate(preguntas):
        st.markdown(f"**{i+1}. {q}**")
        respuestas.append(st.radio("Elegí una opción",ops,key=f"q{i}",index=None))
    if st.button("Corregir cuestionario",type="primary"):
        aciertos=0
        for i,(_,_,correcta,explica) in enumerate(preguntas):
            if respuestas[i]==correcta: aciertos+=1; st.success(f"Pregunta {i+1}: correcta. {explica}")
            else: st.error(f"Pregunta {i+1}: respuesta correcta: {correcta}. {explica}")
        st.metric("Resultado",f"{aciertos} de {len(preguntas)}",f"{aciertos/len(preguntas)*100:.0f}%")
    st.divider()
    st.subheader("Consignas para debatir")
    st.markdown("1. ¿Por qué una empresa invertiría en energía renovable?\n2. ¿Qué diferencias existen entre crecimiento económico y desarrollo sustentable?\n3. ¿Quién debería financiar la transición energética?\n4. ¿Qué efectos podría tener sobre el empleo de una región?")

elif pagina == "Proyecto integrador":
    st.title("Proyecto integrador: una propuesta energética para mi comunidad")
    st.write("En grupos, diseñen una propuesta para incorporar una solución de energía renovable en la escuela, el barrio o una institución.")
    etapas=[("1. Diagnóstico","Identificar una necesidad energética y describir cómo se resuelve actualmente."),("2. Selección","Elegir una fuente renovable y justificar por qué sería adecuada."),("3. Análisis económico","Estimar inversión, mantenimiento, ahorros y financiamiento."),("4. Impacto social y ambiental","Reconocer beneficios, posibles efectos negativos y personas involucradas."),("5. Comunicación","Preparar una presentación, afiche o informe.")]
    for t,d in etapas:
        with st.expander(t): st.write(d)
    st.subheader("Plantilla de trabajo")
    nombre=st.text_input("Nombre del proyecto")
    problema=st.text_area("¿Qué necesidad busca resolver?")
    fuente=st.selectbox("Fuente elegida",["Solar","Eólica","Hidráulica","Biomasa","Geotérmica","Otra"])
    beneficiarios=st.text_area("¿Quiénes serían los beneficiarios?")
    costos=st.text_area("¿Qué inversiones y costos habría que considerar?")
    impacto=st.text_area("¿Qué beneficios e impactos tendría?")
    if st.button("Generar resumen"):
        if nombre.strip() and problema.strip():
            st.markdown("### Resumen de la propuesta")
            st.write({"Proyecto":nombre,"Problema":problema,"Fuente":fuente,"Beneficiarios":beneficiarios or "A completar","Costos":costos or "A completar","Impacto":impacto or "A completar"})
        else: st.error("Completá al menos el nombre del proyecto y el problema.")
st.divider()
st.caption("Material didáctico · Economía · 5.º año de secundaria | Energías renovables y desarrollo sustentable")
