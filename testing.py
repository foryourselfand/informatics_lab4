from inout import IO
from converter import FromJsonToProtoConverter


def main():
    io = IO()
    converter = FromJsonToProtoConverter()

    timetable_input = io.get_input_timetable()
    timetable_output = converter.convert(timetable_input)
    # print(timetable_output)

    io.write_output_timetable(timetable_output)

    timetable_serialized = io.get_serialized_timetable()
    # print(timetable_serialized)

    print(timetable_output == timetable_serialized)


if __name__ == '__main__':
    main()
