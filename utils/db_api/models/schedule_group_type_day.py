from sqlalchemy import Integer, Column, String

from utils.db_api.db_gino import BaseModel


class ScheduleGroupTypeDay(BaseModel):
    __tablename__ = 'schedule_group_type_day'
    group_name_with_type_and_day = Column(String(40), primary_key=True)
    academic_degree = Column(String(30))
    faculty = Column(String(100))
    year = Column(Integer())
    group_name = Column(String(25))
    week_type = Column(String(15))
    day_of_week = Column(String(15))
    first_lecture_time = Column(String(15))
    first_lecture = Column(String(255))
    second_lecture_time = Column(String(15))
    second_lecture = Column(String(255))
    third_lecture_time = Column(String(15))
    third_lecture = Column(String(255))
    fourth_lecture_time = Column(String(15))
    fourth_lecture = Column(String(255))
    fifth_lecture_time = Column(String(15))
    fifth_lecture = Column(String(255))
    sixth_lecture_time = Column(String(15))
    sixth_lecture = Column(String(255))
    seventh_lecture_time = Column(String(15))
    seventh_lecture = Column(String(255))

