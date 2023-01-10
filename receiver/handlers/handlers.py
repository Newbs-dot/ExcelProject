from aiogram import types
from aiogram.dispatcher import FSMContext

from api_drivers import google_sheet_driver
from bot import BotState, dp
from utils import file_helper, telegram_buttons_helper


async def table_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer('Загрузите файлы', reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(BotState.upload_files)


async def start_handler(message: types.Message, state: FSMContext) -> None:
    await dp.bot.set_my_commands([
        types.BotCommand('table', 'Начать работу бота'),
        types.BotCommand('end', "Закончить работу бота"),
    ])

    await message.answer('Загрузите файлы', reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(BotState.upload_files)


async def end_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer('Бот прекратил работу', reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


async def upload_files_handler(message: types.Message, files: list[types.Message], state: FSMContext) -> None:
    if not file_helper.is_files_type_correct(files):
        await message.answer(
            f'Тип файлов некорректный\nПожалуйста загрузите файлы в одном из этих форматов {file_helper.allowed_file_types}',
            reply_markup=types.ReplyKeyboardRemove())
        return

    await file_helper.set_files_state(files, state)
    await message.answer('Получаем листы гугл таблицы')
    resp = await google_sheet_driver.get_google_sheet_lists()

    try:
        await message.answer(resp.text)
    except Exception:
        await message.answer('Выберете нужный лист', reply_markup=types.ReplyKeyboardMarkup(keyboard=telegram_buttons_helper.get_buttons_by_list(resp.name_list)))
        await BotState.select_lists.set()


async def select_lists_handler(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    files = data['files']
    list_name = message.text

    await message.answer('Бот начал работу', reply_markup=types.ReplyKeyboardRemove())
    response = await google_sheet_driver.update_google_sheets_table(list_name, files)

    try:
        await message.answer(response.text)
    except Exception:
        await message.answer('Результат записан в файл')

    await state.finish()
