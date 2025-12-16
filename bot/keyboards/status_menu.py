from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_status_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(text="🔄 Обновить", callback_data="status"),
            InlineKeyboardButton(text="↩️ Назад", callback_data="main_menu"),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)