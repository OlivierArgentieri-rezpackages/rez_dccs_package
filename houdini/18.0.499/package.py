name = "houdini"
version = "18.0.499"

tools = [
    "pyside2-rcc",
    "rcc",
    "uic",
    "hbatch",
    "houdinifx",
    "hrender",
    "hscript",
    "hython"
]


def commands():
    env.PATH.append('{root}')  # noqa
    env.PATH.append('F:/Program_Files/Houdini_18.0.499/bin')  # noqa
    env.PYTHONPATH.append('F:/Program_Files/Houdini_18.0.499/python27/lib/site-packages')  # noqa
    env.PATH.append("F:/Program_Files/Houdini_18.0.499/python27/lib/site-packages-forced/PySide2")  # noqa
    env.PATH.append("F:/Program_Files/Houdini_18.0.499/toolkit/include")  # noqa
