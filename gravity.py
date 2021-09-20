import csv

from numpy import MAY_SHARE_BOUNDS

data = []
with open('BrownDwarfs.csv','r') as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data.append(row)

headers = data[0]
temp_list = data[1:]

Masses = []
Radiuses = []

for row in temp_list:
    Masses.append(float(row[3]))
    Radiuses.append(float(row[4]))

G = 6.67e-11
for i in range(0,len(temp_list)):
    m = Masses[i]*1.989e+30
    r = Radiuses[i]*6.957e+8
    gravity = str((G*m)/(r*r)) + ' m/s2'
    temp_list[i].append(gravity)

headers.append('Gravity')
print(temp_list[1]) 
print(headers)    

with open('Result_data.csv','w') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(temp_list)