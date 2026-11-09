# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/shared/congrats.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/shared/congrats.py


class ICongratsCtx(object):

    @property
    def background(self):
        raise NotImplementedError

    @property
    def title(self):
        raise NotImplementedError

    @property
    def description(self):
        raise NotImplementedError

    @property
    def image(self):
        raise NotImplementedError

    @property
    def imageAlt(self):
        raise NotImplementedError

    @property
    def confirmLabel(self):
        raise NotImplementedError

    @property
    def backLabel(self):
        raise NotImplementedError

    def onConfirm(self):
        raise NotImplementedError

    def onBack(self):
        raise NotImplementedError
