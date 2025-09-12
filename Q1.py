def reverse_integer(x):
    result = 0
    sign = -1 if x < 0 else 1  # 處理正負號
    x = abs(x)  # 取得數字的絕對值進行處理
    while x > 0:
        digit = x % 10  # 取得最後一位數字
        result = result * 10 + digit  # 將這個數字加到結果的末尾
        x = x // 10  # 移除原數字的最後一位
    return sign * result  # 恢復正負號並返回結果

# 讓使用者輸入數字進行測試
try:
    user_input = input("請輸入一個整數: ")
    number = int(user_input)
    result = reverse_integer(number)
    print(f"輸入: {number}")
    print(f"輸出: {result}")
except ValueError:
    print("輸入錯誤！請輸入有效的整數")