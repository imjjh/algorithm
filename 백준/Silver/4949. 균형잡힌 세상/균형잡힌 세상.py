
while True:
    stack =[]
    string = input()
    flag = True

    if string == ".":
        break

    for i in string: 
        if i == "(" or i == "[":
            stack.append(i)
        elif stack and i == ")" and stack[-1] == "(":
            stack.pop()
        elif stack and i == "]" and stack[-1] == "[":
            stack.pop()
        elif i == ")" or i== "]":
            flag = False
            break

    if flag and not stack:
        print("yes")
    else:
        print("no")

        