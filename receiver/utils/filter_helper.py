from aiogram import types
from aiogram.dispatcher import FSMContext

from receiver.models import filter_type, GoogleSheetsFilterItem


class FilterHelper:
    _end_button_text: str = 'Закончить выбор фильтров'

    @classmethod
    async def add_filter_to_state(cls, state: FSMContext, filter_text: str) -> list[str]:
        data = await state.get_data()

        if 'filters' not in data:
            data['filters'] = []

        icon = filter_text[-1]
        filter_name = filter_text[:-1]

        data['filters'].append({'name': filter_name, 'type': filter_type.Selected if '✅' in icon else filter_type.NotSelected})
        await state.update_data(data=data)

        return data['filters']

    @classmethod
    async def get_filter_buttons_markup(cls, selected_filter_list: list[GoogleSheetsFilterItem]) -> types.ReplyKeyboardMarkup:
        all_filter_list = ['Болезнь', 'Отпуск', 'Прогул']  # запрос на получение всех фильтров пользователя
        buttons = []

        for filter_text in list(filter(lambda all_filter: all_filter not in map(lambda selected_filter: selected_filter['name'], selected_filter_list), all_filter_list)):
            buttons.append([types.KeyboardButton(text=filter_text + '✅'), types.KeyboardButton(text=filter_text + '❌')])

        buttons.append([types.KeyboardButton(text=cls._end_button_text)])

        return types.ReplyKeyboardMarkup(keyboard=buttons)

    @classmethod
    async def can_change_state(cls, state: FSMContext, message_text: str) -> bool:
        data = await state.get_data()

        return cls._end_button_text in message_text and 'filters' in data and len(data['filters']) > 0


filter_helper = FilterHelper()
