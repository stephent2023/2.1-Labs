companies = []
sales = []

file = open("carSale.csv", "r")
lines = file.readlines()

for x in range(0, len(lines),2):
    line = lines[x]
    companies.append(line.strip("\n\t"))
    line = lines[x+1]
    data = line.strip().split(',')
    sales.append(list(map(int,data)))

#print(companies)
#print(sales[0])

monthlysales = []
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"]
for i in range(0, 8):
    month = 0
    for j in range(0,(len(sales))):
        month += sales[j][i]
    print(months[i],":",month)
    monthlysales.append(month)

total = 0
yearlysales = []
for i in range(0,(len(sales))):
    companytotal = 0
    for j in range(0, 8):
        companytotal += sales[i][j]
        total += sales[i][j]
    print(companies[i],":",companytotal)
    yearlysales.append(companytotal)

print("Total: ",total)
