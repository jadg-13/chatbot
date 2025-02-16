


import openai
import os


from flask import Flask, request, jsonify

app = Flask(__name__)



# Configurar la clave de API de OpenAI
API_KEY = os.getenv("OPENAI_API_KEY")

# Función para obtener respuesta de ChatGPT
def obtener_respuesta(mensaje):
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Eres un chatbot que responde en español."},
                    {"role": "user", "content": mensaje}],
            api_key=API_KEY
        )
        return respuesta["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/chat", methods=["POST"])
def chat():
    datos = request.get_json()
    mensaje = datos.get("mensaje", "")
    if not mensaje:
        return jsonify({"error": "Mensaje vacío"}), 400
    respuesta = obtener_respuesta(mensaje)
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
