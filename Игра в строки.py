#спортпрога 29.10.2025

k = int(input())
 
kratos = input()
kratos_len = len(kratos)
 
arey = input()
arey_len = len(arey)
 
if arey_len < k or kratos_len < k:
    print('NO')
    exit(0)
 
arey_dict = {}
for char in arey:
    if char in arey_dict:
        arey_dict[char] += 1
    else:
        arey_dict[char] = 1
 
kratos_dict = {}
for i in range(k):
    if kratos[i] in kratos_dict:
        kratos_dict[kratos[i]] += 1
    else:
        kratos_dict[kratos[i]] = 1
 
flag = True
for key, value in kratos_dict.items():
    if key in arey_dict and arey_dict[key] >= value:
        continue
    else:
        flag = False
        break
 
if flag:
    print('YES')
    exit(0)
 
for i in range(1, kratos_len - k + 1):
    kratos_dict[kratos[i - 1]] -= 1
    if kratos_dict[kratos[i -  1]] == 0:
        kratos_dict.pop(kratos[i - 1])
    if kratos[k + i - 1] in kratos_dict:
        kratos_dict[kratos[k + i - 1]] += 1
    else:
        kratos_dict[kratos[k + i - 1]] = 1
 
    flag = True
    for key, value in kratos_dict.items():
        if key in arey_dict and arey_dict[key] >= value:
            continue
        else:
            flag = False
            break
    if flag:
        print('YES')
        exit(0)
print('NO')
