import pytest

from calculadora.operacoes import (
    soma,
    subtracao,
    multiplicacao,
    divisao,
)


def test_soma():
    assert soma(2, 3) == 5


def test_subtracao():
    assert subtracao(5, 3) == 2


def test_multiplicacao():
    assert multiplicacao(4, 3) == 12


def test_divisao():
    assert divisao(10, 2) == 5


def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)