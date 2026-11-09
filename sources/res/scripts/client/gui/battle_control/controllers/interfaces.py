# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/interfaces.py


class IBattleController(object):
    __slots__ = ()

    def startControl(self, *args):
        raise NotImplementedError

    def stopControl(self):
        raise NotImplementedError

    def getControllerID(self):
        raise NotImplementedError


class IBattleControllersRepository(object):
    __slots__ = ()

    @classmethod
    def create(cls, setup):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError

    def getController(self, ctrlID):
        raise NotImplementedError

    def addController(self, ctrl):
        raise NotImplementedError
