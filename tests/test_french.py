"""French Language tests"""
import pytest

from language.french import orthography_to_phonology


@pytest.mark.parametrize(
    "orthography,phonology",
    [
        ("", ""),
        ("chat", "\u0283a"),
        ("chatte", "\u0283at"),
        ("lettre", "l\u025bt\u0280"),
    ],
)
def test_orthography_word(orthography, phonology):
    assert orthography_to_phonology(orthography) == phonology
