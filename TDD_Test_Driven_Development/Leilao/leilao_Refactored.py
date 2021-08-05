'''MODULO 06 - SERVE PARA REFATORAR O CÓDIGO, OU SEJA, RETIRAR O QUE NÃO É MAIS NECESSÁRIO'''
from excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self._nome = nome
        self._carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self._valor_eh_valido(valor):
            raise LanceInvalido('Não pode propor o lance maior que o da carteira')
        lance = Lance(self, valor)
        leilao.propoe(lance)
        self._carteira -= valor


    @property
    def nome(self):
        return self._nome

    @property
    def carteira(self):
        return self._carteira

    def _valor_eh_valido(self, valor):
        return valor <= self._carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self._lances = []
        self.menor_lance = 0.0
        self.maior_lance = 0.0

    def propoe(self, lance: Lance):
        if self._lance_eh_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor

            self._lances.append(lance)

    @property
    def lances(self):
        return self._lances[:] # [:] devolve uma cópia da lista, chamado também de cópia rasa (pesquisar o que é)

    def _tem_lances(self):
        return self._lances

    def _usuario_diferentes(self, lance):
        if self._lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido('O mesmo usuário não pode dar dois lances seguidos')

    def _valor_maior_que_lance_anterior(self, lance):
        if lance.valor > self._lances[-1].valor:
            return True
        raise LanceInvalido('O valor do lance deve ser maior que o lance anterior')

    def _lance_eh_valido(self, lance):
        return not self._tem_lances() or (self._usuario_diferentes(lance) and
                                          self._valor_maior_que_lance_anterior(lance))







