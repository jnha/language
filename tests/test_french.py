"""French Language tests"""
import pytest

from language.french import orthography_to_phonology


@pytest.mark.parametrize(
    "orthography,phonology",
    [
        ("", ""),
        ("chat", "\u0283a"),
        ("chatte", "\u0283at"),
        ("eau", "o"),
        ("elle", "\u025bl"),
        ("été", "ete"),
        ("fait", "f\u025b"),
        ("Français", "f\u0280\u0251\u0303s\u025b"),
        ("huile", "\u0265il"),
        ("lettre", "l\u025bt\u0280"),
        ("plomb", "pl\u0254\u0303"),
        ("rouge", "\u0280u\u0292"),
    ],
)
def test_orthography_word(orthography, phonology):
    assert orthography_to_phonology(orthography) == phonology
