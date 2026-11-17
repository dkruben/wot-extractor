# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/ClanProfileMainWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from gui.Scaleform.daapi.view.lobby.clans.clan_profile_event import ClanProfileEvent as ClanProfileEvent
from gui.clans.clan_helpers import ClanListener as ClanListener
from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileBaseView import ClanProfileBaseView as ClanProfileBaseView
from gui.Scaleform.daapi.view.meta.ClanProfileMainWindowMeta import ClanProfileMainWindowMeta as ClanProfileMainWindowMeta
from gui.Scaleform.genConsts.CLANS_ALIASES import CLANS_ALIASES as CLANS_ALIASES
from gui.Scaleform.locale.CLANS import CLANS as CLANS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import i18n as i18n, dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class ClanProfileMainWindow(ClanProfileMainWindowMeta, ClanListener):
    _lobbyContext: Any
    __clanDBID: Any
    __clanDossier: Any
    __clanAbbrev: Any
    def __init__(self, ctx):
        ...
    def onWindowClose(self):
        ...
    def getClanDossier(self):
        ...
    def onClanEnableChanged(self, enabled):
        ...
    def _populate(self):
        ...
    def _updateData(self):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    def _dispose(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def __closeClanProfileHandler(self, _):
        ...
