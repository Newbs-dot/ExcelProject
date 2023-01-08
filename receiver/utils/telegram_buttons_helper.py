from aiogram import types


class TelegramButtonsHelper:
    @classmethod
    def get_buttons_by_list(cls, str_list: list[str]) -> list[list[types.KeyboardButton]]:
        res = []

        for i in range(0, len(str_list), 2):
            if i != len(str_list) - 1:
                res.append([types.KeyboardButton(text=str_list[i]), types.KeyboardButton(text=str_list[i + 1])])
            else:
                res.append([types.KeyboardButton(text=str_list[i])])

        return res


telegram_buttons_helper = TelegramButtonsHelper()
