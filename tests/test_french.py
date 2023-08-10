"""French Language tests"""
import pytest

from language.french import orthography_to_phonology


@pytest.mark.parametrize(
    "orthography,phonology",
    [
        ("", ""),
        ("chat", "\u0283a"),
        ("chatte", "\u0283at"),
        ("fait", "f\u025b"),
        ("lettre", "l\u025bt\u0280"),
        ("rouge", "\u0280u\u0292"),
    ],
)
def test_orthography_word(orthography, phonology):
    assert orthography_to_phonology(orthography) == phonology
