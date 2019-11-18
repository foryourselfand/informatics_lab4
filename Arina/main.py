from yaml import load, FullLoader
from dicttoxml import dicttoxml
from datetime import datetime


def my_convert():
    file_yaml = open('timetable.yaml', 'r', encoding='utf-8')
    file_xml = open('timetable_my.xml', 'w+', encoding='utf-8')

    keys = []
    tabs = []
    last_tabs_count = -1

    for line_yaml in file_yaml.readlines():
        line_yaml = line_yaml.replace('\n', '')
        line_xml = ''

        line_split = line_yaml.split(':')
        key = line_split[0]

        values = line_split[1:]
        value = ':'.join(values)

        spaces = key.count(' ')
        new_tabs_count = spaces // 2
        tab = '\t' * new_tabs_count

        key = key.strip()
        value = value.strip()

        if new_tabs_count < last_tabs_count:
            last_key = keys.pop()
            last_tab = tabs.pop()
            line_xml = f'{last_tab}</{last_key}>\n'
            file_xml.write(line_xml)
            line_xml = ''

        line_xml += tab
        line_xml += f'<{key}>'

        if value != '':
            line_xml += value
            line_xml += f'</{key}>'
        else:
            keys.append(key)
            tabs.append(tab)

        line_xml += '\n'
        file_xml.write(line_xml)

        last_tabs_count = new_tabs_count
    while len(keys) != 0 and len(tabs) != 0:
        last_key = keys.pop()
        last_tab = tabs.pop()
        line_xml = f'{last_tab}</{last_key}>\n'
        file_xml.write(line_xml)

    file_yaml.close()
    file_xml.close()


def lib_convert():
    file_yaml = open('timetable.yaml', 'r', encoding='utf-8')
    file_xml = open('timetable_lib.xml', 'w+', encoding='utf-8')

    dict_yaml = load(file_yaml, Loader=FullLoader)

    binary_xml = dicttoxml(dict_yaml,
                           root=False,
                           custom_root='timetable',
                           attr_type=False)
    xml = binary_xml.decode('utf-8')

    file_xml.write(xml)

    file_yaml.close()
    file_xml.close()


def time_check(num=10):
    start_my = datetime.now()
    for i in range(num):
        my_convert()
    end_my = datetime.now()
    time_my = (end_my - start_my).total_seconds()

    start_lib = datetime.now()
    for i in range(num):
        lib_convert()
    end_lib = datetime.now()
    time_lib = (end_lib - start_lib).total_seconds()
    print('time_my:', time_my)
    print('time_lib:', time_lib)


def main():
    my_convert()
    lib_convert()

    time_check()


if __name__ == '__main__':
    main()
