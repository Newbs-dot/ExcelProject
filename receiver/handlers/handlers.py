from typing import List

from aiogram import types
from aiogram.dispatcher import FSMContext

from bot import BotState
from utils import filter_helper


async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Загрузите файлы', reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(BotState.upload_files)


async def end_handler(message: types.Message, state: FSMContext):
    await message.answer('Бот прекратил работу', reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


async def upload_files_handler(message: types.Message, files: List[types.Message]):
    files_media_group = types.MediaGroup()

    for file in files:
        file_id = file[file.content_type].file_id
        files_media_group.attach({"media": file_id, "type": file.content_type})

    await message.answer_media_group(files_media_group)

    filter_buttons_markup = await filter_helper.get_filter_buttons_markup([])
    await message.answer('Выберите критерии подсчета дней:', reply_markup=filter_buttons_markup)
    await BotState.select_filters.set()


async def select_filters_handler(message: types.Message, state: FSMContext):
    selected_filters = await filter_helper.get_filter_data(state)

    if filter_helper.can_change_state(selected_filters, message.text):
        await message.answer('Введите ссылку на Google Диск с итоговым файлом', reply_markup=types.ReplyKeyboardRemove())
        await BotState.send_google_url.set()
        return

    selected_filters = await filter_helper.add_filter_to_state(state, message.text)
    filter_buttons_markup = await filter_helper.get_filter_buttons_markup(selected_filters)

    await message.answer('Выберите критерии подсчета дней:', reply_markup=filter_buttons_markup)


async def send_google_url_handler(message: types.Message, state: FSMContext):
    await message.answer('итоговый урл')
    await state.finish()
