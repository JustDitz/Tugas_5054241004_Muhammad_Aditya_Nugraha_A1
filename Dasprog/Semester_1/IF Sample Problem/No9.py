WM = int(input("Weekday Minute: "))
NM = int(input("Night Minute: "))
WNM = int(input("Weekend Minute: "))

Cost = 3999
if(WM > 600): Cost+=((WM-600)*40)

print(f"Weekday Minute: {WM}")
print(f"Night Minute: {NM}")
print(f"Weekend Minute: {WNM}")
print(f"Pretax Bill: {round(Cost/100)}$")
print(f"Average Minute Cost: {round((WM+NM+WNM/Cost)/100)}$")
Taxes = round((Cost*5.25)/10000)
print(f"Taxes: {Taxes}$")
print(f"Total Bill: {round(Cost/100)+Taxes}$")