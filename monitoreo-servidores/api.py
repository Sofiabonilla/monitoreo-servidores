from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Función para obtener las últimas métricas de la base de datos
def get_last_metrics(limit=10):
    conn = sqlite3.connect("monitoring.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM metrics ORDER BY timestamp DESC LIMIT ?", (limit,))
    data = cursor.fetchall()
    conn.close()
    return data

# Función para obtener el estado actual
def get_status():
    conn = sqlite3.connect("monitoring.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM metrics WHERE type='status' ORDER BY timestamp DESC LIMIT 1")
    status = cursor.fetchone()
    conn.close()
    if status:
        return {"status": status[1], "timestamp": status[2]}  # Asumiendo que el estado está en la columna 1 y el timestamp en la 2
    else:
        return {"status": "No disponible", "timestamp": None}

# Ruta que expone las métricas a través de una API GET
@app.get("/metrics")
def read_metrics(limit: int = 10):
    return {"data": get_last_metrics(limit)}

# Ruta para obtener el estado actual
@app.get("/status")
def read_status():
    return get_status()

# Ruta para obtener el historial completo de métricas
@app.get("/history")
def read_history():
    return {"data": get_last_metrics(limit=None)}  # Obtén todo el historial

