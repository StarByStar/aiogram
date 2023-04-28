from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext

from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

button = KeyboardButton('share contact', request_contact=True)
kb = ReplyKeyboardMarkup()
kb.add(button)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Отправь боту свой контакт через кнопку и он напишет тебе твой user_id и номер телефона', reply_markup=kb)  

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contacts(msg: types.Message, state: FSMContext):
    await msg.answer(f'номер успешно получен: {msg.contact.phone_number}, id пользователя:{msg.contact.user_id}', reply_markup=kb)
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp)
