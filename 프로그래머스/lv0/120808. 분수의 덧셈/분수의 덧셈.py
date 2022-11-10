import fractions

def solution(denum1, num1, denum2, num2):
    answer = []
    s = 0
    a = fractions.Fraction(denum1, num1)
    b = fractions.Fraction(denum2, num2)
    s = a + b
    answer.append(s.numerator)
    answer.append(s.denominator)
    return answer