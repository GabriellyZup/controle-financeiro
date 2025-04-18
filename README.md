# 💰 Controle Financeiro Pessoal em Python

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](https://www.python.org/)
[![GitHub Actions](https://github.com/GabriellyZup/controle-financeiro/actions/workflows/ci.yml/badge.svg)](https://github.com/GabriellyZup/controle-financeiro/actions)
[![Open in GitHub](https://img.shields.io/badge/GitHub-Open%20Source-success)](https://github.com/GabriellyZup/controle-financeiro)

Sistema de controle financeiro pessoal implementado em Python utilizando Programação Orientada a Objetos (POO), com CI/CD e containerização.

## 🚀 Funcionalidades

- ✅ Registro de transações financeiras (entradas e saídas)
- ✅ Validação de tipos de dados
- ✅ Cálculo automático de saldo
- ✅ Filtragem por categorias
- ✅ Containerização com Docker/Podman
- ✅ CI/CD com GitHub Actions

## 📦 Estrutura do Projeto

```bash
controle-financeiro/
├── .github/
│   └── workflows/
│       └── ci.yml       # Pipeline de CI/CD
├── financas/
│   ├── __init__.py
│   ├── transacao.py     # Classe Transacao
│   └── carteira.py      # Classe Carteira
├── main.py              # Execução principal
├── Dockerfile           # Configuração de container
├── .gitignore
└── README.md
```

## ⚙️ Instalação

### Ambiente Local
```bash
git clone https://github.com/GabriellyZup/controle-financeiro.git
cd controle-financeiro

python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

python main.py
```

### Containerização (Podman/Docker)
```bash
# Build da imagem
podman build -t controle-financeiro .

# Executar container
podman run --rm controle-financeiro
```

## 🧑💻 Uso

```bash
# Execução local
python main.py

# Execução via container
podman run --rm controle-financeiro
```

**Saída:**
```
Erro criando transação: O valor deve ser um número (int ou float)! 👮♀️

--- Todas as Transações ---
Salário | +5000.00 | Renda | 15/05/2024
Aluguel | -1200.00 | Moradia | 15/05/2024
Supermercado | -350.75 | Alimentação | 16/05/2024

--- Resumo Geral ---
Total de Transações: 3
Renda Total: 5000.00
Gastos Totais: -1550.75
Saldo Final: 3449.25
```

## 🛠 CI/CD Pipeline
O projeto utiliza GitHub Actions para:
- ✅ Execução automática de testes em push
- ✅ Verificação de compatibilidade com Python 3.11
- ✅ Validação da construção do Dockerfile

![CI/CD Pipeline](https://github.com/GabriellyZup/controle-financeiro/actions/workflows/ci.yml/badge.svg)

## 🤝 Contribuição
```bash
1. Faça um fork do projeto
2. Crie sua feature branch (git checkout -b feature/incrivel)
3. Commite suas mudanças (git commit -m 'feat: Minha feature incrível')
4. Push para a branch (git push origin feature/incrivel)
5. Abra um Pull Request
```

---
Desenvolvido com ❤️ por [GabriellyZup](https://github.com/GabriellyZup)  
💪 **Mulheres na tecnologia transformando linhas de código em soluções reais!** 🐍🚀
