# test_tachycardia.py
import pytest


@pytest.mark.parametrize("s, expected", [
    ("tachycardic", True),
    (" taCHyca. rdic", True),
    ("Tach?ycardic ...", True),
    ("tchycardic", True),    # Miss one word
    ("tachyQcardic", True),  # Insert one word
    ("t0chycard1c", True),   # Mistake two words
    ("t0chycrd1c", False),   # Mistake or miss three words
    ("ooooops Tachycardic,", True)  # The string contains "tachycardic"
])
def test_is_tachycardic(s, expected):
    from tachycardia import is_tachycardic
    result = is_tachycardic(s)
    assert result == expected
