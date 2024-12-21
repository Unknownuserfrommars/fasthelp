class RemovalError(ModuleNotFoundError):
    pass

class err:
    def __init__(self):
        return RemovalError("This module has been removed. This was formerly a bundle of the classes CHelper, JSHelper, JavaHelper, etc.\nHowever, this is no longer the case.")