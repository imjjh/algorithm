isbn = input()
asterisk_index = isbn.find("*")
isbn = list(isbn)
for i in range(10):
    isbn[asterisk_index] = i

    result = 0
    for j in range(len(isbn)):
        if j % 2 == 0:
            result += int(isbn[j])
        else:
            result += int(isbn[j]) * 3
    
    if result % 10 == 0:
        answer = i
        break
        
print(answer)