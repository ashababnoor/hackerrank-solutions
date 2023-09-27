'''
Piling Up!
Link: https://www.hackerrank.com/challenges/piling-up/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_stackable(arr, n) -> bool:
    order = []
    start_index = 0
    end_index = n-1
    
    print(f"Debug: {arr = }, {n = }")
    
    for i in range(n):
        print(f"Debug: {i = }, {start_index = }, {end_index = }")
        print(f"Debug: {order = }")
        
        if i == 0:
            if arr[start_index] > arr[end_index]:
                order.append(arr[start_index])
                start_index += 1
            else:
                order.append(arr[end_index])
                end_index -= 1
        else:
            if order[-1] >= arr[start_index] and order[-1] >= arr[end_index]:
                if arr[start_index] > arr[end_index]:
                    order.append(arr[start_index])
                    start_index += 1
                else:
                    order.append(arr[end_index])
                    end_index -= 1
            elif order[-1] >= arr[start_index]:
                order.append(arr[start_index])
                start_index += 1
            elif order[-1] >= arr[end_index]:
                order.append(arr[end_index])
                end_index -= 1
            else:
                return False
    
    print(f"Debug: {order = }")
    
    return True


T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    arr = [int(num) for num in input().rstrip().split()]
    
    if is_stackable(arr, n): print("Yes")
    else: print("No") 
