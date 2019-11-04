import json
from pprint import pprint

import timetable_pb2


def convert(timetable_dict):
    timetable = timetable_pb2.TimeTable()
    for i in range(1):
        lesson_dict = timetable_dict['lessons'][i]

        actual_lesson_dict = lesson_dict['actual_lesson']
        teacher_dict = lesson_dict['teacher']
        time_dict = lesson_dict['time']
        start_time_dict = time_dict['start']
        end_time_dict = time_dict['end']
        place_dict = lesson_dict['place']
        pprint(lesson_dict)

        lesson = timetable.lessons.add()

        actual_lesson = lesson.actual_lesson
        actual_lesson.name = actual_lesson_dict['name']
        actual_lesson.lesson_type = actual_lesson_dict['lesson_type']
        # print(lesson.actual_lesson)

        teacher = lesson.teacher
        teacher.last_name = teacher_dict['last_name']
        teacher.first_name = teacher_dict['first_name']
        teacher.patronymic = teacher_dict['patronymic']
        # print(lesson.teacher)

        time = lesson.time
        time.parity = time_dict['parity']

        start_time = time.start
        start_time.hour = start_time_dict['hour']
        start_time.minute = start_time_dict['minute']

        end_time = time.end
        end_time.hour = end_time_dict['hour']
        end_time.minute = end_time_dict['minute']
        # print(lesson.time)

        place = lesson.place
        place.address = place_dict['address']
        place.room = place_dict['room']
        # print(lesson.place)


with open('timetable.json', 'r', encoding='utf-8') as file:
    input_data = file.read()
    timetable_dict = json.loads(input_data)

convert(timetable_dict)

# with open('timetable.serialized', 'wb') as file:
#     file.write(timetable.SerializeToString())
