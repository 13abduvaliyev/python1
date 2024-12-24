number = str(input("Telefon raqam kiriting: "))

result = "+998 ("+ number[0:2] + ")-" + number[2:5] + "-" + number[5:7] + "-" + number[7:9]

print(result)