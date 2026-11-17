# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileSummaryWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl import backport as backport
from gui.shared import event_dispatcher as shared_events
from helpers.i18n import makeString as _ms
from gui.clans.clan_helpers import ClanListener as ClanListener
from gui.clans.formatters import getClanRoleString as getClanRoleString
from gui.clans.clan_cache import ClanInfo as ClanInfo
from gui.shared.formatters import text_styles as text_styles
from gui.shared.view_helpers.emblems import ClanEmblemsHelper as ClanEmblemsHelper
from gui.Scaleform.daapi.view.meta.ProfileSummaryWindowMeta import ProfileSummaryWindowMeta as ProfileSummaryWindowMeta
from gui.Scaleform.locale.PROFILE import PROFILE as PROFILE

class ProfileSummaryWindow(ProfileSummaryWindowMeta, ClanEmblemsHelper, ClanListener):
    __rating: Any
    def __init__(self, *args):
        ...
    def getGlobalRating(self, databaseID):
        ...
    def openClanStatistic(self):
        ...
    def onClanEmblem32x32Received(self, clanDbID, emblem):
        ...
    def onClanEnableChanged(self, enabled):
        ...
    def onAccountClanProfileChanged(self, profile):
        ...
    def onAccountClanInfoReceived(self, info):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _requestClanInfo(self):
        ...
    # decorador original: @adisp_process
    def _receiveRating(self, databaseID):
        ...
    def _getClanBtnParams(self, isVisible):
        ...
