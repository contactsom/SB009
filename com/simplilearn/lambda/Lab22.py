'''
22. Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function.
'''


def sum_P_N(l) :
    sump = 0
    sumn = 0
    for positive in list(filter(lambda x : x if x >= 0 else "", l)):
        sump += positive

    for negative in list(filter(lambda x : x if x < 0 else "", l)):
        sumn += negative

    return "Sum of Positive is {} and sum of negative is {}".format(sump, sumn)


lint = [2, 4, -6, -9, 11, -12, 14, -5, 17]
result=sum_P_N(lint)

print(result)