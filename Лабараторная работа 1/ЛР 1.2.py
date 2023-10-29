page = 100
line = 50
symbol = 25

book = (page * line * symbol) * 4
size_book = book / (1024 * 1024)
quantity = 1.44 // size_book
print("Количество книг, помещающихся на дискету:", int(quantity))
