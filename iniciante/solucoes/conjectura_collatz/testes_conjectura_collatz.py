from unittest import TestCase, main
from .collatz import (
    verifica_collatz,
    calcula_tamanho_da_sequencia_de_collatz,
    sequencia_de_collatz
)


class TestPares(TestCase):
    def test_40_must_return_20(self):
        self.assertEqual(verifica_collatz(40), 20)

    def test_20_must_return_10(self):
        self.assertEqual(verifica_collatz(10), 5)

    def test_16_must_return_8(self):
        self.assertEqual(verifica_collatz(16), 8)


class TestImpares(TestCase):
    def test_5_must_return_16(self):
        self.assertEqual(verifica_collatz(5), 16)

    def test_13_must_return_40(self):
        self.assertEqual(verifica_collatz(13), 40)

    def test_15_must_return_46(self):
        self.assertEqual(verifica_collatz(15), 46)


class TestSequenciaCollatz(TestCase):
    def test_13(self):
        self.assertEqual(
            sequencia_de_collatz(13),
            [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        )

    def test_22(self):
        self.assertEqual(
            sequencia_de_collatz(22),
            [22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        )

    def test_7(self):
        self.assertEqual(
            sequencia_de_collatz(6),
            [6, 3, 10, 5, 16, 8, 4, 2, 1]
        )


class TestSizeCollatzLen(TestCase):
    def test_size_when_22_must_be_16(self):
        self.assertEqual(calcula_tamanho_da_sequencia_de_collatz(22), 16)


if __name__ == '__main__':
    main()
