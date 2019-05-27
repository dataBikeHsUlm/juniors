import csv
import re

FILENAME = "../data/geonamesandpostcodeinfo2Dpostalcodes.csv"

# needed for loading whole csv file
countries = {}
codes = {}

def calculateShortCentroid(country, codesincountry):
    shortall = {}
    returndictshortall = {}

    for allcodes in codesincountry:
        for fullcode,coordinates in allcodes.items():
            nohyphen = fullcode.replace('-', '')
            firstdigit = re.search("\d", nohyphen)
            short_code = ""
            if firstdigit:
                print(country)
                if country == "MT":
                    short_code = nohyphen[firstdigit.start(): (firstdigit.start() + 3)]
                else:
                    short_code = nohyphen[firstdigit.start() : (firstdigit.start()+ 2)]
            else:
                short_code = nohyphen[:2]
            lat = coordinates[0][0]
            lon = coordinates[0][1]
            if not short_code in shortall:
                shortall[short_code] = []
            shortall[short_code].append((lat, lon))

    for short_code in shortall:
        lat_sum = 0
        lon_sum = 0

        for point in shortall[short_code]:
            lat_sum += point[0]
            lon_sum += point[1]
        lat_avg = lat_sum / len(shortall[short_code])
        lon_avg = lon_sum / len(shortall[short_code])
        returndictshortall[short_code] = (round(lat_avg,4),round(lon_avg,4))
        # print("%s %.4f %.4f" % (short_code, lat_avg, lon_avg))
    return (returndictshortall)


#with open("BE.txt", "r") as file:
#with open("allextract.txt", "r") as file:
with open("../data/geonames-and-postcodeinfo.csv", "r", encoding='utf-8') as file:
    reader = csv.reader(file, delimiter="\t")
    country = ""
    fieldnames = ['country','postalcode','region','lat','long', 'source']
    next(reader, None)  # skip the headers
    for line in reader:
        country = line[0]
        postal_code = line[1]
        lat = float(line[3])
        lon = float(line[4])
        source = line[5]

        if not postal_code in codes:
            codes[postal_code] = []

        if not postal_code in codes.keys():
            codes[postal_code] = [lat,lon,source]
        else:
            codes[postal_code].append((lat,lon,source))

        if not country in countries:
            countries[country] = []
        if not country in countries.keys():
            countries[country] = [codes]
        else:
            countries[country].append((codes))
            codes = {}
    #print(countries)
    #print(codes)


#https://github.com/pelias/csv-importer
#https://github.com/pelias/document-service

file= open(FILENAME, "w", newline='', encoding='utf-8')
writer = csv.writer(file, delimiter='\t')
header = ['country', '2dpostalcode','c&2dp','lat','lon']
writer.writerow(header)

for country,postcodes in countries.items():
    for shortcode,coordinates in calculateShortCentroid(country, countries[country]).items():
        line=(country, shortcode, country+shortcode, coordinates[0], coordinates[1])
        writer.writerow(line)
        #print(line)

file.close()