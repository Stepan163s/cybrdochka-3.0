from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)



admin_panel = ReplyKeyboardMarkup(
    adm = [
    [
                    KeyboardButton(text="status"),
                    KeyboardButton(text="ban_user"),
                    ]
                ],
                resize_keyboard=True,
            )
