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

## 🛠️ **Instalación y Configuración**  

### 🔹 **Requisitos Previos**    
- Python 3  
- SQLite3  
- `psutil` y `requests` (se instalan en el siguiente paso)  

### 🔹 **Instalar dependencias**  
Ejecuta (en un entorno virtual):  
```bash
pip install psutil requests fastapi uvicorn sqlite3
```
---

## 🛠️**Configuración del Bot**
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

### 1️⃣ Prueba /status
![Prueba /status](https://drive.google.com/uc?export=view&id=1qB0wYMzfTKUKbxWoKhOnEKnrRNneoXk3)

### 2️⃣ Alerta recibida en Telegram  
![Alerta de Telegram](https://drive.google.com/uc?export=view&id=1xvsPH_5yL0z1iBTCYROGgHMbHz7C5e2K)  

### 3 Prueba si no funcionan las métricas 
![No funcionamiento](https://drive.google.com/uc?export=view&id=1vbuw8i6DIjN5cM7aPBgzE8cld5QF_qIa)  

## 🚀 Conclusión  

Este proyecto implementa un sistema de monitoreo y alertas para servidores Linux utilizando **Python, FastAPI, SQLite y Telegram**. Se desarrolló un bot de Telegram que permite consultar el estado de los servidores y un servicio de notificaciones para alertar cuando los recursos superen el **75% de uso**.  

Espero que esta solución cumpla con los requerimientos y demuestre mis habilidades en desarrollo y administración de servidores. Agradezco la oportunidad de participar en esta prueba técnica y estoy entusiasmado por la posibilidad de formar parte de su equipo.  

---

## 📩 Contacto  

Si tienen alguna duda o comentario, pueden contactarme a través de mi correo electrónico:  

✉️ **[ingsofiabonilla@gmail.com](ingsofiabonilla@gmail.com)**  

📌 ¡Gracias por su tiempo y consideración! Espero su respuesta. 🚀  

