import csv
import re

print("path to bad IPs txt file: ")
bad_ips_file = input()

with open(bad_ips_file, 'r') as f:
    bad_ips = f.read().splitlines()

print("path to the CSV file: ")
csv_file = input()

output_file = open('bad_ip_rows.csv', 'w', newline='')
writer = csv.writer(output_file)

f = open(csv_file, 'r')
reader = csv.reader(f)

for row in reader:
    for field in row:
        pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        ips = re.findall(pattern, field)
        for ip in ips:
            if ip in bad_ips:
                print('Bad IP found: ' + ip)
                writer.writerow(row)
                break
