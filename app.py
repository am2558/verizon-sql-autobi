from flask import Flask, request, jsonify, render_template_string
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="YOUR_GOOGLE_GEMINI_API_KEY")


@app.route('/')
def home():
    return render_template_string("<h1>Welcome to the SQL Query Generator</h1>")

@app.route('/generate-sql', methods=['POST'])
def generate_sql():
    data = request.get_json()
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        response = genai.generate_text(
            model="YOUR_GEMINI_MODEL_NAME",
            prompt=user_query,
            max_output_tokens=150
        )
        sql_query = response.result if response.result else "No query generated."
        return jsonify({"sql_query": sql_query})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
