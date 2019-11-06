import json
from datetime import datetime

import schedule_pb2


def get_key_and_value(s):
    a = s.split(":")
    key = a[0].strip().replace('"', '')
    value = a[1].strip().replace('"', '')
    if value[-1] == ',':
        value = value[:-1]
    return key, value


def get_schedule_by_my(text):
    schedule = dict()

    a = text.split('\n')

    index = 1
    lesson_key = ''
    while True:
        line = a[index].strip()
        index = index + 1
        if line == '},':
            continue
        elif line == '}':
            break
        key, value = get_key_and_value(line)
        if value == '{':
            lesson_key = key
            schedule[lesson_key] = dict()
        else:
            schedule[lesson_key][key] = value
    return schedule


def write_schedule(schedule):
    with open('out.out', 'wb') as file:
        file.write(schedule.SerializeToString())


def read_schedule():
    schedule = schedule_pb2.Schedule()
    with open('out.out', 'rb') as file:
        schedule.ParseFromString(file.read())
    return schedule


def get_schedule_by_lib(text):
    return json.loads(text)


def speed_test(input_text, number):
    start_my = datetime.now()
    for i in range(number):
        get_schedule_by_my(input_text)
    end_my = datetime.now()
    time_my = end_my - start_my

    start_lib = datetime.now()
    for i in range(number):
        get_schedule_by_lib(input_text)
    end_lib = datetime.now()
    time_lib = end_lib - start_lib

    print("number: ", number)
    print("my speed", time_my.total_seconds())
    print("lib speed", time_lib.total_seconds())


def main():
    with open('schedule.json') as file:
        text = file.read()

    schedule_dict = get_schedule_by_my(text)
    schedule_pb = schedule_pb2.Schedule()

    for lesson_values in schedule_dict.values():
        lesson = schedule_pb.lessons.add()
        for key, value in lesson_values.items():
            if key == 'name':
                lesson.name = value
            elif key == 'teacher':
                lesson.teacher = value
            elif key == 'time':
                lesson.time = value
            elif key == 'place':
                lesson.place = value
            elif key == 'room':
                lesson.room = value

    write_schedule(schedule_pb)

    new_schedule_pb = read_schedule()
    print(new_schedule_pb)
    speed_test(text, 1000)


if __name__ == '__main__':
    main()
