from financas.transacao import Transacao
from financas.carteira import Carteira

def main():
    carteira = Carteira()
    
    # Adicionando transações (similar a new Transacao(...) em Java)
    carteira.adicionar(Transacao("Salário", 5000.0, "Renda", "15/05/2024"))
    carteira.adicionar(Transacao("Aluguel", -1200.0, "Moradia", "15/05/2024"))
    carteira.adicionar(Transacao("Supermercado", -350.75, "Alimentação", "16/05/2024"))

    print("\n--- Todas as Transações ---")
    carteira.exibir_transacoes()

    print("\n--- Resumo Geral ---")
    carteira.resumo_geral()

if __name__ == "__main__":
    main()