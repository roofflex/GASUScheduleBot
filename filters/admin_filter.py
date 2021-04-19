from aiogram.types import Message
from aiogram.dispatcher.filters import Filter
from data.config import ADMINS


class IsAdmin(Filter):

    async def check(self, message: Message) -> bool:
        return message.from_user.id in list(map(lambda x: int(x), ADMINS))


