cost = int(input("Mahsulot narxini kiriitng: "))
discount = int(input("Chegirma foizini kiriitng: "))

last_cost = cost - cost * discount/100

print(f"{discount} foizli chegirma bilan mahsulotingizning narxi {last_cost}")