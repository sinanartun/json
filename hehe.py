from __future__ import print_function
import json
import sys


# def get_edges(treedict, parent=None):
#     name = next(iter(treedict.keys()))
#     if parent is not None:
#         edges.append((parent, name))
#     for item in treedict[name]["children"]:
#         if isinstance(item, dict):
#             get_edges(item, parent=name)
#         else:
#             edges.append((name, item))

file1 = open('/Users/synan/Downloads/data_2020_json/1.json', 'r')
count = 0

while True:
    count += 1

    # Get next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break

    data = json.loads(line)
    # print(json.dumps(data, indent=4), file=sys.stderr)
    print(data["release"])



file1.close()
# Tree in JSON format

# Convert JSON tree to a Python dict


# Convert back to JSON & print to stderr so we can verify that the tree is correct.


# Extract tree edges from the dict




