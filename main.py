from aiogram import Bot, Dispatcher, types, executor 
from config import token
import random
bot = Bot(token)
dp = Dispatcher(bot)
@dp.message_handler(commands='start')
async def start(msg:types.Message):
    await msg.answer(f"Hello {msg.from_user.full_name}")
    await msg.answer("я загадал число от 1 до 3 угадай его")

@dp.message_handler(text=["1","2","3"])
async def lox(msg:types.Message):
    user = int(msg.text)
    rando = random.randint(1,3)
    if rando == user:
        await msg.reply(f"вы угодали правельный ответ: {rando}")
    else:
        await msg.reply(f"Ты лох: Число бота: {rando}")

executor.start_polling(dp)
