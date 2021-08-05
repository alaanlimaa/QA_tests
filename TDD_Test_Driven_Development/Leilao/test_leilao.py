from unittest import TestCase
from leilao_refactored import *
import pytest


class TestLeilao(TestCase):

    def setUp(self): # criação dos cenário para todos os testes
        self.gui = Usuario('Gui', 10000.00)
        self.lance_gui = Lance(self.gui, 1200.00)
        self.leilao = Leilao('Celulares')


    def test_retorna_maior_menor_valor_dolance_quando_add_em_ordem_crescente(self):
        alan = Usuario('Alan', 10000.00)
        lance_alan = Lance(alan, 1530.00)

        self.leilao.propoe(self.lance_gui)
        self.leilao.propoe(lance_alan)

        menor_valor_esperado = 1200.00
        maior_valor_esperado = 1530.00

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            alan = Usuario('Alan', 10000.00)
            lance_alan = Lance(alan, 1530.00)

            self.leilao.propoe(lance_alan)
            self.leilao.propoe(self.lance_gui)


    def test_retornar_mesmo_valor_para_maior_menor_quando_leilao_tiver_um_lance(self):

        self.leilao.propoe(self.lance_gui)

        self.assertEqual(1200.00, self.leilao.menor_lance)
        self.assertEqual(1200.00, self.leilao.maior_lance)

    def test_retornar_mesmo_valor_para_maior_menor_quando_leilao_tiver_tres_lances(self):
        aline = Usuario("Aline", 10000.00)
        alan = Usuario('Alan', 10000.00)

        lance_alan = Lance(alan, 1530.00)
        lance_aline = Lance(aline, 1300.00)

        self.leilao.propoe(self.lance_gui)
        self.leilao.propoe(lance_aline)
        self.leilao.propoe(lance_alan)

        menor_valor_esperado = 1200.00
        maior_valor_esperado = 1530.00

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # se o leilao não tiver lances, deve permitir propor um lance
    def test_permite_propor_lance_caso_leilao_nao_tenha_nenhum_lance(self):
        self.leilao.propoe(self.lance_gui)
        total_lances = len(self.leilao.lances)

        self.assertEqual(1, total_lances)

    # se o ultimo usuario for diferente, deve permitir propor o lance
    def test_permite_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 10000.00)
        lance_yuri = Lance(yuri, 1600.00)

        self.leilao.propoe(self.lance_gui)
        self.leilao.propoe(lance_yuri)

        total_lances = len(self.leilao.lances)

        self.assertEqual(2, total_lances)

    # se o outro usuario for o mesmo, não deve permitir propor o lance

    '''def test_nao_permite_propor_lance_caso_o_usuario_seja_o_mesmo(self): # com exceções jeito 01
        lance_gui200 = Lance(self.gui, 1600.00)

        try:
            self.leilao.propoe(self.lance_gui)
            self.leilao.propoe(lance_gui200)
            self.fail(msg='Não Lançou exceção') # Estamos solicitando falhar o teste, (msg='') exibe a mensagem de falha
        except ValueError:
            total_lances = len(self.leilao.lances)
            self.assertEqual(1, total_lances)
            OBS: deve ter o else no dominio'''

    def test_nao_permite_propor_lance_caso_o_usuario_seja_o_mesmo(self): # jeito 02
        lance_gui200 = Lance(self.gui, 1600.00)

        with self.assertRaises(LanceInvalido): # significa estar esperando fazer um asserção, seja lançado uma exceção
            self.leilao.propoe(self.lance_gui)
            self.leilao.propoe(lance_gui200)
