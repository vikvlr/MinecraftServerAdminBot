from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from bot.keyboards.main_menu import get_main_menu_keyboard

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    welcome_text = (
        "🤖 *Добро пожаловать в Minecraft Server Admin Bot!*\n\n"
        "С помощью этого бота вы можете:\n"
        "• 📊 Проверять статус сервера\n"
        "• ⚡ Выполнять команды на сервере\n"
        "• 🔔 Получать уведомления о событиях\n"
        "• 📈 Смотреть аналитику и отчеты\n\n"
        "👇 Выберите действие в меню ниже:"
    )

    await message.answer(
        welcome_text,
        parse_mode="Markdown",
        reply_markup=get_main_menu_keyboard()
    )


@router.callback_query(F.data == "main_menu")
async def main_menu_callback(callback: CallbackQuery):
    welcome_text = (
        "🏠 *Главное меню*\n\n"
        "👇 Выберите действие:"
    )

    await callback.message.edit_text(
        welcome_text,
        parse_mode="Markdown",
        reply_markup=get_main_menu_keyboard()
    )
    await callback.answer()