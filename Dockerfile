# Usa imagem Alpine (leve e segura)
FROM python:3.11-alpine

WORKDIR /app

# Copia estrutura necessária
COPY financas/ financas/
COPY main.py ./

# Instala dependências de compilação (se necessário)
RUN apk add --no-cache gcc musl-dev

CMD ["python", "main.py"]
