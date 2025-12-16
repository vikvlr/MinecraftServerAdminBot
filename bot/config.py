import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    """Конфигурация приложения"""

    # Telegram Bot
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN не установлен в .env файле")

    # Администраторы
    ADMIN_IDS = []
    admin_ids_str = os.getenv("ADMIN_IDS", "")
    if admin_ids_str:
        try:
            ADMIN_IDS = list(map(int, admin_ids_str.split(",")))
        except ValueError:
            print("Ошибка парсинга ADMIN_IDS. Проверьте формат в .env")

    # RCON
    RCON_HOST = os.getenv("RCON_HOST", "localhost")
    RCON_PORT = int(os.getenv("RCON_PORT", 25575))
    RCON_PASSWORD = os.getenv("RCON_PASSWORD", "")

    # Server
    SERVER_NAME = os.getenv("SERVER_NAME", "Minecraft Server")