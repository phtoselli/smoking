line = '.'
years = float(input(f"Tempo como fumante (em anos){line*5}:"))
value = float(input(f"Valor do maço{line*20}:"))
quantity = float(input(f"Quantidade de maços por dia{line*6}:"))

total_days = years * 12 * 30
quantity_total_per_day = total_days * quantity
total_value = quantity_total_per_day * value

first_param = 20000
second_param = 50000

if total_value < first_param:
    print(f"Com o valor R$ {total_value:.2f}, você poderia ter dado entrada em um carro.")
elif first_param <= total_value <= second_param:
    print(f"Com o valor R$ {total_value:.2f}, você poderia ter comprado um carro popular usado.")
else:
    print(f"Com o valor R$ {total_value:.2f}, você poderia ter comprado um carro zero.")
