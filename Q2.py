def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    prev_prev = 0  
    prev = 1       
    for i in range(2, n + 1):
        current = prev + prev_prev  
        prev_prev = prev           
        prev = current
    return prev

# 輸入一個非負整數來計算費波那契數
user_input = input("請輸入 n 值: ")
n = int(user_input)
print(f"F{n} = {fibonacci_iterative(n)} (使用迭代法)")
print(f"F{n} = {fibonacci_recursive(n)} (使用遞迴法)")