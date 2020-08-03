from xml.etree import ElementTree as ET

tree = ET.parse('../../data/chp3/data-text.xml')
root = tree.getroot()

data = root.find('Data')

all_data = []
for observation in data:
    record = {}
    for item in observation:
        lookup_key = list(item.attrib.keys())[0]
        if lookup_key == 'Numeric':
            rec_key = 'NUMERIC'
            rec_value = item.attrib['Numeric']
        else:
            rec_key = item.attrib[lookup_key]
            rec_value = item.attrib['Code']
        record[rec_key] = rec_value
    all_data.append(record)

i = 1
for data in all_data:
    print("Id No. {}".format(i))
    for item in data:
        print("    {} : {}".format(item, data[item]))
    print(" ")
    i += 1
