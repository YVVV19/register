from . import Config


def migrate():
    Config.down()
    Config.up()