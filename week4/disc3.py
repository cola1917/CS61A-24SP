def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        print(n % 10)
        swipe(n // 10)
        # 这里的N  ！！！！ 
        print(n % 10)

def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return n * skip_factorial(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    # 更好的答案
    def f(i):
        if n % i == 0:
            return n == i
        else:
            return f(i+1)
    return f(2)

def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return 1 + hailstone( n // 2)

def odd(n):
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    else:
        return 1 + hailstone( n * 3 + 1)

def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        # print('DEBUG',who,i,direction)
        if i == n:
            return who
        if has_seven(i) or i % 7 == 0:
            direction *= -1
        if who in [1,5]:
            if who == 1 and direction == -1:
                who = k +1
            elif who == 5 and direction == 1:
                who = 0
        '''
        差异部分,看起来答案更快一点,我过于追求在调用时进行参数的计算
        who = who + direction
        if who > k:
            who = 1
        if who < 1:
            who = k
        '''
        return f(i+1,who+direction,direction)


    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)
    

# 最后一个问题

