ranges = 0
celcius = 0
vballoon = 0
kelvin = 0
log = []
tem = 2800/(99+273.15)

ranges = int(input())

for x in range(0,ranges):
    celcius = float(input())
    kelvin = celcius+273.15
    vballoon = kelvin*tem
    log.append(round(vballoon,7))
for n in log: print(n)
