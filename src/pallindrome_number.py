# TODO: Find all one digit to 10 digit numbers for which abcd * 4 = dcba

def find_all_pallindrome_numbers(number):
    for num in range(1000,10000):
        rev_num = int(str(num)[::-1])
        if num * 4 == rev_num:
            return
ans = find_all_pallindrome_numbers()
print(ans)