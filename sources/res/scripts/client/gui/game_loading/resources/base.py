# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_loading/resources/base.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/resources/base.py
import typing
from gui.game_loading import loggers
if typing.TYPE_CHECKING:
    from gui.game_loading.resources.models import BaseResourceModel
_logger = loggers.getResourcesLogger()

class BaseResources(object):
    __slots__ = ()

    def destroy(self, *args, **kwargs):
        self.onDisconnected()
        _logger.debug('%s destroyed.', self)

    def onConnected(self, *args, **kwargs):
        _logger.debug('%s on connected called.', self)

    def onDisconnected(self, *args, **kwargs):
        _logger.debug('%s on disconnected called.', self)

    def reset(self, *args, **kwargs):
        _logger.debug('%s restarted.', self)

    def get(self, *args, **kwargs):
        raise NotImplementedError

    def __repr__(self):
        return ('<Resources:{}>').format(self.__class__.__name__)
