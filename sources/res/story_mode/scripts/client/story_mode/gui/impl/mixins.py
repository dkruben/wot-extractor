# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/mixins.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/mixins.py
from __future__ import absolute_import
from PlayerEvents import g_playerEvents

class DestroyWindowOnDisconnectMixin(object):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super(DestroyWindowOnDisconnectMixin, self).__init__(*args, **kwargs)
        g_playerEvents.onDisconnected += self.__disconnectHandler

    def _finalize(self):
        g_playerEvents.onDisconnected -= self.__disconnectHandler
        super(DestroyWindowOnDisconnectMixin, self)._finalize()

    def __disconnectHandler(self):
        self.destroy()
