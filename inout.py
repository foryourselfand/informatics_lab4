from pprint import pprint
import timetable_pb2

from jsonparser import JsonParser


class IO:
    def __init__(self):
        self.parser = JsonParser()

    def get_input_timetable(self):
        with open('timetable.json', 'r', encoding='utf-8') as file:
            input_data = file.read()
            timetable = self.parser.parse(input_data)
        return timetable

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
    data = io.get_input_timetable()
    pprint(data)


if __name__ == '__main__':
    main()
