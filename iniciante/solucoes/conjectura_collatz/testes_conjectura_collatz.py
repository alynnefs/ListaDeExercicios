from unittest import TestCase, main
from collatz import (
    verifica_collatz,
    calcula_tamanho_da_sequencia_de_collatz,
    sequencia_de_collatz
)


class TestesPares(TestCase):
    def teste_40_deve_retornar_20(self):
        self.assertEqual(verifica_collatz(40), 20)

    def teste_20_deve_retornar_10(self):
        self.assertEqual(verifica_collatz(10), 5)

    def teste_16_deve_retornar_8(self):
        self.assertEqual(verifica_collatz(16), 8)


class TestesImpares(TestCase):
    def teste_5_devet_retornar_16(self):
        self.assertEqual(verifica_collatz(5), 16)

    def teste_13_deve_retornar_40(self):
        self.assertEqual(verifica_collatz(13), 40)

    def teste_15_deve_retornar_46(self):
        self.assertEqual(verifica_collatz(15), 46)


class TestesSequenciaCollatz(TestCase):
    def testes_13(self):
        self.assertEqual(
            sequencia_de_collatz(13),
            [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        )

    def testes_22(self):
        self.assertEqual(
            sequencia_de_collatz(22),
            [22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        )

    def testes_7(self):
        self.assertEqual(
            sequencia_de_collatz(6),
            [6, 3, 10, 5, 16, 8, 4, 2, 1]
        )


class TestesTamanhoSequenciaCollatz(TestCase):
    def testes_tamanho_sequencia_collatz_deve_retornar_16_quando_o_numero_for_22(self):
        self.assertEqual(calcula_tamanho_da_sequencia_de_collatz(22), 16)


if __name__ == '__main__':
    main()
