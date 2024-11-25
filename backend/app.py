import os
import pandas as pd
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyCZHLlq8BlOJa-B5JSU4M8bIEtFjOdoHIg")

def parse_csv(file):
    df = pd.read_csv(file)
    schema = {
        "columns": df.columns.tolist(),
        "types": df.dtypes.astype(str).tolist()
    }
    return schema

def generate_sql_prompt(schema, query):
    columns = ", ".join([f"{name} ({dtype})" for name, dtype in zip(schema["columns"], schema["types"])])
    prompt = (
        f"Given a table with columns: {columns}, generate an SQL query for the following request:\n"
        f"{query}\n"
    )
    return prompt

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

        if response and hasattr(response, 'text'):
            sql_query = response.text
            print(response.text)
        else:
            sql_query = "Could not generate SQL query."

        return jsonify({"sql_query": sql_query})
    
    except Exception as e:
        print(f"Error generating query: {e}")
        return jsonify({"sql_query": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5011)))