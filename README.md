# 📊 Monitoreo y Alertas para Servidores Linux  
#Sofia Luisa Carolina Bonilla Beltran
En esta prueba tecnica se implementa un sistema de monitoreo para servidores Linux que mide el uso de **CPU, RAM y Disco**, enviando alertas a Telegram cuando los valores superan el 75%. Además, proporciona una API para consultar estadísticas y un bot de Telegram para gestionar las alertas.  

---

## 🚀 **Características del Proyecto**  

✅ Monitoreo automático cada 5 minutos.  
✅ Alertas a Telegram cuando los recursos superan el 75%.  
✅ Base de datos SQLite para almacenar métricas.  
✅ Bot de Telegram para consultar el estado del servidor.  
✅ API REST para acceder a las métricas.  

---

## 🛠️ **1. Instalación y Configuración**  

### 🔹 **Requisitos Previos**    
- Python 3  
- SQLite3  
- `psutil` y `requests` (se instalan en el siguiente paso)  

### 🔹 **Instalar dependencias**  
Ejecuta (en un entorno virtual):  
```bash
pip install psutil requests fastapi uvicorn sqlite3

---

### 🛠️**Configuración del Bot**
TELEGRAM_BOT_TOKEN = "7856544682:AAGgnhcoMf-GS-EalmHIsvAKz8jO8JjjWrg"
TELEGRAM_CHAT_ID = "ID_DEL_GRUPO"

---

## 🛠️**Ejecución del programa**
Iniciar la API: uvicorn api:app --host 0.0.0.0 --port 8000
Inicial el bot: python3 bot.py
**En el bot**
/status : para ver el estado actual del servidor
/history : para consultar las alertas enviadas.

---

## 📸 **Resultados**


