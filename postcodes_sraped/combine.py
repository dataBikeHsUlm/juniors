filenames = ['geonames_and_postcodeinfo/reordered_postcodeinfo.csv', 'geonames_and_postcodeinfo/striped_geonames.csv']
with open('geonames_and_postcodeinfo/merged_geonames_and_postcodeinfo.csv', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())