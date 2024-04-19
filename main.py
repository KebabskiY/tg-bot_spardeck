import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F

from script import parsing


API_TOKEN = '6722886286:AAHWUq_k1cdK-giVHZz1_pZeubLUvfF1iT8'  # Основной
# API_TOKEN = '7124676371:AAExUh6yZy4oetfTQ4p8dpeVQRN2iWwOWeE' # Тестовый

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    btn = [
        [types.KeyboardButton(text="Сколько работы?")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=btn,
        resize_keyboard=True,
        input_field_placeholder="Выберите нужное действие"
    )
    await message.answer('Привет! \nЯ помогу определить как много работы тебе предстоит!',
                         reply_markup=keyboard)


@dp.message(F.text.lower() == "сколько работы?")
async def with_puree(message: types.Message):
    await message.answer('Запрашиваю данные...')
    await message.reply('\n'.join(parsing()))


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
