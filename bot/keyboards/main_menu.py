from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(text="📊 Статус сервера", callback_data="status"),
            InlineKeyboardButton(text="⚡ Быстрые команды", callback_data="quick_commands"),
        ],
        [
            InlineKeyboardButton(text="📈 Мониторинг", callback_data="monitoring"),
            InlineKeyboardButton(text="🔔 Уведомления", callback_data="notifications"),
        ],
        [
            InlineKeyboardButton(text="❓ Помощь", callback_data="help"),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)