# There is a queue for the self-checkout tills at the supermarket. 
# Your task is write a function to calculate the total time required for all 
# the customers to check out!
# input

#     customers: an array of positive integers representing the queue. 
#     Each integer represents a customer, and its value is the amount of time 
#     they require to check out.
#     n: a positive integer, the number of checkout tills.

# output

# The function should return an integer, the total time required.
# Important

# Please look at the examples and clarifications below, 
# to ensure you understand the task correctly :)
# Examples

# queue_time([5,3,4], 1)
# # should return 12
# # because when n=1, the total time is just the sum of the times

# queue_time([10,2,3,3], 2)
# # should return 10
# # because here n=2 and the 2nd, 3rd, and 4th people in the 
# # queue finish before the 1st person has finished.

# queue_time([2,3,10], 2)
# # should return 12

# Clarifications

#     There is only ONE queue serving many tills, and
#     The order of the queue NEVER changes, and
#     The front person in the queue (i.e. the first element in the array/list) 
#     proceeds to a till as soon as it becomes free.

# N.B. You should assume that all the test input will be valid, as specified above.


# analysis
# function ->calc all time for all customers to check out
# input;
# array of positive num
    #  each num = customer
    # each customer value=time to check out
# output;
    # total time required for  check out  
# Algorithm should do the  following
# Start:
# Till A = 0
# Till B = 0

# Customer 1 -> Till A
# Till A = 1
# Till B = 0

# Customer 2 -> Till B
# Till A = 1
# Till B = 2

# Customer 3 -> least busy till (A)
# Till A = 4
# Till B = 2

# Customer 4 -> least busy till (B)
# Till A = 4
# Till B = 6

# At the end:

# Till A finishes at 4
# Till B finishes at 6

# Answer:

# max(4, 6) = 6
# till = cashier

array=[1,2,3,4]
def  queue_time(arr,n):
    till_A=0
    till_B=0
    till_c=0
    till_A=arr[0]
    till_B=arr[1]
    till_c=arr[2]
    if till_A<till_B and till_A<till_c:
        # till_A+=arr[2]
        till_B+=arr[3]
    elif till_B<till_A and till_B<till_c:
        # till_B+=arr[2]
        till_A+=arr[3]
    else:
        till_c+=arr[3]

    return max(till_A,till_B,till_c)

#Algorithm;

# 1. Create n tills with workload 0.
# 2. For each customer:
    #   find the till with the smallest workload
    #   add customer time to that till
# 3. Return the largest workload.

def queue_time(arr,n):
    tills=[]
    for i  in range(n):
       tills.append(arr[i])
    for i in range(n,len(arr)):        
        if n >=  len(arr):
           n=n-1
        smal_till_ind=tills.index(min(tills))
        tills[smal_till_ind]+=arr[i]
        
    return f"the Total time spend  for all both tills is; {max(tills)}s."
        

print(queue_time([5,3,2,1],2))


def queue_time(arr,n):
    tills=[0] * n
    for cusomer in arr:
        least_busy=tills.index(min(tills))
        tills[least_busy]+= cusomer

    return f"the Total time spend  for all  tills is; {max(tills)}s."





print(queue_time([5,3,2,1],2))

