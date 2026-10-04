import matplotlib.pyplot as py # type: ignore

print("Welcome to Company Quarter goal checker")
print("This is only to check the expected/actual sales for past 2 years only")
yr = ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26", "Q4 26"]
e_sl = [] #expected sales
a_sl = [] #actual sales
inp = ""

#receiving expected sales
try :
    for i in range (0,8) :
        inp = int(input("Enter the expected sales for each quarter (from Q1 25 to Q4 26)"))
        e_sl.append(inp) #type: ignore
except SyntaxError:
    print("Only numbers are allowed")

#receiving actual sales
try :
    for i in range (0,8) :
        inp = int(input("Enter the actual sales for each quarter (from Q1 25 to Q4 26)"))
        a_sl.append(inp) #type: ignore
except ValueError:
    print("Only numbers are allowed")

py.plot(yr, e_sl, label="Expected Sales") #type: ignore
py.plot(yr, a_sl, label="Actual Sales") #type: ignore

py.xlabel("Quarter") #type: ignore
py.ylabel("Sales") #type: ignore
py.title("Expected vs Actual Sales") #type: ignore
py.legend() #type: ignore
py.show() #type: ignore

for i in range (0,8) :
    if e_sl[i] < a_sl[i] :
        sur = a_sl[i]-e_sl[i] #how much over the target (surplus) #type: ignore
        print(f"The goal was surpased in {yr[i]} by {sur}")
    elif e_sl[i] > a_sl[i] :
        defi = e_sl[i]-a_sl[i] #how much below the target (deficit) #type: ignore
        print(f"The goal was missed in {yr[i]} by {defi}")
    