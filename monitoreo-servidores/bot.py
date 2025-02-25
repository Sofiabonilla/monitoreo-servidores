from telegram import Update
from telegram.ext import Application, CommandHandler
import requests
TOKEN = "7856544682:AAGgnhcoMf-GS-EalmHIsvAKz8jO8JjjWrg"

# Función para obtener las métricas desde el servidor FastAPI
def get_metrics():
    response = requests.get("http://localhost:8000/metrics")
    return response.json()["data"]

# Comando /status que muestra las métricas
def status(update: Update, context):
    metrics = get_metrics()
    message = "\n".join([f"Host: {m[1]}, CPU: {m[3]}%, RAM: {m[4]}%, Disk: {m[5]}%" for m in metrics])
    update.message.reply_text(message)

# Función principal para iniciar el bot
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("status", status))  # Comando que llama a la función "status"
    application.run_polling()

if __name__ == '__main__':
    main()
