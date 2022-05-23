import logging

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = ''


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)


    text_and_data = (
        ('Rus 🇷🇺', 'rus'),
        ('Eng 🇬🇧', 'eng'),
    )
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)

    keyboard_markup.row(*row_btns)
    keyboard_markup.add(

        types.InlineKeyboardButton('developer', url='https://t.me/zekicks'),
    )

    await message.reply("Привет, выбери язык!\nHello, choose a language!", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='rus')  
@dp.callback_query_handler(text='eng')  
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data

    await query.answer(f'You answered with {answer_data!r}')

    if answer_data == 'rus':
        text = 'Выбран русский язык!'
    elif answer_data == 'eng':
        text = 'selected English'

    await bot.send_message(query.from_user.id, text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)