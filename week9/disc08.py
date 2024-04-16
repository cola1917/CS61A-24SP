class Link:
    """A linked list is either a Link object or Link.empty

    >>> s = Link(3, Link(4, Link(5)))
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.rest.rest is Link.empty
    True
    >>> s.rest.first * 2
    8
    >>> print(s)
    <3 4 5>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
def strange_loop():
    """Return a Link s for which s.rest.first.rest is s.

    >>> s = strange_loop()
    >>> s.rest.first.rest is s
    True
    """
    "*** YOUR CODE HERE ***"
    s = Link(1,Link(Link(1)))
    s.rest.first.rest = s
    return s

def sum_rec(s):
    """
    Returns the sum of the elements in s.

    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_rec(a)
    14
    >>> sum_rec(Link.empty)
    0
    """
    # Use a recursive call to sum_rec
    "*** YOUR CODE HERE ***"
    if s == Link.empty:
        return 0
    if s.rest == Link.empty:
        return s.first
    else:
        return s.first + sum_rec(s.rest)
    '''
    basecase只需要定zai最后empty就可以停下来，不需要提前
    if s == Link.empty:
        return 0
    return s.first + sum_rec(s.rest)
    '''

def sum_iter(s):
    """
    Returns the sum of the elements in s.

    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_iter(a)
    14
    >>> sum_iter(Link.empty)
    0
    """
    # Don't call sum_rec or sum_iter
    "*** YOUR CODE HERE ***"
    total,rest = 0, s
    while rest != Link.empty:
        total,rest = total + rest.first, rest.rest
    return total

def overlap(s, t):
    """For increasing s and t, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap(a, b)  # 3 and 7
    2
    >>> overlap(a.rest, b)  # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    "*** YOUR CODE HERE ***"
    # if s is Link.empty or t is Link.empty:
    #     return 0
    # if s.first == t.first:
    #     return 1 + overlap(s.rest,t.rest)
    # elif s.first > t.first:
    #     return overlap(s,t.rest)
    # else:
    #     return overlap(s.rest,t)
    count = 0
    while True:
        if s is Link.empty or t is Link.empty:
            break
        elif s.first == t.first:
            count +=1
            s, t = s.rest, t.rest
        elif s.first > t.first:
            t = t.rest
        else:
            s = s.rest
    return count

# Q4
# 我不李姐

def divide(n, d):
    """Return a linked list with a cycle containing the digits of n/d.

    >>> display(divide(5, 6))
    0.8333333333...
    >>> display(divide(2, 7))
    0.2857142857...
    >>> display(divide(1, 2500))
    0.0004000000...
    >>> display(divide(3, 11))
    0.2727272727...
    >>> display(divide(3, 99))
    0.0303030303...
    >>> display(divide(2, 31), 50)
    0.06451612903225806451612903225806451612903225806451...
    """
    assert n > 0 and n < d
    result = Link(0)  # The zero before the decimal point
    "*** YOUR CODE HERE ***"
    cache = {}
    tail = result
    while n not in cache:
        # print('DEBUG',n)
        # 乘10 出来都是整数
        q, r = 10 * n // d, 10 * n % d
        # 将商存起来
        tail.rest = Link(q)
        tail = tail.rest
        # 存到字典里，再遇到这个除数时，说明遇到环了，结束了，直接连起来就行了
        cache[n] = tail
        # 余数继续除
        n = r
    # 连接环
    tail.rest = cache[n]
    return result

def display(s, k=10):
    """Print the first k digits of infinite linked list s as a decimal.

    >>> s = Link(0, Link(8, Link(3)))
    >>> s.rest.rest.rest = s.rest.rest
    >>> display(s)
    0.8333333333...
    """
    assert s.first == 0, f'{s.first} is not 0'
    digits = f'{s.first}.'
    s = s.rest
    for _ in range(k):
        assert s.first >= 0 and s.first < 10, f'{s.first} is not a digit'
        digits += str(s.first)
        s = s.rest
    print(digits + '...') 
    
