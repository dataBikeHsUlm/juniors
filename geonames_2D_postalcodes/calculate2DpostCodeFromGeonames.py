import csv

FILENAME = "geonames2Dpostalcodes.csv"

# needed for loading whole csv file
countries = {}
codes = {}

def calculateShortCentroid(country):
    shortall = {}
    returndictshortall = {}

    for allcodes in country:
        for fullcode,coordinates in allcodes.items():
            short_code = fullcode[:2]
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
with open("allCountries.txt", "r") as file:
    reader = csv.reader(file, delimiter="\t")
    country = ""
    for line in reader:
        country = line[0]
        postal_code = line[1]
        lat = float(line[9])
        lon = float(line[10])

        if not postal_code in codes:
            codes[postal_code] = []

        if not postal_code in codes.keys():
            codes[postal_code] = [lat,lon]
        else:
            codes[postal_code].append((lat,lon))

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

#name postcode source layer	lat	 lon

file= open(FILENAME, "w", newline='')
writer = csv.writer(file)
header = ['country','postcode','source','layer','lat','lon']
writer.writerow(header)

for country,postcodes in countries.items():
    #print(country,calculateShortCentroid(countries[country]))
    for shortcode,coordinates in calculateShortCentroid(countries[country]).items():
        line=(country, shortcode, 'geonames2D', 'postalcode', coordinates[0], coordinates[1])
        writer.writerow(line)
        #print(line)

file.close()