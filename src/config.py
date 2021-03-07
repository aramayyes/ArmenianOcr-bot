import os


class WebAppConfig:
    """ Web App Configuration """

    PORT = os.environ.get("PORT", 3978)


class BotConfig:
    """ Bot Configuration """

    WEBHOOK_URL = os.environ.get('WEBHOOK_URL', '')
    API_TOKEN = os.environ.get('API_TOKEN', '')
