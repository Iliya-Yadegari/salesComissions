salaryLst = [250,560,370,1321,678,954,476,678,456]

count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0

for i in salaryLst:
    if i >= 200 and i <= 299:
        count2 += 1
    elif i >= 300 and i <= 399:
        count3 += 1
    elif i >= 400 and i <= 499:
        count4 += 1
    elif i >= 500 and i <= 599:
        count5 += 1
    elif i >=600 and i <= 699:
        count6 += 1
    elif i >= 700 and i <= 799:
        count7 += 1
    elif i >= 800 and i <= 899:
        count8 += 1        
    elif i >= 900 and i <= 999:
        count9 += 1
    elif i >= 1000:
        count10 += 1

print(f'Between 200 and 299 : {count2}\nBetween 300 and 399 : {count3}\nBetween 400 and 499 : {count4}\nBetween 500 and 599 : {count5}\nBetween 600 and 699 : {count6}\nBetween 700 and 799 : {count7}\nBetween 800 and 899 : {count8}\nBetween 900 and 999 : {count9}\nLarger than 1000 : {count10}')