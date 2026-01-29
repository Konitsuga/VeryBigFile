'''
Throw a pair of die. A player bets k1 units of money on whether 
the sum of the two numbers is Under 7 or Over 7, and k2 units
on Equal to 7. For Under 7 and Over 7, the returns are a:1,
while, for Equal to 7, the returns are b:1, if the player wins
the bet. If the bet is lost, the unit of moneygoes to the casino.
The strategy for betting will be to independently and randomly
select one of the 3 bets. The simulation will track the average return
over a large number of trails.
'''
import random
total, change, count = 100000, 0, 0 
bet_k1, a, b = 1, 1.4, 5
bet_k2 = 1
throw1 = random.randint(1, 6)
throw2 = random.randint(1, 6)
bet = random.choice(range(1, 4))  # 1 = <7, 2 = >7, 3 = =7
for i in range(1000000):
    throw1 = random.randint(1, 6)
    throw2 = random.randint(1, 6)
    bet = random.choice(range(1, 4))  # 1 = <7, 2 = >7, 3 = =7
    if total <= 0:
        break
    if bet == 1:
        if throw1 + throw2 < 7:
            total = total + bet_k1 * a
            change = change + bet_k1 * a
        else:
            total = total - bet_k1
            change = change - bet_k1
    elif bet == 2:
        if throw1 + throw2 > 7:
            total = total + bet_k1 * a
            change = change + bet_k1 * a
        else:
            total = total - bet_k1
            change = change - bet_k1
    else:
        if throw1 + throw2 == 7:
            total = total + bet_k2 * b
            change = change + bet_k2 * b
        else:
            total = total - bet_k2
            change = change - bet_k2
    count += 1
print(count, total, change/count)
# 
# Clean Code Took help of AI
import random
change, total, count = 0, 100000, 0
for i in range(1000000):
    win = False
    k1, k2 = 1, 1
    a, b = 1.4, 5

    sum = random.randint(1, 6) + random.randint(1, 6)
    bet = random.choice([1, 2, 3])

    if (bet == 1 and sum < 7) or (bet == 2 and sum > 7):
        win, roi = True, k1 * a
    elif bet == 3 and sum == 7:
        win, roi = True, k2 * b

    if win:
        total += roi
        change += roi
    else:
        total -= k1
        change -= k1
    count +=1
print(count, total, change/count)