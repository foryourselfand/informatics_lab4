import timetable_pb2


class FromJsonToProtoConverter:
    def __init__(self):
        self.actual_lesson = dict()
        self.teacher = dict()
        self.time = dict()
        self.start_time = dict()
        self.end_time = dict()
        self.place = dict()

        self.lesson_pb = None

    def convert(self, input_timetable):
        timetable = timetable_pb2.TimeTable()

        for i in range(4):
            lesson_key = input_timetable[f'lesson_{i + 1}']
            self.fill_data_from_single_lesson(lesson_key)

            self.lesson_pb = timetable.lessons.add()
            self.fill_actual_lesson()
            self.fill_teacher()
            self.fill_time()
            self.fill_place()
        return timetable

    def fill_data_from_single_lesson(self, lesson):
        self.actual_lesson = lesson['actual_lesson']
        self.teacher = lesson['teacher']
        self.time = lesson['time']
        self.start_time = self.time['start']
        self.end_time = self.time['end']
        self.place = lesson['place']

    def fill_actual_lesson(self):
        actual_lesson = self.lesson_pb.actual_lesson
        actual_lesson.name = self.actual_lesson['name']
        actual_lesson_type = self.actual_lesson['lesson_type']
        if actual_lesson_type == 'ЛЕК':
            actual_lesson.lesson_type = actual_lesson.LessonType.LECTURE
        elif actual_lesson_type == 'ПРАК':
            actual_lesson.lesson_type = actual_lesson.LessonType.PRACTICE
        elif actual_lesson_type == 'ЛАБ':
            actual_lesson.lesson_type = actual_lesson.LessonType.LABORATORY_WORK

    def fill_teacher(self):
        teacher = self.lesson_pb.teacher
        teacher.last_name = self.teacher['last_name']
        teacher.first_name = self.teacher['first_name']
        teacher.patronymic = self.teacher['patronymic']

    def fill_time(self):
        time = self.lesson_pb.time
        time.is_even = self.time['is_even']

        start_time = time.start
        start_time.hour = self.start_time['hour']
        start_time.minute = self.start_time['minute']

        end_time = time.end
        end_time.hour = self.end_time['hour']
        end_time.minute = self.end_time['minute']

    def fill_place(self):
        place = self.lesson_pb.place
        place.address = self.place['address']
        place.room = self.place['room']
