# discord-telegram-bot
**Note:**
Automatizar contas de usuário é contra o Discord ToS e coloca sua conta em risco de exclusão.
Eu não recomendo usá-lo. Faça isso por sua conta e risco.

## Pré-requisitos

- [Python](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/) (Se você pretende implantar o aplicativo como uma imagem do Docker)

## Install

Existem duas maneiras de começar a usar o bot, dependendo da sua preferência:

### Manual

```bash
git clone https://github.com/joaojsrbr/discord-telegram-bot.git
cd discord-telegram-bot
pip install -r requirements.txt
python main.py
```

### Docker CLI

```bash
git clone https://github.com/joaojsrbr/discord-telegram-bot.git
cd discord-telegram-bot
docker build -t discord-telegram-bot .
docker run -d -v `pwd`/keys.py:/app/keys.py discord-telegram-bot:latest
```

## Configuração

Antes de executar o bot, você deve primeiro configurá-lo para que ele possa se conectar à API Discord e Telegram. Crie um arquivo keys.py e preencha as seguintes informações:

- `DISCORD_TOKEN`: token de usuário do Discord
- `DISCORD_CHANNELS`: IDs de canal para encaminhar
- `TELEGRAM_TOKEN`: Token de bot do Telegram
- `TELEGRAM_CHAT_ID`: ID do chat do Telegram para encaminhar
