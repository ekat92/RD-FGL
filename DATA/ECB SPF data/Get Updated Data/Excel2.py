import os
os.chdir('G:/My Drive/...')
import csv
import pandas
# Clean the file
output = open('second_edit.csv', 'w', newline='')
output.close()
##reported dates + two more quarters
fdates = ['1999Q3', '1999Q4', '2000Q1', '2000Q2', '2000Q3', '2000Q4', '2001Q1', '2001Q2', '2001Q3', '2001Q4', '2002Q1', '2002Q2', '2002Q3', '2002Q4', '2003Q1', '2003Q2', '2003Q3', '2003Q4', '2004Q1', '2004Q2', '2004Q3', '2004Q4', '2005Q1', '2005Q2', '2005Q3', '2005Q4', '2006Q1', '2006Q2', '2006Q3', '2006Q4', '2007Q1', '2007Q2', '2007Q3', '2007Q4', '2008Q1', '2008Q2', '2008Q3', '2008Q4', '2009Q1', '2009Q2', '2009Q3', '2009Q4', '2010Q1', '2010Q2', '2010Q3', '2010Q4', '2011Q1', '2011Q2', '2011Q3', '2011Q4', '2012Q1', '2012Q2', '2012Q3', '2012Q4', '2013Q1', '2013Q2', '2013Q3', '2013Q4', '2014Q1', '2014Q2', '2014Q3', '2014Q4', '2015Q1', '2015Q2', '2015Q3', '2015Q4', '2016Q1', '2016Q2', '2016Q3', '2016Q4', '2017Q1', '2017Q2', '2017Q3', '2017Q4', '2018Q1', '2018Q2', '2018Q3', '2018Q4', '2019Q1', '2019Q2', '2019Q3', '2019Q4','2020Q1', '2020Q2', '2020Q3', '2020Q4','2021Q1', '2021Q2', '2021Q3', '2021Q4','2022Q1', '2022Q2', '2022Q3', '2022Q4','2023Q1', '2023Q2', '2023Q3', '2023Q4','2024Q1', '2024Q2', '2024Q3', '2024Q4','2025Q1']

output = open('second_edit.csv', 'a', newline='')
writer = csv.writer(output)

writer.writerow([''] + fdates)

for k in range(128):    # for each k (forecaster)
    row = [k + 1]       # [1]
    for t in range(len(fdates)):  # for each t (time)
        date = fdates[t]        # '1999Q3'
        f = open('first_edit.csv')  # THESE TWO LINES ARE NECESSARY FOR CORRECT LOOPING
        csv_f = csv.reader(f)       # THESE TWO LINES ARE NECESSARY FOR CORRECT LOOPING
        flag = 'NoValueFound'
        for j, i in enumerate(csv_f):
            if i[0] == date and i[1] == str(k + 1):
                row.append(i[2])
                flag = 'ValueFound'
        if flag == 'NoValueFound':
            row.append('')
    writer.writerow(row)


f.close()
output.close()
