import base64
from io import BytesIO

from aiogram import types
from aiogram.dispatcher import FSMContext

from bot import bot


class FileHelper:
    allowed_file_types: set[str] = ['xlsx', 'xls']

    @classmethod
    def is_files_type_correct(cls, files: list[types.Message]) -> bool:
        return all(file.document.file_name.split('.')[-1] in cls.allowed_file_types for file in files)

    @classmethod
    async def set_files_state(cls, files: list[types.Message], state: FSMContext) -> None:
        res = []

        for file in files:
            downloaded_file = await bot.download_file_by_id(file[file.content_type].file_id)
            bytes_io = BytesIO()
            bytes_io.write(downloaded_file.getvalue())
            encoded = base64.b64encode(bytes_io.getvalue())
            res.append(encoded.decode('ascii'))

        data = await state.get_data()
        data['files'] = res
        await state.update_data(data=data)


file_helper = FileHelper()
