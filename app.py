import gradio as gr
from controladores.controlador_meteorologico import WeatherController

controller = WeatherController()

def agregar_estacion(nombre):
    controller.add_station(nombre)
    return f"Estación '{nombre}' agregada."

def agregar_dato(nombre_estacion, dato_clima):
    controller.add_weather_to_station(nombre_estacion, dato_clima)
    return f"Clima agregado a '{nombre_estacion}': {dato_clima}"

def mostrar_datos():
    output = ""
    current = controller.head_station
    while current:
        output += f"📍 Estación {current.name}:\n"
        weather = current.weather_head
        while weather:
            desc = controller.encryptor.decrypt(weather.encrypted_data)
            output += f"  - {desc}\n"
            weather = weather.next
        output += "\n"
        current = current.next_station
    return output or "Sin estaciones aún."

with gr.Blocks() as demo:
    gr.Markdown("### 🌤️ Estaciones Meteorológicas (Encriptadas)")

    with gr.Row():
        nombre_estacion = gr.Textbox(label="Nombre de nueva estación")
        btn_agregar_estacion = gr.Button("Agregar estación")
    estado1 = gr.Textbox(label="Estado", interactive=False)

    with gr.Row():
        estacion_para_clima = gr.Textbox(label="Nombre estación")
        clima = gr.Textbox(label="Clima")
        btn_agregar_clima = gr.Button("Agregar clima")
    estado2 = gr.Textbox(label="Estado", interactive=False)

    btn_mostrar = gr.Button("Mostrar datos desencriptados")
    area_datos = gr.Textbox(label="Datos", lines=15, interactive=False)

    btn_agregar_estacion.click(fn=agregar_estacion, inputs=nombre_estacion, outputs=estado1)
    btn_agregar_clima.click(fn=agregar_dato, inputs=[estacion_para_clima, clima], outputs=estado2)
    btn_mostrar.click(fn=mostrar_datos, outputs=area_datos)

demo.launch()
