name = "maya"
version = "2019"
build_command = False

tools = [
    "designer",
    "fcheck",
    "imconvert",
    "imgcvt",
    "lconvert",
    "maya",
    "mayabatch",
    "mayapy",
    "pyside2-rcc",
    "rcc",
    "shiboken2",
    "uconv",
    "uic",
]


def commands():
    env.PATH.append('{root}')  # noqa
    env.PATH.append('D:/Program_Files/Maya2019.2/bin')  # noqa
    env.PYTHONPATH.append('D:/Program_Files/Maya2019.2/Python/Lib/site-packages')  # noqa
    env.QT_PLUGIN_PATH.append("D:/Program_Files/Maya2019.2/qt-plugins")  # noqa
    env.PATH.append("D:/Program_Files/Maya2019.2/devkit")  # noqa
    env.PATH.append("D:/Program_Files/Maya2019.2/include")  # noqa
