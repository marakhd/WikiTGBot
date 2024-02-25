#Импортируем конфиг и функции
import config as cfg
import functions as func

#Импортируем логирование и asyncio
import asyncio
import logging

#Импортируем aiogram и его модули
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

#Включаем логирование для отладки
logging.basicConfig(level=logging.INFO)

#Объявляем бота и диспетчера
bot = Bot(token=cfg.TOKEN, parse_mode="HTML") #Берем токен из конфига
dp = Dispatcher()

#Хендлер для команды старт
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f'Привет! \n\nЭто бот Wikipedia.'
                         f'\nТы можешь отправить мне слово, а я найду его значение на Wikipedia.org')

#Хендлер для команды why
@dp.message(Command("why"))
async def start(message: types.Message):
    await message.answer(f'Мы OpenSource проект телеграм бота википедии!'
                         f'\nВы можете наблюдать за разработкой на нашем <a href="{cfg.GITHUB}">GitHub</a>', disable_web_page_preview = True)

#Хендлер для команды help
@dp.message(Command("help"))
async def start(message: types.Message):
    await message.answer(f'Если бот не отвечает, значит он нашел несколько вариантов ответа. '
                         f'\nПопробуйте задать вопрос конкретнее!'
                         f'\nНапример: <s>python</s> <b>Python язык</b>')
    await message.answer(f'После отправки запроса боту, нужно чуть чуть подождать(3-5сек)')

#Хендлер для текстовых запросов
@dp.message(F.text)
async def search(message: types.Message):
    query = message.text
    msg = await message.answer('Обрабатываем ваш запрос...')
    response = await func.process_query(query)
    await msg.delete()
    await message.reply(response)

@dp.message()
async def nottext(message: types.Message):
    if not message.text:
        await message.answer(f'Это не текст! \nДанный бот принимает только текстовые сообщение.')

#Функция запуска пулинга
async def main():
    await dp.start_polling(bot)

#Запускаем функцию пулинга
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt):
        print('Bot sucess stoped')