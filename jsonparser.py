from pprint import pprint


class JsonParser:
    def __init__(self):
        self.dicts = [{}]
        self.keys = []

    def parse(self, input_text: str):
        text = input_text.split('\n')

        for line in text:
            if ':' in line:
                temp_key, temp_value = line.split(':')
                new_key = temp_key.strip()[1:-1]
            else:
                temp_value = line
                new_key = None

            temp_value = temp_value.strip()
            temp_value = temp_value[:-1] if temp_value[-1] == ',' else temp_value

            if temp_value == '{':
                self.keys.append(new_key)
                self.dicts.append({})
            elif temp_value == '}':
                last_key = self.keys.pop()
                last_dict = self.dicts.pop()
                new_dict = self.dicts.pop()
                new_dict[last_key] = last_dict
                self.dicts.append(new_dict)
            else:
                self.keys.append(new_key)
                if "\"" in temp_value:
                    temp_value = str(temp_value[1:-1])
                elif temp_value in ['true', 'false']:
                    temp_value = temp_value[0].upper() + temp_value[1:]
                    temp_value = bool(temp_value)
                elif temp_value == 'null':
                    temp_value = None
                else:
                    if '.' in temp_value:
                        temp_value = float(temp_value)
                    else:
                        temp_value = int(temp_value)

                last_key = self.keys.pop()

                last_dict = self.dicts.pop()
                last_dict[last_key] = temp_value
                self.dicts.append(last_dict)

        return self.dicts[0][None]


def main():
    with open('timetable.json', 'r', encoding='utf-8') as input_file:
        input_data = input_file.read()

    parser = JsonParser()
    result = parser.parse(input_data)
    pprint(result)


if __name__ == '__main__':
    main()
