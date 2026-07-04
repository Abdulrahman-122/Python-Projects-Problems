#non efficint code as it contain for loop (n^2)
#  arr = [6, 9, 21]
# def solution(arr):
#     while True:
#         changed=False
#         for i in range(len(arr)):
#             for j in range(len(arr)):
#                 if arr[i]>arr[j]:
#                     arr[i]=arr[i]-arr[j]
#                     changed=True

#         if not changed:
#             return sum(arr)
# print(solution(arr));
#let's study this

def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp

    return a


def final_array(arr):
    current_gcd = arr[0]

    for i in range(1, len(arr)):
        current_gcd = gcd(current_gcd, arr[i])

    result = [] 

    for _ in range(len(arr)):
        result.append(current_gcd)

    return result

print(final_array([3,100,5]))