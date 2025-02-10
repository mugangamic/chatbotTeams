from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/messages', methods=['POST'])
def receive_data():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "Campo 'text' é obrigatório!"}), 400

    # Simula uma resposta do bot para o Teams
    response = {
        "type": "message",
        "text": f"Você disse: {data['text']}"
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
