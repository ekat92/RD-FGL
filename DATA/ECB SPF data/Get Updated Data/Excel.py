import os
os.chdir('G:/My Drive/....')
import csv
# Clean the file
output = open('first_edit.csv', 'w', newline='')
output.close()

flag1 = 'Off'
for doc in sorted(os.listdir()):
    if doc == '1999Q1.csv':  # First document that we ned
        flag1 = 'On'
    if flag1 == 'On':
        f = open(doc)
        csv_f = csv.reader(f)
        output = open('first_edit.csv', 'a', newline='')
        writer = csv.writer(output)

        # Which quarter to lookup (2Q ahead)
        if doc[5] == '1' or doc[5] == '2':
            lookup = doc[:5] + str(int(doc[5]) + 2)  # e.g. '2019Q2.csv' --> '2019Q4.csv'
        elif doc[5] == '3' or doc[5] == '4':
            lookup = str(int(doc[:4]) + 1) + doc[4] + str((int(doc[5]) + 2) % 4)  # e.g. '1999Q4.csv' --> '2000Q2.csv'
        else:
            print('ERROR')

        # Add appropriate rows from each doc to output file
        flag2 = 'OFF'  # flag for corresponding block, turn on for 'Growth exp...' and off with ''
        ind = -1
        for i, row in enumerate(csv_f):
            # Select Growth, Flag2 ON and next index should be for TARGET_PERIOD identification
            if row[0] == 'GROWTH EXPECTATIONS; YEAR-ON-YEAR CHANGE IN REAL GDP':
            # if row[0] == 'INFLATION EXPECTATIONS; YEAR-ON-YEAR CHANGE IN HICP':
                flag2 = "ON"
                ind = i + 1

            # Turn of the Flag
            if row[0] == '':
                flag2 = "OFF"

            # Write TARGET_PERIOD row and # of options
            if i == ind:
                count = 0
                for r in row[3:]:
                    if r != '':
                        count += 1
                row[2] = count
                try:
                    row[3 + count] = 'Volatility'
                except IndexError:
                    row.append('Volatility')
                writer.writerow(row)  # Write TARGET_PERIOD row

            # Write all the lines in the selected block + add colatility in the end
            if flag2 == "ON" and row[0] == lookup and row[2] != '':
                volcum = 0
                for i in row[3:]:
                    if i != '':
                        volcum += float(i)**2 / 100

                if volcum == 0:
                    try:
                        row[3 + count] = 1  # ASSUMPTION
                    except IndexError:
                        row.append(1)

                else:
                    try:
                        row[3 + count] = 100 / volcum
                    except IndexError:
                        row.append(100 / volcum)

                writer.writerow(row)

        # Separate block by ''
        writer.writerow([''])

        if doc == '2024Q3.csv':  # Last doc that we need
            break

f.close()
output.close()
