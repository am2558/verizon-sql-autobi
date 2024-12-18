import os
import pandas as pd
from flask import Flask, request, jsonify, send_file
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyBMfK_Vj4acUcMAglRdtZ3OmrKr82dLzts")

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
    return send_file('index.html')

@app.route('/generate-sql', methods=['POST'])
def generate_sql():
    try:
        if 'csvFile' not in request.files:
            return jsonify({"error": "No CSV file uploaded"}), 400

        csv_file = request.files['csvFile']
        query = request.form.get('query', '')

        if not query:
            return jsonify({"error": "No query provided"}), 400
        
        schema = parse_csv(csv_file)

        prompt = generate_sql_prompt(schema, query)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        # Check response from the API
        if response and hasattr(response, 'text'):
            sql_query = response.text
        else:
            sql_query = "Could not generate SQL query."

        return jsonify({"sql_query": sql_query})
    
    except Exception as e:
        print(f"Error generating query: {e}")
        return jsonify({"sql_query": f"Error generating query: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
