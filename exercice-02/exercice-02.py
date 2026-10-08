temperature = [-3, 0, 15, 31]
for i in temperature:
    if i < 0:
        print(f"{i}°C : gel")    
    elif i < 15:
        print(f"{i}°C :froid")
    elif i < 25:
        print(f"{i}°C :doux")
    else:
        print(f"{i}°C :chaud")

année = [2024,1900,2000]
for i in année:
    if i%4== 0 and i%100 != 0 or i%400==0:
        print(f"{i} : bisextile")
    else : 
        print(f"{i} : non bisextile")

