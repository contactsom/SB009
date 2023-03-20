import csv


teacherData=[
                ["NAME","EMAIL","PHONE"],
                ["Mohan","mohan@gmail.com",12345],
                ["Raj","raj@gmail.com",9856],
                ["John","john@gmail.com",909856]
             ]


with open('teacher.csv', mode='w') as file:
    writer=csv.writer(file)
    for i in teacherData:
        writer.writerow(i)