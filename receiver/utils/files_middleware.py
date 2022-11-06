import asyncio
from typing import Union

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware


class FilesMiddleware(BaseMiddleware):
    _files_storage: dict = {}
    _latency: Union[int, float] = 0.01

    # сбор файлов в одну группу
    async def on_process_message(self, message: types.Message, data: dict):
        try:
            self._files_storage[message.media_group_id].append(message)
            raise CancelHandler()  # Tell aiogram to cancel handler for this group element
        except KeyError:
            self._files_storage[message.media_group_id] = [message]
            await asyncio.sleep(self._latency)
            data['files'] = self._files_storage[message.media_group_id]

    # очистка хранилища файлов
    async def on_post_process_message(self, message: types.Message, result: dict, data: dict):
        if 'files' in data and len(data['files']) != 0:
            del self._files_storage[message.media_group_id]


file_middleware = FilesMiddleware()
