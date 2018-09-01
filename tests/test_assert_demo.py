def test_simple_assert():
    assert 1 == 2

def test_func_result():
    assert 0 == min(max(1, ord('2')), min(3, max(len('abcd'), 5), 6 + 7 * 8 - 0o11))
