import csv
import sys

filename=sys.argv[1]
with open(filename, "r") as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    maths,biology,english,physics,chemistry,hindi,names = [],[],[],[],[],[],[]
    for row in data:
      names.append(row[0])
      maths.append(row[1])
      biology.append(row[2])
      english.append(row[3])
      physics.append(row[4])
      chemistry.append(row[5])
      hindi.append(row[6])
names.remove('Name')        
maths.remove('Maths')
biology.remove('Biology')
english.remove('English')
physics.remove('Physics')
chemistry.remove('Chemistry')
hindi.remove('Hindi')
#converting the marks which are strings to integers
biology = [int(i) for i in biology]
maths = [int(i) for i in maths]
english = [int(i) for i in english]
physics = [int(i) for i in physics]
chemistry = [int(i) for i in chemistry]
hindi = [int(i) for i in hindi]
#finding the toppers of each subjects
mathsmax= max(maths)
matindices = [index for index, value in enumerate(maths) if value == mathsmax]
print("Topper in Maths is :")
for i in matindices:
  print(names[i])
print('\n')
biomax= max(biology)
bioindices = [index for index, value in enumerate(biology) if value == biomax]
print("Topper in biology is :")
for i in bioindices:
  print(names[i])
print('\n')
engmax= max(english)
engindices = [index for index, value in enumerate(english) if value == engmax]
print("Topper in english is :")
for i in engindices:
  print(names[i])
print('\n')
phymax= max(physics)
phyindices = [index for index, value in enumerate(physics) if value == phymax]
print("Topper in Physics is :")
for i in phyindices:
  print(names[i])
print('\n')


chemax= max(chemistry)
cheindices = [index for index, value in enumerate(chemistry) if value == chemax]
print("Topper in Chemistry is :")
for i in cheindices:
  print(names[i])
print('\n')
hinmax= max(hindi)
hinindices = [index for index, value in enumerate(hindi) if value == hinmax]
print("Topper in Hindi is :")
for i in hinindices:
  print(names[i])

print('\n')


#finding the best students in the class
avg=0
avg1=0
avg1i=0
avg2=0
avg2i=0
avg3=0
avg3i=0
for i in range(len(names)):
  avg=(biology[i]+maths[i]+chemistry[i]+physics[i]+english[i]+hindi[i])/6
  if avg>=avg1:
    avg3=avg2
    avg2=avg1
    avg1=avg
    avg3i=avg2i
    avg2i=avg1i
    avg1i=i
  elif avg>=avg2:
    avg3=avg2
    avg2=avg
    avg3i=avg2i
    avg2i=i
  elif avg>=avg3:
    avg3=avg
    avg3i=i

print("Best students in the class are :"+names[avg1i]+","+names[avg2i]+","+names[avg3i])

    
