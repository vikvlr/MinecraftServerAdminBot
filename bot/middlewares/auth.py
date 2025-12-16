from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from typing import Callable, Dict, Any, Awaitable


class AuthMiddleware(BaseMiddleware):
    """Middleware для проверки прав администратора"""

    def __init__(self, admin_ids: list):
        super().__init__()
        self.admin_ids = admin_ids

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        if not self.admin_ids:
            return await handler(event, data)

        user_id = event.from_user.id

        if user_id in self.admin_ids:
            return await handler(event, data)
        else:
            if isinstance(event, Message):
                await event.answer("У вас нет прав для выполнения этой команды.")
            elif isinstance(event, CallbackQuery):
                await event.answer("У вас нет прав для этого действия.", show_alert=True)
            return