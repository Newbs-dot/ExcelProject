from aiogram import types
from aiogram.dispatcher import FSMContext

from bot import BotState
from utils import filter_helper, file_helper
from api_driver import api_driver


async def start_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer('Загрузите файлы', reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(BotState.upload_files)


async def end_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer('Бот прекратил работу', reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


async def upload_files_handler(message: types.Message, files: list[types.Message], state: FSMContext) -> None:
    if not file_helper.is_files_type_correct(files):
        await message.answer(f'Тип файлов некорректный\nПожалуйста загрузите файлы в одном из этих форматов {file_helper.allowed_file_types}',
                             reply_markup=types.ReplyKeyboardRemove())
        return

    await file_helper.set_files_state(files, state)
    filter_buttons_markup = await filter_helper.get_filter_buttons_markup([])

    await message.answer('Выберите критерии подсчета дней:', reply_markup=filter_buttons_markup)
    await BotState.select_filters.set()


async def select_filters_handler(message: types.Message, state: FSMContext) -> None:
    if await filter_helper.can_change_state(state, message.text):
        await message.answer('Введите ссылку на Google Диск с итоговым файлом', reply_markup=types.ReplyKeyboardRemove())
        await BotState.send_google_url.set()
        return

    selected_filters = await filter_helper.add_filter_to_state(state, message.text)
    filter_buttons_markup = await filter_helper.get_filter_buttons_markup(selected_filters)

    await message.answer('Выберите критерии подсчета дней:', reply_markup=filter_buttons_markup)


async def send_google_url_handler(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    url = message.values.get('text')
    filters = data['filters']
    files = data['files']
    resp = await api_driver.write_data_by_url(files=files, filters=filters, google_doc_url=url)
    await message.answer(resp)
    await state.finish()
