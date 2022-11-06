from typing import List

from aiogram import types
from aiogram.dispatcher import FSMContext


class FilterHelper:
    end_button_text: str = 'Закончить выбор фильтров'

    @classmethod
    async def get_filter_data(cls, state: FSMContext):
        data = await state.get_data()

        if 'filters' not in data:
            data['filters'] = []

        await state.update_data(data=data)

        return data

    @classmethod
    async def add_filter_to_state(cls, state: FSMContext, filter_text: str):
        data = await state.get_data()
        data['filters'].append(filter_text)
        await state.update_data(data=data)

        return data['filters']

    @classmethod
    async def get_filter_buttons_markup(cls, selected_filter_list: List[str]):
        all_filter_list = ['Болезнь', 'Отпуск', 'Прогул']  # запрос на получение всех фильтров пользователя
        buttons = []

        for filter_text in list(filter(lambda all_filter: all_filter not in map(lambda selected_filter: selected_filter[:-1], selected_filter_list), all_filter_list)):
            buttons.append([types.KeyboardButton(text=filter_text + '✅'), types.KeyboardButton(text=filter_text + '❌')])

        buttons.append([types.KeyboardButton(text=cls.end_button_text)])

        return types.ReplyKeyboardMarkup(keyboard=buttons)

    @classmethod
    def can_change_state(cls, selected_filter_list: List[str], message_text: str):
        return cls.end_button_text in message_text and len(selected_filter_list) > 0


filter_helper = FilterHelper()