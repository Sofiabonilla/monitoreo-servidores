import paramiko
import sqlite3
import psutil
import socket
import requests

# Configuración
SERVIDORES = [("10.0.2.15", "sofiabonilla", "bruno")]
TELEGRAM_BOT_TOKEN = "7856544682:AAGgnhcoMf-GS-EalmHIsvAKz8jO8JjjWrg"
TELEGRAM_CHAT_ID = "-4631008134"

def get_local_metrics():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    return hostname, ip_address, cpu_usage, mem_usage, disk_usage

def get_remote_metrics(ip, user, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=user, password=password)
    stdin, stdout, stderr = ssh.exec_command("""
        hostname &&
        ip -4 a | grep inet | awk '{print $2}' | head -n 1 &&
        top -bn1 | grep 'Cpu(s)' | awk '{print $2}' &&
        free -m | awk 'NR==2{print $3/$2 * 100.0}' &&
        df -h / | awk 'NR==2{print $5}'
    """)
    output = stdout.read().decode().split("\n")
    ssh.close()

    # Reemplazar comas por puntos antes de convertir a float
    cpu = float(output[2].replace(',', '.'))  # Reemplazamos coma por punto
    mem = float(output[3].replace(',', '.'))  # Reemplazamos coma por punto
    disk = float(output[4].strip('%').replace(',', '.'))  # Reemplazamos coma por punto

    return output[0], output[1], cpu, mem, disk


def save_to_db(hostname, ip, cpu, mem, disk):
    conn = sqlite3.connect("monitoring.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO metrics (hostname, ip, cpu, memory, disk) VALUES (?, ?, ?, ?, ?)",
                   (hostname, ip, cpu, mem, disk))
    conn.commit()
    conn.close()

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)

# Monitoreo local y remoto
for ip, user, password in SERVIDORES:
    hostname, ip, cpu, mem, disk = get_remote_metrics(ip, user, password)
    save_to_db(hostname, ip, cpu, mem, disk)

hostname, ip, cpu, mem, disk = get_local_metrics()
save_to_db(hostname, ip, cpu, mem, disk)

# Enviar alerta si alguno de los recursos supera el umbral
if cpu > 75 or mem > 75 or disk > 75:
    alert_msg = f"‼️ ALERTA en {hostname} ({ip})\nCPU: {cpu}%\nRAM: {mem}%\nDisco: {disk}%"
    send_telegram_alert(alert_msg)
