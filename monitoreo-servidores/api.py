from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Función para obtener las últimas métricas de la base de datos
def get_last_metrics():
    conn = sqlite3.connect("monitoring.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM metrics ORDER BY timestamp DESC LIMIT 10")
    data = cursor.fetchall()
    conn.close()
    return data

# Ruta que expone las métricas a través de una API GET
@app.get("/metrics")
def read_metrics():
    return {"data": get_last_metrics()}
