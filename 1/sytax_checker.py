input = input()

res = [input[0]]
slist = list(input[1:])
for s in slist:
    if len(res)>0:
        if res[-1]=='(':
            if s==')':
                res.pop()
            else: res.append(s)
        elif res[-1]=='[':
            if s==']':
                res.pop()
            else: res.append(s)
        elif res[-1]=='{':
            if s=='}':
                res.pop()
            else: res.append(s)
    else: res.append(s)

# print(res)
print(bool(not res))