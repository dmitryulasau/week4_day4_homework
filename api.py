from testbook import testbook

@testbook('/path/to/notebook.ipynb', execute=True)
def test_foo(tb):
    foo = tb.ref("foo")

    assert foo(2) == 3