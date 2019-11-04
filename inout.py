import json
from pprint import pprint


class IO:
    @staticmethod
    def get_input_timetable():
        with open('timetable.json', 'r', encoding='utf-8') as file:
            input_data = file.read()
            timetable = json.loads(input_data)
        return timetable

    @staticmethod
    def write_output_timetable(timetable):
        with open('timetable.serialized', 'wb') as file:
            file.write(timetable.SerializeToString())


def main():
    data = IO.get_input_timetable()
    pprint(data)


if __name__ == '__main__':
    main()
