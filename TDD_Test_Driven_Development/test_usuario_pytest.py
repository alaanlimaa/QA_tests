from leilao_refactored import Usuario, Leilao
import pytest
from excecoes import LanceInvalido


@pytest.fixture
def alan():
    return Usuario('alan', 20000.00) #parecido com o método setUP da unitest, cria-se o cenário para os testes

@pytest.fixture
def leilao():
    return Leilao('Motos Harley')


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(alan, leilao):
    alan.propoe_lance(leilao, 13000)

    assert alan.carteira == 7000 # usando assert o pytest reconhece a condição


def test_deve_permitir_propor_lance_quando_o_valor_for_MENOR_que_o_valor_da_carteira(alan, leilao):

    alan.propoe_lance(leilao, 13000)

    assert alan.carteira == 7000


def test_deve_permitir_propor_lance_quando_o_valor_e_IGUAL_ao_valor_da_carteira(alan, leilao):

    alan.propoe_lance(leilao, 20000)

    assert alan.carteira == 0.0


def test_nao_deve_permitir_propor_lance_quando_o_valor_MAIOR_que_o_valor_da_carteira(alan, leilao):

    with pytest.raises(LanceInvalido):

        alan.propoe_lance(leilao, 21000)

        assert alan.carteira == 20000.00

