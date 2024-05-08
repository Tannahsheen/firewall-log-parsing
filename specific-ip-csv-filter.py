import csv
ip_address = 'xxx.xxx.xxx.xxx'
filtered_rows = []
with open('INPUTFILE.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['src_ip'] == ip_address or row['dst_ip'] == ip_address:
            filtered_rows.append(row)
for row in filtered_rows:
    print(row)
