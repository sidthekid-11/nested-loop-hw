num = int(input("Enter a decimal number: "))

before = num

b = ""

if num == 0:
    b = "0"
else:
    while num > 0:
        remainder = num % 2      
        b = str(remainder) + b 
        num = num // 2        

print("Binary of", before, "is:", b)