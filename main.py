import asyncio
import logging
import aiogram
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6759437236:AAElGqw5LBAe3oSM0G5Zn2M6JDxFcRL5Lko")
# Диспетчер
dp = Dispatcher()

@dp.message(Command("start"))
async def my_start(message: types.Message):
    await message.answer("Hello")

@dp.message(Command("button"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Кнопка 1"), types.KeyboardButton(text="Кнопка 3")],
        [types.KeyboardButton(text="Кнопка 2")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Вибери кнопку", reply_markup=keyboard)

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message, bot: Bot):
    await bot.send_dice(message.chat.id, emoji=DiceEmoji.BASKETBALL)

# @dp.message(F.text)
# async def echo_message(message: types.Message):
#     if message.text == "Кнопка 1":
#         await message.answer("Ти натиснув на кнопку 1")
#     await message.answer(message.text)

# # Запуск процесса поллинга новых апдейтов
# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())

# _______________________________________________________________________________________________________________________

# import aiogram
# import requests
# from aiogram import Bot, Dispatcher, types

# API_TOKEN = '6759437236:AAElGqw5LBAe3oSM0G5Zn2M6JDxFcRL5Lko'

# bot = Bot(token=API_TOKEN)

# dp = Dispatcher(bot)


# async def get_joke():
#     url = "https://official-joke-api.appspot.com/jokes/random"
#     response = requests.get(url)
#     joke_data = response.json()
#     return joke_data['setup'], joke_data['punchline']


# @dp.message_handler(commands=['joke'])
# async def send_joke(message: types.Message):
#     setup, punchline = await get_joke()
#     await message.answer(f"{setup}\n\n{punchline}")


# async def on_startup(dp):
#     await bot.set_my_commands([
#         types.BotCommand("joke", "Get a random joke")
#     ])


# if __name__ == '__main__':
#     from aiogram import executor
#     executor.start_polling(dp, on_startup=on_startup)
