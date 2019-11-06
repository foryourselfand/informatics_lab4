from pprint import pprint
import timetable_pb2
import json
from datetime import datetime

from jsonparser import JsonParser


class IO:
    def __init__(self):
        self.parser = JsonParser()
        self.text = ''
        self.read_text()

    def read_text(self):
        with open('timetable.json', 'r', encoding='utf-8') as file:
            self.text = file.read()

    def get_input_timetable(self):
        return self.parser.parse(self.text)

    def get_input_timetable_by_loads(self):
        return json.loads(self.text)

    def single_speed_test(self, parse_function, number: int = 1000):
        start_time = datetime.now()
        for i in range(number):
            parse_function()
        end_time = datetime.now()
        all_time = (end_time - start_time).total_seconds()
        return all_time

    def speed_test(self, number: int = 1000):
        my_time = self.single_speed_test(self.get_input_timetable, number)
        lib_time = self.single_speed_test(self.get_input_timetable_by_loads, number)
        print('my_time:', my_time)
        print('lib_time:', lib_time)

    @staticmethod
    def write_output_timetable(timetable):
        with open('timetable.serialized', 'wb') as file:
            file.write(timetable.SerializeToString())

    @staticmethod
    def get_serialized_timetable():
        timetable = timetable_pb2.TimeTable()
        with open('timetable.serialized', 'rb') as file:
            timetable.ParseFromString(file.read())
        return timetable


def main():
    io = IO()
    io.speed_test()


if __name__ == '__main__':
    main()
