from main import test_function as cal

def test(a,b,c):
    res = cal(a,b)

    assert res == c


test(10,20, 10 + 20)
test(1,15, 1 + 15)
test(40,150, 40 + 151) #broken
