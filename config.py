from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "5888890044:AAHPxrsoU-IvZuBhdN1G2DQDjN0xnzAhbnk")
API_ID = int(getenv("API_ID", "26363266"))
API_HASH = getenv("API_HASH", "f7efe49e1daeccc0ff64da9004e3c517")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900999999999999999999999"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Music:Music@cluster0.f9x4i.mongodb.net/Cluster0?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5548606006").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5548606006").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001801920807"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "TRX-MUSIC")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/CuteXdBacha/TRXXXZZ"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


if str(getenv("STRING_SESSION1", "BQAcTl8Cm3rgmtolusr54dyLdqWar8hHJhqQOd1FQgGm7C0bUclqtD8ouU-S-RFN0xmmEaBSdx11iHzyBj4VH5V4lu7FZk7e0qJ6T7rVQLTT0nhbGsCF1CwsHIFogmbgFCl2di7Ag8TW2CGWrIHwRlBZoxlXissKqhNuy2WnhzHJNOUnFQVTAfSIR9zS1vZdwMqwW15U-ql2RTUwXTaS0jYozlr1sL-WJhuHkHa_auDYOTKWCjDWle82rMSxpBi4VQfAdWimWORUsR2MvmpDhhk8O__cqaoT3bkcNSgelWgnaInikJmZEUUoOrt55Y7dww8MS7-4LE6n16XPbPTtBqolAAAAAWHNMOIA")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
