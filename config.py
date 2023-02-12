from os import getenv

class Config(object):
      API_HASH = getenv("67a71560b00a31ffa692c67428f06d38")
      API_ID = int(getenv("8130624", 0))
      AS_COPY = True if getenv("AS_COPY", False) == "True" else False
      BOT_TOKEN = getenv("5828767366:AAFNC-KQuI09agabSLGhjUa369Nx7PAw49c", "")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "").replace("\n", " ").split(' '))
