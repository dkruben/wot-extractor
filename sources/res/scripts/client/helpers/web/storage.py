# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/web/storage.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/web/storage.py


class IStorage(object):

    def close(self):
        raise NotImplementedError

    def add(self, name, data, callback):
        raise NotImplementedError

    def remove(self, name):
        raise NotImplementedError

    def isStored(self, name):
        raise NotImplementedError

    def getAll(self):
        raise NotImplementedError
