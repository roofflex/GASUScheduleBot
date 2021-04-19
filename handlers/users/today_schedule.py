from loader import dp
from aiogram.dispatcher.filters import Command
from states.registration import RegistrationStates
from aiogram.types import Message
from data.config import TIMEZONE
from utils.db_api.methods.schedule_methods import get_day_schedule_by_userid
from utils import schedule_to_text
from keyboards.inline import share_schedule
import datetime

@dp.message_handler(Command("today"), state=RegistrationStates.RegistrationComplete)
async def show_today_schedule(message: Message):
    # weekday is number 0-6(monday-sunday), we increment it, so it is 1-7
    now = datetime.datetime.now(TIMEZONE)
    weekday = now.weekday() + 1

    if(weekday == 7):
        await message.answer(text="Cегодня воскресенье, занятий нет!\n"
                                  "Хороших выходных!")
    else:
        user_id = message.from_user.id

        schedule = await get_day_schedule_by_userid(user_id=user_id, weekday=weekday)
        await message.answer(text="Расписание на сегодня:")
        text_schedule = await schedule_to_text.convert(schedule)
        await message.answer(text=text_schedule, reply_markup=share_schedule.generate_keyboard(""))



