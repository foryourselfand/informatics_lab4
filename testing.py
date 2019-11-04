import json
from pprint import pprint

import timetable_pb2


class FromJsonToProtoConverter:
    def __init__(self, timetable):
        self.timetable = timetable

        self.actual_lesson = dict()
        self.teacher = dict()
        self.time = dict()
        self.start_time = dict()
        self.end_time = dict()
        self.place = dict()

        self.lesson = None

    def convert(self):
        timetable = timetable_pb2.TimeTable()

        for i in range(1):
            lesson = self.timetable['lessons'][i]

            self.fill_data_from_single_lesson(lesson)

            self.lesson = timetable.lessons.add()

            self.fill_actual_lesson()
            self.fill_teacher()
            self.fill_time()
            self.fill_place()
        print(timetable)

    def fill_data_from_single_lesson(self, lesson):
        self.actual_lesson = lesson['actual_lesson']
        self.teacher = lesson['teacher']
        self.time = lesson['time']
        self.start_time = self.time['start']
        self.end_time = self.time['end']
        self.place = lesson['place']
        # pprint(self.lesson)

    def fill_actual_lesson(self):
        actual_lesson = self.lesson.actual_lesson
        actual_lesson.name = self.actual_lesson['name']
        actual_lesson_type = self.actual_lesson['lesson_type']
        if actual_lesson_type == 'ЛЕК':
            actual_lesson.lesson_type = actual_lesson.LessonType.LECTURE
        elif actual_lesson_type == 'ПРАК':
            actual_lesson.lesson_type = actual_lesson.LessonType.PRACTICE
        elif actual_lesson_type == 'ЛАБ':
            actual_lesson.lesson_type = actual_lesson.LessonType.LABORATORY_WORK

    def fill_teacher(self):
        teacher = self.lesson.teacher
        teacher.last_name = self.teacher['last_name']
        teacher.first_name = self.teacher['first_name']
        teacher.patronymic = self.teacher['patronymic']

    def fill_time(self):
        time = self.lesson.time
        time.is_even = self.time['is_even']

        start_time = time.start
        start_time.hour = self.start_time['hour']
        start_time.minute = self.start_time['minute']

        end_time = time.end
        end_time.hour = self.end_time['hour']
        end_time.minute = self.end_time['minute']

    def fill_place(self):
        place = self.lesson.place
        place.address = self.place['address']
        place.room = self.place['room']


def main():
    with open('timetable.json', 'r', encoding='utf-8') as file:
        input_data = file.read()
        timetable = json.loads(input_data)

    converter = FromJsonToProtoConverter(timetable)
    converter.convert()

    # with open('timetable.serialized', 'wb') as file:
    #     file.write(timetable.SerializeToString())


if __name__ == '__main__':
    main()
