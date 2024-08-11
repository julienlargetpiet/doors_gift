import random 

n = int(input("What is the number of doors?"))
choice = int(input("What is your door number?"))
n_reduce = int(input("From how many doors you want to reduce?"))

cadeau_l = []
issu_l = []

for i in range(0, n):
    cadeau_l.append(0)
    issu_l.append(i)

id_cadeau = random.choice(issu_l) 
cadeau_l[id_cadeau] = 1
from_choice = []
for i in issu_l:
    from_choice.append(i)
from_choice.pop(id_cadeau)
from_choice.remove(choice)

cnt = 0
while cnt < n_reduce and len(from_choice) > 0:
    cur_id = random.choice(from_choice)
    cur_pop = issu_l.index(cur_id)
    issu_l.pop(cur_pop)
    cadeau_l.pop(cur_pop)
    from_choice.pop(from_choice.index(cur_id))
    cnt = cnt + 1

print("Gift distributed :)")
print(issu_l, "the doors number left")
print(cadeau_l, "gift list after the help")
print("From", 1/n, "chance to win to", (1 - 1 / n) / (len(cadeau_l) - 1), "if you change (chances to win the gift with the other doors divided by the number of them)")
choice2 = str(input("Do you want to change? (y/n)"))
if choice2 == "y":
    pre_issu_l = []
    for i in issu_l:
        pre_issu_l.append(i)
    issu_l.remove(choice)
    choice = pre_issu_l.index(random.choice(issu_l))
print(choice, "is the last choice")
if cadeau_l[choice] == 0:
    print("You have not the gift")
else:
    print("You have the gift")





