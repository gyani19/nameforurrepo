class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "6889147649:AAEJNWXlMTKu88E_rpNKRzv_TrPfkmF_CdE6889147649:AAEJNWXlMTKu88E_rpNKRzv_TrPfkmF_CdE"
    OWNER_ID = "6354291932" # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "Shanks"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://infotel:infotel666@database-1.cku9h92xjemg.ap-south-1.rds.amazonaws.com:5431t/dbname'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
