#https://github.com/deepmind/mathematics_dataset/blob/master/mathematics_dataset/sample/arithmetic_test.py
from mathematics_dataset.sample import arithmetic
from mathematics_dataset.sample import number


for ix in range(100):
    target = number.integer_or_rational(4, signed=True)
    entropy = 9.0
    expression = arithmetic.arithmetic(target, entropy)
    print(expression)
