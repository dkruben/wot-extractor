# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/collection/resources/common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/collection/resources/common.py
import logging
from gui.collection.resources.cdn.cache import CollectionsCdnCacheMgr
from gui.collection.resources.local.cache import CollectionsLocalCacheMgr
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
_logger = logging.getLogger(__name__)

@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def makeCacheMgr(lobbyContext=None):
    settings = lobbyContext.getServerSettings()
    if settings.collectionsConfig.useCdnResourceCache:
        if settings.fileServer.getCollectionsContentConfigUrl():
            return CollectionsCdnCacheMgr()
        _logger.warning('External url not configured yet. The local cache will be used.')
    return CollectionsLocalCacheMgr()
