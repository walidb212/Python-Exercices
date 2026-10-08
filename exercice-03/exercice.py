temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]
moyenne = sum(temperatures) / len(temperatures)
print(f"Moyenne : {moyenne}")
min = min(temperatures)
max = max(temperatures)
print(f"Min : {min} / Max : {max}")
jours = 0
for i in temperatures:
    if i > 15:
        jours += 1
print(f"Jours > 15°C : {jours}")
fahrenheit = []
for i in temperatures:
    value = i*9/5+32
    fahrenheit.append(value)
print(f"Fahrenheit : {fahrenheit}")

for a, i in enumerate(temperatures):
    print(f"Jour {a+1} : {i} °C")
