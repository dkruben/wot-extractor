# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/shared/promo.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/shared/promo.py


class IPromoLogger(object):

    def logAction(self, **kwargs):
        raise NotImplementedError

    def logTeaserAction(self, teaserData, **kwargs):
        raise NotImplementedError

    def getLoggingFuture(self, teaserData=None, **kwargs):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError
