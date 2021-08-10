files = ['1.txt', '2.txt', '3.txt']

result_dict = {}

for file in files:
    file_dict = {}
    with open(file, encoding='utf-8') as f:
        file_dict['name'] = file
        lines = f.readlines()
        file_dict['lines_count'] = len(lines)
        file_dict['data'] = ''.join(lines)
        result_dict[len(lines)] = file_dict

list_keys = sorted(list(result_dict.keys()))

with open('result.txt', 'w', encoding='utf-8') as f:
    for file in list_keys:
        f.write(result_dict[file]['name'] + '\n')
        f.write(str(result_dict[file]['lines_count']) + '\n')
        f.write(result_dict[file]['data'] + '\n')
