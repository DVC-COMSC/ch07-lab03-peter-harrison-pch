
# ******************************
# Make your Code
# ******************************
numbers = []
iterat = 5
for i in range(iterat):
    numbers.append(int(input("Integer: ")))

averag = sum(numbers) / len(numbers)

answer = []
for i in range(iterat):
    if numbers[i] > averag:
        answer.append(numbers[i])

print(*answer)