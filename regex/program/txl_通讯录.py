import re
text = """Ross McFluff: 834.345.1254 155 Elm Street 
Ronald Heathmore: 892.345.3428 436 finley Avenue 
Frank Burger: 925.541.7625 662 South Dogwood Way 
Heather Albrecht: 548.326.4584 939 Park Place"""

pattern = "(.*): (.*?) (.*)"

res = re.findall(pattern,text)

res_dict = {}

for item in res:
    name = item[0]
    phone_num = item[1]
    addr = item[2]
    res_dict[name] = {'phone_num':phone_num,'address':addr} 

print(res_dict)
