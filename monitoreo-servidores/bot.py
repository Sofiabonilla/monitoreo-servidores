from telegram import Update
from telegram.ext import Application, CommandHandler
import requests

TOKEN = "7856544682:AAGgnhcoMf-GS-EalmHIsvAKz8jO8JjjWrg"

def get_metrics():
    try:
        response = requests.get("http://localhost:8000/metrics")
        response.raise_for_status()  # Levanta un error si el código de respuesta no es 2xx
        return response.json()["data"]
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener métricas: {e}")
        return []

async def status(update: Update, context):
    metrics = get_metrics()
    if not metrics:
        await update.message.reply_text("No se pudo obtener las métricas.")
        return

    message = "\n".join([f"Host: {m[1]}, CPU: {m[3]}%, RAM: {m[4]}%, Disk: {m[5]}%" for m in metrics])
    await update.message.reply_text(message)

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("status", status))
    
    application.run_polling()

if __name__ == '__main__':
    main()

