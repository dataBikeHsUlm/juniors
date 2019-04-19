import csv

codes = {}

with open("BE.txt", "r") as file:
    reader = csv.reader(file, delimiter = "\t")
    for line in reader:
        short_code = line[1][:2]
        lat = float(line[9])
        lon = float(line[10])

        if not short_code in codes:
            codes[short_code] = []

        codes[short_code].append((lat, lon))

    print(codes)

for short_code in codes:
    lat_sum = 0
    lon_sum = 0

    for point in codes[short_code]:
        lat_sum += point[0]
        lon_sum += point[1]

    lat_avg = lat_sum / len(codes[short_code])
    lon_avg = lon_sum / len(codes[short_code])

    print("BE %s %.4f %.4f" % (short_code, lat_avg, lon_avg))