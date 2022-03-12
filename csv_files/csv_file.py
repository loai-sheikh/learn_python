import csv
with open('C:/projects/python/testing/csv_files/file.csv',newline='') as f:
    reader = csv.reader(f)
    #skip title
    next(reader)
    for row in reader:
        print(row)
        #print(row[0])

with open('C:/projects/python/testing/csv_files/file.csv',newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["fruits"])

with open('C:/projects/python/testing/csv_files/file2.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([["tamar", "sausage", "wine","tofu cheese"]])


#save objects
class Cdr():

    def __iter__(self):
        return iter([self.name, self.my_value, self.my_datetime])

