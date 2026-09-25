customername = input("What is your name")
CustomerAddress = input ("Input ur address")
w_done = False
L_done = False

while w_done == False:
    width = int(input("iNPUT THE width"))
    if width < 3 or width > 5:
        print("Invalid")

    else:
        w_done = True

while L_done == False:
    length = int(input("iNPUT THE length"))
    if length < 5 or width > 15:
        print("Invalid")

    else:
        L_done = True

power = 0 
panels = 0
area = length * width

if area > 15 and area < 21:
    panels = 8
    power = 3
elif area > 22 and area < 29:
    panels = 12
    power = 4.5
elif area >= 30 and area <= 39:
    panels = 16
    power = 6.4
else:
    panels = 20
    power = 8

panelCost = panels * 195
inverterCost = 1200
installationCost = 0

if panels <= 12:
    installationCost = 2300
else:
    installationCost = 4200

totalCost = panelCost +inverterCost +installationCost

print("")
print()

print("SOLAR PANEL SYSTEM QUOTATION")
print("="*36)
print(f"Customer{customername}")
print("address" + CustomerAddress)
print("="*36)

print("Roof area" + str(area) + "square meters")
print("Number of panels: " + str(panels))
print("Maximum power output" + str(power))
print("="*36)
print("COMPONENT COSTS")
print(f"SolarPanel Cost{panelCost}")
print(f"Invertert: £{inverterCost}")
print(f"Instillation: {installationCost}")
print("="*36)
print(f"TOTAL: {totalCost}")
