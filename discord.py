import time
from pypresence import Presence

# Aquí debes poner el CLIENT ID de tu aplicación de Discord
CLIENT_ID = '1135978338767355924'

def start_discord_presence():
    try:
        # Inicializar Rich Presence
        rpc = Presence(CLIENT_ID)
        rpc.connect()

        # Configuración de la actividad que aparecerá en Discord
        rpc.update(
            state="Jugando AOForever",
            details="En un juego emocionante: AOForever.org",
            large_image="logo_aoforever",  # Asegúrate de haber subido esta imagen en tu app de Discord
            large_text="AOForever",
            start=time.time()
        )

        print("Rich Presence activado en Discord.")

        # Mantener la conexión activa mientras el juego se esté ejecutando
        while True:
            rpc.update(state="Jugando AOForever", details="En un juego emocionante! AOForever.org")
            time.sleep(15)  # Actualiza cada 15 segundos

    except Exception as e:
        print(f"Error al conectar con Discord: {e}")

if __name__ == "__main__":
    start_discord_presence()
