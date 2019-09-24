import pytest


@pytest.mark.parametrize("s, expected", [
    ("tachycardic", True),
    (" :tacHycardic", True),
    ("taCHyca. rdic", True),
    ("Tach?ycardic ...", True),
    ("ooooops tachycardic", False)
])
def test_is_tachycardic(s, expected):
    from tachycardia import is_tachycardic
    result = is_tachycardic(s)
    return result == expected
