from converter import FromJsonToProtoConverter
from inout import IO


def main():
    timetable_input = IO.get_input_timetable()

    converter = FromJsonToProtoConverter(timetable_input)
    timetable_output = converter.convert()
    print(timetable_output)

    IO.write_output_timetable(timetable_output)


if __name__ == '__main__':
    main()
