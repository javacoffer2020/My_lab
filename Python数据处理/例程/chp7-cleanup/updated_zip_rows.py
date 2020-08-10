from csv import reader

data_rdr = reader(open('../../data/unicef/mn.csv', 'r'))
header_rdr = reader(open('../../data/unicef/mn_headers_updated.csv', 'r', encoding='UTF-8'))

data_rows = [d for d in data_rdr]
header_rows = [[h[0], h[1]] for h in header_rdr if h[0] in data_rows[0]]

print(len(header_rows))

all_short_headers = [h[0] for h in header_rows]
skip_index = []
final_header_rows = []

for header in data_rows[0]:
    if header not in all_short_headers:
        index = data_rows[0].index(header)
        skip_index.append(index)
    else:
        for head in header_rows:
            if head[0] == header:
                final_header_rows.append(head)
                break

del all_short_headers
print(skip_index)
new_data = []

for row in data_rows[1:]:
    new_row = []
    for i, d in enumerate(row):
        if i not in skip_index:
            new_row.append(d)
    new_data.append(new_row)


zipped_data = []

for drow in new_data:
    zipped_data.append(zip(header_rows, drow))

print(list(zipped_data[0]))
print(list(zipped_data[1]))
print(list(zipped_data[2]))
print(list(zipped_data[3]))
print(list(zipped_data[4]))
