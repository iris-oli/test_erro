import pytest

from calculadora.operacoes import (
    divisao,
    multiplicacao,
    soma,
    subtracao,
)


def test_soma():
    assert soma(2, 3) == 5


