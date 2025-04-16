from typing import List
from financas.transacao import Transacao

class Carteira:
    def __init__(self):
        self._transacoes: List[Transacao] = []  # Similar a List<Transacao> em Java

    def adicionar(self, transacao: Transacao):
        self._transacoes.append(transacao)  # Como .add() do ArrayList

    def exibir_transacoes(self):
        for t in self._transacoes:
            print(t.resumo())

    def saldo(self) -> float:
        return sum(t.valor for t in self._transacoes)  # Stream().mapToDouble().sum()

    def filtrar_por_categoria(self, categoria: str):
        return [t for t in self._transacoes if t.categoria == categoria]  # Filtro com lambda

    def gastos_totais(self) -> float:
        return sum(t.valor for t in self._transacoes if t.valor < 0)

    def renda_total(self) -> float:
        return sum(t.valor for t in self._transacoes if t.valor >= 0)

    def resumo_geral(self):
        print(f"Total de Transações: {len(self._transacoes)}")
        print(f"Renda Total: {self.renda_total():.2f}")
        print(f"Gastos Totais: {self.gastos_totais():.2f}")
        print(f"Saldo Final: {self.saldo():.2f}")