import csv

with open("subjects.csv", 'w', newline='', encoding='utf-8') as f_write:
    csv_write = csv.writer(f_write, dialect='excel', delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    all_data = ['Математика', 'Физика', 'История', 'Литература']
    csv_write.writerow(all_data)
