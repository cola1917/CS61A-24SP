def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    result = 1
    while k > 0:
        result *= n
        k -= 1
        n -= 1
    return result
    '''
    官方解
    我并没有看出来 n-k 为stop
    total, stop = 1, n-k
    while n > stop:
        total, n = total*n, n-1
    return total
    '''
    


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    result = [num for num in range(1,n+1) if num % k == 0]
    for item in result:
        print(item)
    return len(result)
    '''
    官方正经解法
    这里 for range挺好的 可能没学range吧
    count = 0
    i = 1
    while i <= n:
        if i % k == 0:
            print(i)
            count += 1
        i += 1
    return count
    '''

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    result = 0
    while y > 0:
        result += y % 10
        y //= 10
    return result
    '''
    我对一行赋值计算不熟练 没有官方优雅
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total
    '''


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    while n > 0:
        if n % 10 == 8:
            n //= 10
            if n % 10 == 8:
                return True
        else:
            n //= 10
    return False
    '''
    官方解
    我依然不够优雅  应该直接判断两位的 然后运算n
    def double_eights_alt(n):
    while n:
        if n % 10 == 8 and n // 10 % 10 == 8:
            return True
        n //= 10
    return False
    '''

