# bot-telegram-crypto

El proyecto es un bot en Telegram. El mismo responde con información que obtenemos a través de una API de Coingecko con las 100 criptomonedas con mayor capitlización de mercado.  

## Mensajes que responde el bot
- /start -> Mensaje de bienvenida al bot.
- /help -> Explicación de cómo consultar una criptomoneda en particular, y que otros mensajes responde.
- /coin criptomoneda -> donde criptomoneda debe ser el simbolo de la misma. Ejemplo: /coin btc para obtener información de Bitcoin.
- /social -> para que puedas seguirmne en Linkedin y/o mires mis respositorios de GitHub.

## Pasos para iniciar el bot
1. Dentro de Telegram iniciar un chat con @BotFather, utilizar el comando /newbot. @BotFather nos pedirá un nombre para nuestro bot,
y luegos nos dará un token de seguridad (que este token sea personal, no lo compartas).

2. En este caso mi token está oculto, se podría optar por dos opciones:
    - Crear un archivo token.py, crear una variable my_token = 'Token asignado por @BotFather' y luego importarlo (como fue en mi caso).
    - Reemplazar la llamada a la variable token.my_token por el asignado por @BotFather.  

## Dependencias que utiliza
- pip install response
- pip install python-telegram-bot
