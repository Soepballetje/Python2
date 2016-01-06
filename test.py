import xlrd
import csv
import sys

# write from xls file to csv file
# wb = xlrd.open_workbook('test.xls')
# sh = wb.sheet_by_name('Sheet1')
your_csv_file = open('Desktop-Ward.csv', 'wb')
wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

# for rownum in xrange(sh.nrows):
#     wr.writerow(sh.row_values(rownum))

your_csv_file.close()
print "Converted from xls to csv!"
# write from csv file to html

# if len(sys.argv) < 3:
#   print "Usage: csvToTable.py csv_file html_file"
#   exit(1)

# Open the CSV file for reading
reader = csv.reader(open("Desktop-Ward.csv"))

# Create the HTML file for output
htmlfile = open("data.html","w+")

# initialize rownum variable
rownum = 0

# generate table contents
for row in reader: # Read a single row from the CSV file
    for line in htmlfile:
        # this HTML comment is found in the HTML file where I want to insert the table
        if line == "<!-- Table starts here !-->":
            # write <table> tag
            htmlfile.write('<table>')
            htmlfile.write('<tr>') # write <tr> tag
            for column in row:
                htmlfile.write('<th>' + column + '</th>')
            htmlfile.write('</tr>')
            # write </table> tag
            htmlfile.write('</table>')

        #increment row count
        rownum += 1



# print results to shell
print "Created " + str(rownum) + " row table."
exit(0)