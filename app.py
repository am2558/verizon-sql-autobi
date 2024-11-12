import os
import pandas as pd
from flask import Flask, request, jsonify, send_file
import google.generativeai as genai

app = Flask(__name__)

# Configure the Gemini API with your API key from the environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def parse_csv(file):
    # Load CSV and extract schema
    df = pd.read_csv(file)
    schema = {
        "columns": df.columns.tolist(),
        "types": df.dtypes.astype(str).tolist()
    }
    return schema

def generate_sql_prompt(schema, query):
    # Craft prompt for LLM based on schema and user query
    columns = ", ".join([f"{name} ({dtype})" for name, dtype in zip(schema["columns"], schema["types"])])
    prompt = (
        f"Given a table with columns: {columns}, generate an SQL query for the following request:\n"
        f"{query}\n"
    )
    return prompt

@app.route('/')
def index():
    # Serve the index.html file at the root
    return send_file('index.html')

@app.route('/generate-sql', methods=['POST'])
def generate_sql():
    if 'csvFile' not in request.files:
        return jsonify({"error": "No CSV file uploaded"}), 400

    csv_file = request.files['csvFile']
    query = request.form.get('query', '')

    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Parse CSV to extract schema
    schema = parse_csv(csv_file)

    # Generate prompt and call LLM
    prompt = generate_sql_prompt(schema, query)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    # Extract the generated text from the response
    sql_query = response.text if response and hasattr(response, 'text') else "Could not generate SQL query."

    return jsonify({"sql_query": sql_query})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
