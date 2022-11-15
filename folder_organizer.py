import csv
import shutil
import os

csv_file = 'students.csv'

with open(csv_file, newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        #print(row[0])
        os.mkdir(row[0])
    print("Files created successfully.")

#shutil.move("data/hello_world_game","Tutorials/hello_world_game")
#print(os.listdir('data'))

file_list = os.listdir('data')

for file in file_list:
    if 'game' in file or 'Game' in file:
        shutil.move("data/"+file,"Games/"+file)
    elif 'Python' in file or 'python' in file:
        shutil.move("data/"+file,"Tutorials/"+file)

print("Games and tutorials files moved successfully.")