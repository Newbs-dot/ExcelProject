from aiogram import types
from aiogram.dispatcher import FSMContext

from api_drivers import google_sheet_driver, users_driver, filters_driver
from bot import BotState
from receiver.models import role
from utils import filter_helper, file_helper, get_months_buttons, get_month_by_key


async def start_handler(message: types.Message, state: FSMContext) -> None:
    filter_helper.all_filter_list = None
    await message.answer('производится регистрация пользователя', reply_markup=types.ReplyKeyboardRemove())
    telegram_id = message.from_user.id
    await users_driver.create_user(telegram_id)
    buttons = [[types.KeyboardButton(text='Начать работу')], [types.KeyboardButton(text='Закончить работу')]]
    await message.answer('Выберите действие бота', reply_markup=types.ReplyKeyboardMarkup(keyboard=buttons))
    await BotState.bot_menu.set()


async def table_handler(message: types.Message, state: FSMContext) -> None:
    filter_helper.all_filter_list = None
    await message.answer('производится авторизация пользователя', reply_markup=types.ReplyKeyboardRemove())
    telegram_id = message.from_user.id
    users = await users_driver.get_user(telegram_id)
    try:
        current_role = [user for user in users if user['telegram_id'] in str(telegram_id)][0]['role']
    except Exception as e:
        current_role = role.User

    if current_role == role.User:
        buttons = [[types.KeyboardButton(text='Начать работу')], [types.KeyboardButton(text='Закончить работу')]]
    else:
        buttons = [[types.KeyboardButton(text='Начать работу')], [types.KeyboardButton(text='Закончить работу')], [types.KeyboardButton(text='Добавить фильтры')]]

    await message.answer('Выберите действие бота', reply_markup=types.ReplyKeyboardMarkup(keyboard=buttons))
    await BotState.bot_menu.set()


async def bot_menu_handler(message: types.Message, state: FSMContext) -> None:
    text = message.text
    if text == 'Начать работу':
        await message.answer('Загрузите файлы', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(BotState.upload_files)
    elif text == 'Закончить работу':
        await message.answer('Бот прекратил работу', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
    elif text == 'Добавить фильтры':
        await message.answer('Введите название фильтра', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(BotState.add_filter)


async def add_filter_handler(message: types.Message, state: FSMContext) -> None:
    text = message.text
    if text != 'Введите название фильтра':
        await message.answer('Фильтр сохраняется в базу', reply_markup=types.ReplyKeyboardRemove())
        await filters_driver.create_filter(text)
        await message.answer('Фильтр добавлен', reply_markup=types.ReplyKeyboardRemove())
        buttons = [[types.KeyboardButton(text='Начать работу')], [types.KeyboardButton(text='Закончить работу')], [types.KeyboardButton(text='Добавить фильтры')]]
        await message.answer('Выберите действие бота', reply_markup=types.ReplyKeyboardMarkup(keyboard=buttons))
        await BotState.bot_menu.set()
        return
    await message.answer('Фильтр добавляется', reply_markup=types.ReplyKeyboardRemove())


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


async def select_month_handler(message: types.Message, state: FSMContext) -> None:
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
