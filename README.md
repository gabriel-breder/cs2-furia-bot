# Bot Telegram — FURIA CS:GO (@cs2_furia_bot)

## Descrição Geral

Este projeto é um **Bot para Telegram** que fornece informações atualizadas sobre o time de CS:GO da **FURIA**.

O bot permite:

- Listar jogadores do time.
- Exibir as notícias mais recentes.
- Informar sobre próximas partidas.
- Mostrar resultados de partidas passadas.
- Acessar as redes sociais oficiais da equipe.

---

## Como Rodar o Projeto

### 1. Criar as Migrações do Banco de Dados

Sempre que alterar ou criar modelos no Django, siga o fluxo:

1. **Criar migração:**

   ```bash
   python manage.py makemigrations
   ```

2. **Aplicar migração:**
   ```bash
   python manage.py migrate
   ```

---

### 2. Iniciar o servidor

O servidor será responsável por responder às solicitações do bot.

```bash
python manage.py runserver
```

> ⚠️ O servidor deve ser iniciado em uma instância separada do terminal.

### 3. Iniciar o bot

O bot fará as requisições para o servidor.

```bash
python bot/main.py
```

> ⚠️ O bot deve ser iniciado em uma outra instância do terminal, diferente da do servidor.

---

## Comandos Resumo

| Ação              | Comando                           |
| ----------------- | --------------------------------- |
| Criar migrações   | `python manage.py makemigrations` |
| Aplicar migrações | `python manage.py migrate`        |
| Iniciar servidor  | `python manage.py runserver`      |
| Iniciar bot       | `python bot/main.py`              |

---

## Observações

- Certifique-se de que todas as dependências estejam instaladas.
- O bot e o servidor precisam rodar simultaneamente para o funcionamento correto.

---

## Funcionalidades

### Mostrar a lista de comandos

**Comandos:** `/start` | `/help`

### Listar Jogadores

**Comando:** `/players`

- Nome real
- Nickname
- Links para redes sociais (Instagram)

### Exibir Notícias Recentes

**Comando:** `/noticias`

- Título da notícia
- Link para leitura
- Mostra as 3 últimas notícias

### Próximas Partidas

**Comando:** `/proximas`

- Nome do adversário
- Data da partida
- Hora da partida

### Resultados de Partidas Passadas

**Comando:** `/resultados`

- Nome do adversário
- Resultado da partida
- Data da partida

### Redes Sociais Oficiais

**Comando:** `/redes`

- Links oficiais da equipe FURIA

---

## Fluxo de Uso

1. O usuário acessa o bot no Telegram.
2. Digita um dos comandos disponíveis (`/start`, `/help`, `/players`, `/proximas`, `/noticias`, `/resultados`, `/redes`).
3. O bot se comunica com o servidor.
4. O servidor responde com as informações solicitadas.
