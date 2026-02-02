money_string = input().split(", ")
number_beggars = int(input())
money_int = []
total_summ=[0]* number_beggars
for coin in money_string:
    money_int.append(int(coin))
for i in range(len(money_int)):
    total_summ[i % number_beggars] += money_int[i]
print(total_summ)