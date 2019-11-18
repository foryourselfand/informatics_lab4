from xmltodict import parse
from yaml import safe_dump
from time import time


def parse_my():
    xml_file = open('schedule.xml', 'r', encoding='utf-8')
    yaml_file = open('schedule_my.yaml', 'w', encoding='utf-8')
    for xml_line in xml_file.readlines():
        xml_line = xml_line.replace('\n', '')
        yaml_line = ''

        left_open = xml_line.index('<')
        left_closed = xml_line.index('>')
        tag = xml_line[left_open + 1: left_closed]
        if tag.count('/') != 0:
            continue

        tabs = xml_line.count('\t')
        spaces = ' ' * (tabs * 2)
        yaml_line += spaces

        tag_with_a_colon = tag + ':'
        yaml_line += tag_with_a_colon

        brackets = xml_line.count('<')
        if brackets == 2:
            right_open = xml_line.index('</', left_open + 1)
            value = xml_line[left_closed + 1: right_open]
            value_with_space = ' ' + value
            yaml_line += value_with_space
        yaml_line += '\n'
        yaml_file.write(yaml_line)

    xml_file.close()
    yaml_file.close()


def parse_lib():
    xml_file = open('schedule.xml', 'r', encoding='utf-8')
    yaml_file = open('schedule_lib.yaml', 'w+', encoding='utf-8')

    xml_lines = xml_file.readlines()
    xml_str = ''.join(xml_lines)
    xml_dict = parse(xml_str, dict_constructor=dict)

    safe_dump(xml_dict, yaml_file, allow_unicode=True)

    xml_file.close()
    yaml_file.close()


def check_time(number=100):
    my_start = time()
    for i in range(number):
        parse_my()
    my_end = time()
    my_time = my_end - my_start

    lib_start = time()
    for i in range(number):
        parse_lib()
    lib_end = time()
    lib_time = lib_end - lib_start
    print('my_time:', my_time)
    print('lib_time:', lib_time)


def main():
    parse_my()
    parse_lib()

    check_time()


if __name__ == '__main__':
    main()
