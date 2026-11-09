# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_external_cache.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_external_cache.py


class IWebExternalCache(object):

    class IStorage(object):

        def get(self, url):
            raise NotImplementedError
