import json


file1 = open('/Users/synan/Downloads/data_2020_json/1.json', 'r')
count = 0

while True:
    count += 1

    # Get next line from file
    line = file1.readline()
    if not line:
        break

    json_object = json.loads(line.strip())

    # the result is a Python dictionary:
    if 'release' in json_object:
        if 'country' in json_object:

            print(json_object['release']['country'])



    # print("Line{}: {}".format(count, line.strip()))

file1.close()