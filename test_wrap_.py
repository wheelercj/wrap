from .wrap_ import wrap_

def test_wrap_():
    input_s = """\
        The module containing the token types. There is only one correct
        argument. The only reason why the argument is required is
        because there doesn't seem to be any other way to automatically
        get the list of token types from within the file they are in."""
    expected = """\
        The module containing the token types. There is only one correct argument. The
        only reason why the argument is required is because there doesn't seem to be any
        other way to automatically get the list of token types from within the file they
        are in."""
    assert wrap_(input_s) == expected


if __name__ == '__main__':
    test_wrap_()
