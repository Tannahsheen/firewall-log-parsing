import csv
ip_address = 'XXX.XXX.XXX.XXX'
filtered_rows = []
with open('YOURFILE.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if ip_address in row:
            filtered_rows.append(row)
if filtered_rows:
    with open('filtered.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(filtered_rows)
    print("Filtered rows written to 'filtered.csv'")
else: 
    print("IP not found")
