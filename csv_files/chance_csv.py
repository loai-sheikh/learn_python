import os
import csv
import wget
from termcolor import colored

CSV_URL = 'https://www.pais.co.il/chance/chance_resultsDownload.aspx'

path = os.getcwd()
chance_file_path = os.path.join(path, "Chance.csv")
print(chance_file_path)

if os.path.isfile(chance_file_path):
      os.unlink(chance_file_path)

response = wget.download(CSV_URL,path)

values = []
bastone = []
koba = []
denare = []
sbat = []

with open(chance_file_path, newline='') as f:
      reader = csv.reader(f)
      next(reader)
      for raw in reader:
            values.append([raw[5],raw[4],raw[3],raw[2]])
            bastone.append(raw[5])
            koba.append(raw[4])
            denare.append(raw[3])
            sbat.append(raw[2])

print ('\n\nlast 15 chance:')      
for i in values[:15]:
      print(i)

print ('\nlast 15 array of each kind:') 
#print last 15 array of each kind
print('\u2660')
print(bastone[:15])

print(colored('\u2665\ufe0f', 'red'))
print(koba[:15])

print(colored('\u2666\ufe0f', 'red'))
print(denare[:15])

print('\u2663')
print(sbat[:15])

