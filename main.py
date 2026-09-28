# import pickle
# import os
# import sqlite3
# from flask import Flask, request, render_template_string

# app = Flask(__name__)

# # Vulnerable: Hardcoded credentials
# DB_USER = "admin"
# DB_PASSWORD = "admin123"

# @app.route('/search')
# def search():
#     # Vulnerable: SQL Injection
#     query = request.args.get('query')
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#     sql = f"SELECT * FROM users WHERE username = '{query}'"
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     return str(results)

# @app.route('/upload', methods=['POST'])
# def upload():
#     # Vulnerable: Arbitrary file upload without validation
#     file = request.files['file']
#     filename = request.form.get('filename')
#     # Vulnerable: Path traversal
#     filepath = os.path.join('/uploads/', filename)
#     file.save(filepath)
#     return f"File saved to {filepath}"

# @app.route('/deserialize', methods=['POST'])
# def deserialize():
#     # Vulnerable: Insecure deserialization
#     data = request.data
#     obj = pickle.loads(data)
#     return f"Deserialized: {obj}"

# @app.route('/template')
# def template():
#     # Vulnerable: Server-Side Template Injection (SSTI)
#     name = request.args.get('name', 'Guest')
#     template = f"<h1>Hello {name}!</h1>"
#     return render_template_string(template)

# @app.route('/exec')
# def execute():
#     # Vulnerable: Command Injection
#     cmd = request.args.get('cmd')
#     result = os.system(cmd)
#     return f"Command executed: {result}"

# @app.route('/eval')
# def evaluate():
#     # Vulnerable: Code Injection via eval
#     code = request.args.get('code')
#     result = eval(code)
#     return f"Result: {result}"

# # Vulnerable: Debug mode enabled in production
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
