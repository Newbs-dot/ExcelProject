from aiogram import types

months = {
    'Янв': 'январь', 'Фев': 'февраль', 'Мар': 'март', 'Апр': 'апрель', 'Май': 'май', 'Июн': 'июнь',
    'Июль': 'июль', 'Авг': 'август', 'Сен': 'сентябрь', 'Окт': 'октябрь', 'Ноя': 'ноябрь', 'Дек': 'декабрь'
}


def get_month_by_key(key: str):
    return months[key]


def get_months_buttons() -> types.ReplyKeyboardMarkup:
    buttons = []
    res = []
    i = 0
    for month in months.keys():
        i += 1
        if i == 6:
            res.append(buttons)
            buttons = []
        else:
            buttons.append(types.KeyboardButton(text=month))

    res.append(buttons)

    return types.ReplyKeyboardMarkup(keyboard=res)
