class Transacao:
    def __init__(self, descricao: str, valor: float, categoria: str, data: str):
        # Validação básica do valor
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor deve ser um número (int ou float)!")
            
        self.descricao = descricao
        self.valor = float(valor)  # Garante conversão para float
        self.categoria = categoria
        self.data = data

    def resumo(self) -> str:
        sinal = '+' if self.valor >= 0 else '-'
        valor_formatado = f"{abs(self.valor):.2f}"
        return f"{self.descricao} | {sinal}{valor_formatado} | {self.categoria} | {self.data}"

# Exemplo de uso/teste:
try:
    t1 = Transacao("Teste Inválido", "abc", "Teste", "01/01/2024")
except ValueError as e:
    print(f"Erro criando transação: {e}")  # Deve mostrar o erro