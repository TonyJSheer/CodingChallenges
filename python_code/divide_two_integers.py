
def divide(dividend: int, divisor: int) -> int:
    # first just convert to +ve
    neg_count = 0
    if dividend < 0:
        dividend = -dividend
        neg_count += 1
    if divisor < 0:
        divisor = -divisor
        neg_count += 1

    # now take divisor from dividend, and count how many times this takes until dividend < divisor
    divisor_doublings = [divisor]
    while dividend >= divisor:
        divisor += divisor
        divisor_doublings.append(divisor)
    if divisor_doublings:
        divisor_doublings.pop(-1)

    my_binary_quotient = ''
    for new_divisor in divisor_doublings[::-1]:
        if dividend >= new_divisor:
            dividend -= new_divisor
            my_binary_quotient += '1'
        else:
            my_binary_quotient += '0'

    if not my_binary_quotient:
        return 0
    my_binary_quotient = int(my_binary_quotient, 2)

    if neg_count == 1:
        my_binary_quotient = -my_binary_quotient
    if my_binary_quotient > 2147483647:
        my_binary_quotient = 2147483647
    return my_binary_quotient
