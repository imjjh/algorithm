def solution(phone_book):
    dict={}
    phone_book=set(phone_book)
    for num in phone_book:
        dict[num]=0
        
    for num in phone_book:
        sub_num = ""
        for ch in num:
            sub_num+=ch
            if sub_num in phone_book and sub_num != num:
                return False
    
    return True
    