import csv

with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)

print(type(line))

# Важно! При работе с CSV необходимо указывать параметр newline=’’ во время открытия файла.
