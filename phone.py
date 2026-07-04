# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# import  re
# def create_phone(n):
#     result=""
#     pattern=r"(\d{3})(\d{3})(\d{4})"
#     for i in range(len(n)):
#         result +=" ".join(str(n[i]))

#     return re.sub(pattern,r"(\1) \2-\3",result)


# print(create_phone([1,2,3,4,5,6,7,8,9,0]))
# or

def create_phone(n):
    result=""
    for i in range(len(n)):
       result +=" ".join(str(n[i]))

    return f"({result[0:3]}) {result[3:6]}-{result[6:]}"


print(create_phone([1,2,3,4,5,6,7,8,9,0]))  #returns "(123) 456-7890"
