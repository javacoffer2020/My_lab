from csv import reader
import dataset
import numpy as np

data_rdr = reader(open('../../data/unicef/mn.csv', 'r'))
header_rdr = reader(open('../../data/unicef/mn_headers_updated.csv', 'r', encoding='UTF-8'))

data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr if h[0] in data_rows[0]]

all_short_headers = [h[0] for h in header_rows]

skip_index = []
final_header_rows = []

for header in data_rows[0]:
    if header not in all_short_headers:
        print(header)
        index = data_rows[0].index(header)
        if index not in skip_index:
            skip_index.append(index)
    else:
        for head in header_rows:
            if head[0] == header:
                final_header_rows.append(head)
                break

new_data = []

for row in data_rows[1:]:
    new_row = []
    for i, d in enumerate(row):
        if i not in skip_index:
            new_row.append(d)
    new_data.append(new_row)

zipped_data = []

for drow in new_data:
    zipped_data.append(zip(final_header_rows, drow))

# look for missing

for x in zipped_data[0]:
    if not x[1]:
        print(x)

# look for dupes


# set_of_keys = set([
#     '%s-%s-%s' % (list(x)[0][1], list(x)[1][1], list(x)[2][1]) for x in zipped_data[1:]])
#
# uniques = [x for x in zipped_data[1:] if not
#            set_of_keys.remove('%s-%s-%s' %
#                               (list(x)[0][1], list(x)[1][1], list(x)[2][1]))]


set_of_keys = list()
for x in zipped_data[1:]:
    list_x = list(x)
    set_of_keys.append('%s-%s-%s' % (list_x[0][1], list_x[1][1], list_x[2][1]))
set_of_keys = set(set_of_keys)

for x in zipped_data[1:]:
    if not(x in zipped_data):
        list_x = list(x)
        set_of_keys.remove('%s-%s-%s' % (list_x[0][1], list_x[1][1], list_x[2][1]))

print(len(set_of_keys))

# saving to db

db = dataset.connect('sqlite:///data_wrangling.db')

table = db['unicef_survey']

for row_num, data in enumerate(zipped_data):
    print(list(data))
    for question, answer in enumerate(data):
        data_dict = {
            'question': question[1],
            'question_code': question[0],
            'answer': answer,
            'response_number': row_num,
            'survey': 'mn',
        }

    # table.insert(data_dict)
