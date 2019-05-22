import csv

#reorder columns in Ankur's postcodeinfo merged file

with open('merged_postcodeinfo.txt', 'r', newline='', encoding='utf-8') as infile, open('reordered_postcodeinfo.csv', 'w') as outfile:
    # output dict needs a list for new column ordering
    fieldnames = ['country','postalcode','region','lat','long']
    print(fieldnames)
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')
    # reorder the header first
    writer.writeheader()
    for row in csv.DictReader(infile, delimiter='\t'):
        # writes the reordered rows to the new file
        writer.writerow(row)