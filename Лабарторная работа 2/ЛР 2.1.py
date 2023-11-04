money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
count_mounth = 0
remain = money_capital
while remain > (spend - salary):
    remain += salary
    remain -= spend
    count_mounth += 1
    spend *= (1 + increase)


print("Количество месяцев, которое можно протянуть без долгов:",  count_mounth)
