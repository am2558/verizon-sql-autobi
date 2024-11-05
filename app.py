from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Set up the Google Gemini API key
genai.configure(api_key="AIzaSyBMfK_Vj4acUcMAglRdtZ3OmrKr82dLzts")

@app.route('/generate-sql', methods=['POST'])
def generate_sql():
    data = request.get_json()
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    # Interact with the Gemini model
    try:
        response = genai.generate_text(
            model="YOUR_GEMINI_MODEL_NAME",
            prompt=user_query,
            max_output_tokens=150  # Adjust as needed for your SQL query length
        )
        sql_query = response.result if response.result else "No query generated."
        return jsonify({"sql_query": sql_query})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
