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

### 1. Instalar as dependências

Instale todas as dependências do projeto utilizando o arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

### 2. Configurar variáveis de ambiente

Crie um arquivo .env na raiz do projeto (ou exporte as variáveis diretamente no terminal) com as seguintes configurações:

```bash
export BOT_TOKEN='YOUR-BOT-TOKEN'
export API_URL='http://localhost:8000/api'
```

> ⚠️ Por questões de segurança, o arquivo .env **não está incluído no repositório**, mas o bot token utilizado no bot (@cs2-furia-bot) foi enviado junto ao form.

### 3. Iniciar o servidor

O servidor será responsável por responder às solicitações do bot. O script abaixo já inicia todas as migrações, popula o banco de dados e inicia o servidor.

```bash
python manage.py run_api
```

> ⚠️ O servidor deve ser iniciado em uma instância separada do terminal.

### 4. Iniciar o bot

O bot fará as requisições para o servidor.

```bash
python bot/main.py
```

> ⚠️ O bot deve ser iniciado em uma outra instância do terminal, diferente da do servidor.

### 5. Acessar o Bot

Você pode acessar o bot de diferentes formas:

- Clicando neste [link](https://web.telegram.org/k/#@cs2_furia_bot).

- Copiando e colando o seguinte URL no navegador: https://web.telegram.org/k/#@cs2_furia_bot.

- Pesquisando diretamente no Telegram por: @cs2_furia_bot.

---

## Comandos Resumo

| Ação             | Comando                    |
| ---------------- | -------------------------- |
| Iniciar servidor | `python manage.py run_api` |
| Iniciar bot      | `python bot/main.py`       |

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
