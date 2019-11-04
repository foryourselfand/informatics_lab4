from pprint import pprint

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


def main():
    io = IO()
    data = io.get_input_timetable()
    pprint(data)


if __name__ == '__main__':
    main()
