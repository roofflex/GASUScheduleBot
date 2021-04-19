import datetime

from data.config import TIMEZONE

from utils.db_api.db_gino import db
from utils.db_api.models.schedule_group_type_day import ScheduleGroupTypeDay
from utils.db_api.methods.user_methods import get_user_group


async def get_all_groups():
    #get "group_name" unique db entries, put in list
    query_result_list = await db.select([db.func.distinct(ScheduleGroupTypeDay.group_name)]).gino.all()
    all_groups = list(map(lambda x: x[0], query_result_list))
    return all_groups


async def get_available_faculties():
    ACADEMIC_DEGREE_BACHELOR = "БАКАЛАВРИАТ"
    ACADEMIC_DEGREE_MASTER = "МАГИСТРАТУРА"

    bachelor_faculties_query = await db.select([db.func.distinct(ScheduleGroupTypeDay.faculty)])\
        .where(ScheduleGroupTypeDay.academic_degree == ACADEMIC_DEGREE_BACHELOR).gino.all()
    bachelor_faculties_list = list(map(lambda x: str(x[0]), bachelor_faculties_query))

    master_faculties_query = await db.select([db.func.distinct(ScheduleGroupTypeDay.faculty)])\
        .where(ScheduleGroupTypeDay.academic_degree == ACADEMIC_DEGREE_MASTER).gino.all()
    master_faculties_list = list(map(lambda x: str(x[0]), master_faculties_query))

    all_faculties = [bachelor_faculties_list, master_faculties_list]
    return all_faculties




async def get_day_schedule_by_userid(user_id, weekday, week_type=None):
    # if function is invoked without week_type param, it defaults to None
    # and we get current week type
    if week_type == None:
        week_info = await get_week_info()
        week_type = week_info[0]

    user_group = await get_user_group(user_id)

    # this is schedule_group_type_day PRIMARY KEY
    primary_key = user_group + '_' + str(week_type) + '_' + str(weekday)
    target_day_schedule = await ScheduleGroupTypeDay.get(primary_key)

    return target_day_schedule


async def get_day_schedule_by_groupname(group_name, weekday, week_type=None):
    # if function is invoked without week_type param, it defaults to None
    # and we get current week type
    if week_type == None:
        week_info = await get_week_info()
        week_type = week_info[0]

    # this is schedule_group_type_day PRIMARY KEY
    primary_key = group_name + '_' + str(week_type) + '_' + str(weekday)
    target_day_schedule = await ScheduleGroupTypeDay.get(primary_key)
    return target_day_schedule



async def get_week_schedule_by_userid(user_id, week_type=None):
    # if function is invoked without week_type param, it defaults to None
    # and we get current week type
    if week_type == None:
        week_info = await get_week_info()
        week_type = week_info[0]

    user_group = await get_user_group(user_id)
    schedule_list = []
    for day_index in range(1, 7):
        primary_key = user_group + '_' + str(week_type) + '_' + str(day_index)
        schedule_for_day = await ScheduleGroupTypeDay.get(primary_key)
        schedule_list.append(schedule_for_day)
    return schedule_list



async def get_week_schedule_by_groupname(group_name, week_type=None):
    # if function is invoked without week_type param, it defaults to None
    # and we get current week type
    if week_type == None:
        week_info = await get_week_info()
        week_type = week_info[0]

    schedule_list = []
    for day_index in range(1, 7):
        primary_key = group_name + '_' + str(week_type) + '_' + str(day_index)
        schedule_for_day = await ScheduleGroupTypeDay.get(primary_key)
        schedule_list.append(schedule_for_day)
    return schedule_list


async def get_week_info(for_next_week = False):
    now = datetime.datetime.now(TIMEZONE)
    week_number = now.isocalendar()[1]

    if for_next_week:
        next_week = now + datetime.timedelta(weeks=1)
        week_number = next_week.isocalendar()[1]

    if (week_number % 2 == 0):
        week_info = [0, "ЧИСЛИТЕЛЬ"]
    else:
        week_info = [1, "ЗНАМЕНАТЕЛЬ"]
    return week_info




