from aiogram.utils.markdown import hbold, hitalic
from utils.db_api.models.schedule_group_type_day import ScheduleGroupTypeDay

async def convert(schedule: ScheduleGroupTypeDay):
    lectures_info = []

    group_name_and_day = hbold(f"Группа {schedule.group_name}, {schedule.day_of_week}")
    week_type = hbold(f"Неделя {schedule.week_type}")

    lectures_info.append(f"{group_name_and_day}")
    lectures_info.append(f"{week_type}\n")

    empty_lecture_aliases = ["Нет занятий.", None]
    is_day_off = True
    if schedule.first_lecture not in empty_lecture_aliases:
        lectures_info.append(f"{hitalic(schedule.first_lecture_time)}\n{schedule.first_lecture}\n")
        is_day_off = False
    if schedule.second_lecture not in empty_lecture_aliases:
        lectures_info.append(f"{hitalic(schedule.second_lecture_time)}\n{schedule.second_lecture}\n")
        is_day_off = False
    if schedule.third_lecture not in empty_lecture_aliases:
        lectures_info.append(f"{hitalic(schedule.third_lecture_time)}\n{schedule.third_lecture}\n")
        is_day_off = False
    if schedule.fourth_lecture not in empty_lecture_aliases:
        lectures_info.append(f"{hitalic(schedule.fourth_lecture_time)}\n{schedule.fourth_lecture}\n")
        is_day_off = False
    if schedule.fifth_lecture not in empty_lecture_aliases:
        lectures_info.append(f"{hitalic(schedule.fifth_lecture_time)}\n{schedule.fifth_lecture}\n")
        is_day_off = False
    if schedule.sixth_lecture not in empty_lecture_aliases:
        lectures_info.append(f"{hitalic(schedule.sixth_lecture_time)}\n{schedule.sixth_lecture}\n")
        is_day_off = False
    if schedule.seventh_lecture not in empty_lecture_aliases:
        lectures_info.append(f"{hitalic(schedule.seventh_lecture_time)}\n{schedule.seventh_lecture}\n")
        is_day_off = False


    if (is_day_off):
        text_schedule = f"{group_name_and_day}\n{week_type}\n\nЗанятий нет!"
    else:
        text_schedule = "\n".join(lectures_info)

    return text_schedule
