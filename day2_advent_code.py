password_array = []
match_pass1 = 0
match_pass2 = 0
with open('day2_input.txt') as my_file:
    for line in my_file:
        password_array.append(line)
for i in range(len(password_array)):
    split_pass = password_array[i]
    limits, letter, password = split_pass.split(' ')
    min, max = limits.split('-')
    min = int(min)
    max = int(max)
    # print(password[min - 1])
    # print(password[max - 1])
    letter = letter[0]
    count_letter = (password.count(letter))
    if max >= count_letter >= min:
        # print("passworld match")
        match_pass1 += 1
    if (bool(password[min - 1] == letter) != bool(password[max - 1] == letter)):
        match_pass2 += 1
print('answer part 1 : %d' % match_pass1)
print('answer part 2 : %d' % match_pass2)
