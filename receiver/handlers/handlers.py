from aiogram import types
from aiogram.dispatcher import FSMContext

from api_drivers import google_sheet_driver
from bot import BotState
from utils import filter_helper, file_helper, get_months_buttons, get_month_by_key


async def start_handler(message: types.Message, state: FSMContext) -> None:
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
    filter_buttons_markup = await filter_helper.get_filter_buttons_markup([])

    await message.answer('Выберите критерии подсчета дней:', reply_markup=filter_buttons_markup)
    await BotState.select_filters.set()


async def select_filters_handler(message: types.Message, state: FSMContext) -> None:
    if await filter_helper.can_change_state(state, message.text):
        await message.answer('Выберите месяц для создания листа в итоговом файле:',
                             reply_markup=get_months_buttons())
        await BotState.select_month.set()
        return

    selected_filters = await filter_helper.add_filter_to_state(state, message.text)
    filter_buttons_markup = await filter_helper.get_filter_buttons_markup(selected_filters)

    await message.answer('Выберите критерии подсчета дней:', reply_markup=filter_buttons_markup)


async def select_handler_handler(message: types.Message, state: FSMContext) -> None:
    month = get_month_by_key(message.text)

    data = await state.get_data()
    data['month'] = month
    await state.update_data(data=data)

    await message.answer('Введите ссылку на Google Диск с итоговым файлом',
                         reply_markup=types.ReplyKeyboardRemove())
    await BotState.send_google_url.set()


async def send_google_url_handler(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    url = message.values.get('text')
    filters = data['filters']
    files = data['files']
    month = data['month']
    await message.answer('бот начал работу')
    await google_sheet_driver.write_data_in_table(url, filters, files, month)
    await message.answer('результат записан в файл')
    await state.finish()
