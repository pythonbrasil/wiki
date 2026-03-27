# Testando o Site

Script simples para validar o site antes de fazer PR.

## Uso

```bash
# Gere o site
make html

# Execute os testes
make test
```

## O que verifica

- JSON exposto no HTML (erro de parser)
- Estrutura basica do HTML
- Links 404 (opcional com --check-links)

## Verificar links

```bash
# Terminal 1
make serve

# Terminal 2
python test_site.py --check-links
```

Requer: `pip install requests`
