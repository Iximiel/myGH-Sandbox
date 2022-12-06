from myghsandbox import getVersion, __version__


def test_Version():
    assert __version__ == getVersion()


def test_NotVersion():
    assert __version__ != "v0"
