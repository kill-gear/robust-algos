'''Script to generate Egyptian Fractions using Greedy Algorithm'''

# The Greedy algorithm works because a fraction is always reduced to
# a form where denominator is greater than numerator and numerator
# doesn’t divide denominator. For such reduced forms,
# the highlighted recursive call is made for reduced numerator.
# So the recursive calls keep on reducing the numerator till it reaches 1.


# consider 6/14, we first find ceiling of 14/6, i.e., 3
# So the first unit fraction becomes 1/3,
# then recur for (6/14 – 1/3) i.e., 4/42.

from math import ceil


def egyptian_fraction(num, den):
    if num <= 1:
        print('1/', den, end='')

        return 0
    else:
        den_temp = ceil(den/num)
        print('1/', den_temp, ' + ', end='')
        remainder_den = den_temp * den
        remainder_num = num*den_temp - 1*den
        egyptian_fraction(remainder_num, remainder_den)
        return 0


def main():

    num = int(input("Enter NUM"))
    den = int(input("Enter DEN"))
    egyptian_fraction(num, den)


if __name__ == '__main__':
    main()
