from random import randint
import random

ans_list = []

global our_States
our_States = ['andhra pradesh','arunachal pradesh','assam','goa','bihar','chhattisgarh','gujrat','haryana','himachal pradesh','karnataka','madhya pradesh','maharashtra','punjab','rajasthan']

global our_capitals
our_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Karnataka": "Bengaluru",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
}

# rnd = random.randint(0,len(our_States)-1)

# ans = our_States[rnd]
# print(ans)

# ans_list.append(ans)

# # print(our_States)

# our_States.remove(ans)

# random.shuffle(our_States)

# rnd = random.randint(0,len(our_States)-1)

# ans_list.append(our_States[rnd])

# # print(ans_list)

# our_States.remove(our_States[rnd])

# random.shuffle(our_States)

# rnd = random.randint(0,len(our_States)-1)

# ans_list.append(our_States[rnd])

# print(ans_list)

# # print(our_States)

# # print(our_capitals[our_States[rnd].title()])

#! doing all the above thing in one loop

cnt = 1
while cnt < 4:
    rnd = random.randint(0,len(our_States)-1)
    if cnt ==1:
        #? if the cnt is one that is first time then consider it as our ans for the state
        ans = our_States[rnd]
    
    #? put that to the ans_list
    ans_list.append(our_States[rnd])

    #? remove the selected one from the main state list
    our_States.remove(our_States[rnd])

    #? shuffle the rest to get more randomization
    random.shuffle(our_States)

    cnt +=1

print(ans_list)

print(ans)

random.shuffle(ans_list)
print(ans_list)

print(our_capitals[ans.title()])


