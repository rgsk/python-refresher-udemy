def test1():
    print('test1 start')
    e = 8597
    f = 8597
    print(id(e))
    print(id(f))
    print('test1 end')


def test2():
    print('test2 start')
    a = 32131232131
    b = 32131232131
    print('id(a)', id(a))
    print(id(b))
    print('test2 end')

    a = 8597
    print(id(a))
    print(id(b))


def test3():
    a = 'hello'
    b = 'hello'
    print('id(a)', id(a))
    print('id(b)', id(b))

    c = 'hel' + 'lo'
    print('id(c)', id(c))

    d = 'hel'
    d += 'lo'  # for d it differed

    print('id(d)', id(d))


test3()


def test4():
    a = 'hello'
    b = 'hello'
    print('id(a)', id(a))
    print('id(b)', id(b))

    a += 'world'
    print('id(a)', id(a))
    print('id(b)', id(b))

    c = 'helloworld'  # c may or may not be allocated the same id as a
    print('id(a)', id(a))
    print('id(c)', id(c))


def test5():
    a = 'x'
    b = 'y'
    c = 'z'

    a += 'yz'
    b = 'x' + b + 'z'
    c = 'xy' + c

    print({
        'a': a,
        'b': b,
        'c': c
    })

    print('id(a)', id(a))
    print('id(b)', id(b))
    print('id(c)', id(c))
