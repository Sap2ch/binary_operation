num = abs(int(input()))
result, count = num, 0

while num != 1 and result != 0:
    if num == 1:
        count += 1
        break
    elif num % 2 == 0:
        num = num // 2
        count += 1
    elif num % 2 == 1:
        num += 1

print(f'При количестве {result} нужно провести {count+1} операцию с вычислениями.' if result == 1\
    else f'При количестве {result} нужно провести {count} операций с вычислениями.')