print("Enter weight in kg:",end=" ")
t=float(input())
print('''Convert to unit: 
1. Pounds
2. Tonnes
3. Quintal
4. Ounces
''')

print("Choose an option:", end=" ")
u=(input())
if u=="1":
    print(t*2.2045)
elif u=="2":
    print(t*0.001102)
elif u=="3":
    print(t*0.01)
elif u=="4":
    print(t*35.274)
else:
    print("Enter a valid option")
