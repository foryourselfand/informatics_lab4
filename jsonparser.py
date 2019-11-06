from pprint import pprint


class JsonParser:
    def __init__(self):
        self.dicts = [{}]
        self.keys = []

    def parse(self, input_text: str):
        lines = input_text.split('\n')

        for line in lines:
            if ':' in line:
                current_key, current_value = line.split(':')
                new_key = current_key.strip()[1:-1]
            else:
                new_key = None
                current_value = line

            current_value = current_value.strip()
            current_value = current_value[:-1] if current_value[-1] == ',' else current_value

            if current_value == '{':
                self.keys.append(new_key)
                self.dicts.append({})
            elif current_value == '}':
                last_key = self.keys.pop()
                last_dict = self.dicts.pop()
                new_dict = self.dicts.pop()
                new_dict[last_key] = last_dict
                self.dicts.append(new_dict)
            else:
                self.keys.append(new_key)
                if "\"" in current_value:
                    current_value = str(current_value[1:-1])
                elif current_value in ['true', 'false']:
                    current_value = current_value[0].upper() + current_value[1:]
                    current_value = bool(current_value)
                elif current_value == 'null':
                    current_value = None
                else:
                    if '.' in current_value:
                        current_value = float(current_value)
                    else:
                        current_value = int(current_value)

                last_key = self.keys.pop()

                last_dict = self.dicts.pop()
                last_dict[last_key] = current_value
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
