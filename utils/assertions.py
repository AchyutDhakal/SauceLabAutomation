def assert_true(condition, message):
    assert condition, message

def assert_false(condition, message):
    assert not condition, message

def assert_equal(actual, expected, message):
    assert actual == expected, message

def assert_not_equal(actual, expected, message):
    assert actual != expected, message