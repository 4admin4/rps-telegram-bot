import os
import random
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Налаштування логування
logging.basicConfig(level=logging.INFO)

# Отримання токена (ми налаштуємо його пізніше в системі)
TOKEN = "7123456789:ABCDefGhIjKlMnOpQrStUvWxYz"

bot = Bot(token=TOKEN)
dp = Dispatcher()

CHOICES = ["Камінь 🪨", "Ножиці ✂️", "Папір 📄"]

def get_keyboard():
    builder = ReplyKeyboardBuilder()
    for choice in CHOICES:
        builder.add(types.KeyboardButton(text=choice))
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привіт! Давай зіграємо. Обирай свій варіант:",
        reply_markup=get_keyboard()
    )

@dp.message(F.text.in_(CHOICES))
async def play_game(message: types.Message):
    user_choice = message.text
    bot_choice = random.choice(CHOICES)
    
    if user_choice == bot_choice:
        result = "🤝 Нічия!"
    elif (user_choice == "Камінь 🪨" and bot_choice == "Ножиці ✂️") or \
         (user_choice == "Ножиці ✂️" and bot_choice == "Папір 📄") or \
         (user_choice == "Папір 📄" and bot_choice == "Камінь 🪨"):
        result = "🎉 Ти переміг!"
    else:
        result = "😢 Я переміг!"

    await message.answer(f"Мій вибір: {bot_choice}\nТвій вибір: {user_choice}\n\n{result}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
