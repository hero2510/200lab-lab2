from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route("/api")
def index():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="123456",
            database="labdb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hello from MySQL via Flask API'")
        result = cursor.fetchone()
        return jsonify(message=result[0])
    except Exception as e:
        return jsonify(error=str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
