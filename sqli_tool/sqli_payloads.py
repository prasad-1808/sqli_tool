
classic_payloads = []

with open('classic_sqli.txt','r') as file:
    for payload in file.readlines():
        classic_payloads.append(payload.strip())

time_based_payloads = []

with open('time_based_sqli.txt','r') as file:
    for payload in file.readlines():
        time_based_payloads.append(payload.strip())

