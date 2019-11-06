from pprint import pprint
import json
from datetime import datetime

import slava_proto_pb2


def key_value(string):
    arr = string.split(":")
    key = arr[0].strip()[1:-1]
    value = arr[1].strip()
    if value[-1] == ',':
        value = value[:-1]
    if value != '{':
        value = value[1:-1]
    return key, value


def parse_my(text):
    input_schedule = {}

    data = text.split('\n')
    day_of_week_name, trash = key_value(data[1])
    input_schedule[day_of_week_name] = {}

    i = 1
    lesson = ''
    while True:
        i = i + 1
        new_line = data[i].strip()
        if new_line == '}':
            break
        if new_line == '},':
            continue
        key, value = key_value(new_line)
        if value == '{':
            lesson = key
            input_schedule[day_of_week_name][lesson] = {}
        else:
            input_schedule[day_of_week_name][lesson][key] = value

    return input_schedule


def write(DayOfWeek):
    output_proto = open('slava_output_proto.output', 'wb')

    output_proto.write(DayOfWeek.SerializeToString())

    output_proto.close()


def read():
    input_proto = open('slava_output_proto.output', 'rb')

    DayOfWeek = slava_proto_pb2.DayOfWeek()
    DayOfWeek.ParseFromString(input_proto.read())

    input_proto.close()

    return DayOfWeek


def parse_lib(text):
    return json.loads(text)


def check_speed(text, n):
    my_start = datetime.now()
    for i in range(n):
        parse_my(text)
    my_end = datetime.now()
    my_time = (my_end - my_start).total_seconds()

    lib_start = datetime.now()
    for i in range(n):
        parse_lib(text)
    lib_end = datetime.now()
    lib_time = (lib_end - lib_start).total_seconds()
    print("my ", my_time)
    print("lib", lib_time)


def main():
    input_json = open('slava_schedule.json')
    input_text = input_json.read()
    input_json.close()

    input_schedule = parse_my(input_text)

    day_of_week_name = list(input_schedule.keys())[0]

    DayOfWeek = slava_proto_pb2.DayOfWeek()
    DayOfWeek.name = day_of_week_name
    Schedule = DayOfWeek.schedule

    for lesson_values in input_schedule[day_of_week_name].values():
        CurrentLesson = Schedule.lessons.add()
        for attribute_key, attribute_value in lesson_values.items():
            if attribute_key == 'time':
                CurrentLesson.time = attribute_value
            elif attribute_key == 'address':
                CurrentLesson.address = attribute_value
            elif attribute_key == 'classroom':
                CurrentLesson.classroom = attribute_value
            elif attribute_key == 'name_of_subject':
                CurrentLesson.name_of_subject = attribute_value
            elif attribute_key == 'teacher':
                CurrentLesson.teacher = attribute_value

    # print(DayOfWeek)
    # write(DayOfWeek)

    DayOfWeekNew = read()
    print(DayOfWeekNew)

    check_speed(input_text, 100)


if __name__ == '__main__':
    main()
