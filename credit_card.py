# Christopher Geier (cpg3rb)


def check(pos_int):
    credit_card_number = str(pos_int)
    digit_sum = 0
    for i in range(1, len(credit_card_number)+1,2):
        digit_sum += int(credit_card_number[-i])
    remaining_digit_str = ''
    for i in range(2, len(credit_card_number)+1,2):
        remaining_digit_str += str(int(credit_card_number[-i])*2)
    for i in remaining_digit_str:
        digit_sum += int(i)
    return (digit_sum % 10) == 0