# 🐍 Python Condicionais — if, elif e else

> Repositório de aprendizado com exemplos comentados sobre estruturas condicionais em Python.

---

## 📚 Conteúdo

| Arquivo | Descrição |
|---|---|
| [`01_if_basico.py`](exemplos/01_if_basico.py) | Uso básico do `if` |
| [`02_if_else.py`](exemplos/02_if_else.py) | Combinando `if` com `else` |
| [`03_if_elif_else.py`](exemplos/03_if_elif_else.py) | Múltiplas condições com `elif` |
| [`04_condicionais_aninhadas.py`](exemplos/04_condicionais_aninhadas.py) | Condicionais dentro de condicionais |
| [`05_exemplos_praticos.py`](exemplos/05_exemplos_praticos.py) | Exemplos do mundo real |

---

## 🧠 Conceitos

### `if` — "Se"
Executa um bloco de código **somente se** a condição for verdadeira.

```python
if condicao:
    # código executado se condicao == True
```

### `else` — "Senão"
Executa um bloco alternativo quando a condição do `if` é falsa.

```python
if condicao:
    # executado se True
else:
    # executado se False
```

### `elif` — "Senão, se"
Verifica uma nova condição quando a anterior foi falsa. Evita aninhar vários `if`.

```python
if condicao1:
    # executado se condicao1 == True
elif condicao2:
    # executado se condicao1 == False e condicao2 == True
else:
    # executado se todas as condições forem False
```

---

## 🚀 Como usar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/python-condicionais.git

# Entre na pasta
cd python-condicionais

# Execute qualquer exemplo
python exemplos/01_if_basico.py
```

---

## 📝 Requisitos

- Python 3.8+
- Nenhuma biblioteca externa necessária

---

## 👤 Autor

Feito com 💚 durante o aprendizado de Python.

---

## 📄 Licença

MIT — sinta-se livre para usar e modificar!
