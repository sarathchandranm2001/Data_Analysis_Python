def Numbers():
    count = 0
    total_sum = 0
    numb=0
    
    for num in range(101, 200):
        if num % 7 == 0:
            num=numb
            count += 1
            total_sum += num
            
    return count, total_sum,numb


count_divisible, sum_divisible,numm = Numbers()


print(f"Number of integers divisible by 7: {count_divisible}")
print(f"Sum of integers divisible by 7: {sum_divisible}")
print(f"Sum of integers divisible by 7: {numm}")
