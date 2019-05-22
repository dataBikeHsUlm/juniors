import csv

#country code      : iso country code, 2 characters
#postal code       : varchar(20)
#place name        : varchar(180)
#admin name1       : 1. order subdivision (state) varchar(100)
#admin code1       : 1. order subdivision (state) varchar(20)
#admin name2       : 2. order subdivision (county/province) varchar(100)
#admin code2       : 2. order subdivision (county/province) varchar(20)
#admin name3       : 3. order subdivision (community) varchar(100)
#admin code3       : 3. order subdivision (community) varchar(20)
#latitude          : estimated latitude (wgs84)
#longitude         : estimated longitude (wgs84)
#accuracy          : accuracy of lat/lng from 1=estimated, 4=geonameid, 6=centroid of addresses or shape

fieldnames = ['country','postalcode','region','lat','long']

with open("allgeonames.txt","rt", encoding='utf-8') as source, open('striped_geonames.csv', 'w') as outfile:
    rdr= csv.reader(source, delimiter='\t')
    with outfile:
        wtr= csv.writer( outfile, delimiter='\t' )
        for r in rdr:
            wtr.writerow( (r[0], r[1], r[2], r[9], r[10]) )