# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileTabNavigator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection as ProfileSection
from gui.Scaleform.daapi.view.meta.ProfileTabNavigatorMeta import ProfileTabNavigatorMeta as ProfileTabNavigatorMeta
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.impl.lobby.achievements.achievements_main_view import AchievementsViewCtx as AchievementsViewCtx
from gui.shared import events as events, g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE

class ProfileTabNavigator(ProfileTabNavigatorMeta):
    gf_views_map: list
    __userName: Any
    __userID: Any
    __databaseID: Any
    __navigatorOwnInitInfo: Any
    __selectedData: Any
    tabId: Any
    def __init__(self, *args):
        ...
    def invokeUpdate(self):
        ...
    def _populate(self):
        ...
    def registerFlashComponent(self, component, alias, *args):
        ...
    def onTabChange(self, tabId):
        ...
    def onViewReady(self, alias):
        ...
    @staticmethod
    def __safeCall(obj, attrName, *args, **kwargs):
        ...
