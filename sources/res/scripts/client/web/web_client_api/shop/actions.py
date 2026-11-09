# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/shop/actions.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/shop/actions.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.store.actions_formatters import getAllActionsInfoIterator
from helpers import dependency
from web.web_client_api import w2c, W2CSchema
from skeletons.gui.server_events import IEventsCache
from web.web_client_api.shop import formatters

def _filterActions(act):
    return act.isAvailable().isValid


class ActionsWebApiMixin(object):
    eventsCache = dependency.descriptor(IEventsCache)

    @w2c(W2CSchema, 'get_actions')
    def getActions(self, _):
        actions = self.eventsCache.getActions(filterFunc=_filterActions).values()
        entities = self.eventsCache.getActionEntities()
        actionsInfo = getAllActionsInfoIterator(actions, entities) if actions else []
        fmt = formatters.makeActionFormatter().format
        return [fmt(actionInfo) for actionInfo in actionsInfo]
