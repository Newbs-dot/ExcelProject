import asyncio

import aiohttp


async def _get_request(session, url: str):
    async with session.get(url) as response:
        return await response.text()


async def _post_request(session, url: str, body):
    async with session.post(url, json=body) as response:
        return await response.text()


async def send_get_request(url: str):
    async with aiohttp.ClientSession() as session:
        tasks = [_get_request(session, url)]
        result = (await asyncio.gather(*tasks))[0]

    return result


async def send_post_request(url: str, body):
    async with aiohttp.ClientSession() as session:
        tasks = [_post_request(session, url, body)]
        result = (await asyncio.gather(*tasks))[0]

    return result
