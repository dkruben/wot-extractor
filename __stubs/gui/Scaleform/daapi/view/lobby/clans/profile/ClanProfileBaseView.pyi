# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/ClanProfileBaseView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from gui import SystemMessages as SystemMessages
from gui.Scaleform.daapi.view.meta.ClanProfileBaseViewMeta import ClanProfileBaseViewMeta as ClanProfileBaseViewMeta
from gui.Scaleform.locale.CLANS import CLANS as CLANS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.clans import formatters as clans_fmts
from gui.clans.clan_helpers import ClanListener as ClanListener
from gui.clans.data_wrapper.utils import formatField as formatField
from gui.clans.settings import CLIENT_CLAN_RESTRICTIONS as RES
from gui.impl import backport as backport
from gui.shared.formatters import text_styles as text_styles
from gui.shared.view_helpers.emblems import ClanEmblemsHelper as ClanEmblemsHelper
from gui.wgcg.base.contexts import CreateApplicationCtx as CreateApplicationCtx
from helpers import i18n as i18n
_JOIN_BTN_ACTION_ID = 'join'

class ClanProfileBaseView(ClanProfileBaseViewMeta, ClanEmblemsHelper, ClanListener):
    _clanDossier: Any
    __headerBtnStates: Any
    _dummyMustBeShown: Any
    def __init__(self):
        ...
    def setClanDossier(self, clanDossier):
        ...
    def onHeaderButtonClick(self, actionId):
        ...
    def onClanEmblem128x128Received(self, clanDbID, emblem):
        ...
    def _populate(self):
        ...
    def onClanEnableChanged(self, enabled):
        ...
    def onAccountWebVitalInfoChanged(self, fieldName, value):
        ...
    def onClanWebVitalInfoChanged(self, clanDbID, fieldName, value):
        ...
    def _dispose(self):
        ...
    # decorador original: @adisp_process
    def _sendApplication(self):
        ...
    def _onAppSuccessfullySent(self):
        ...
    def _updateClanInfo(self, clanInfo):
        ...
    def _updateClanEmblem(self, clanDbID):
        ...
    def _updateHeaderState(self):
        ...
    def _getHeaderButtonStateVO(self, actionBtnVisible=False, actionBtnLabel=None, iconBtnVisible=False, topTFVisible=False, middleTFVisible=False, actionId=None, actionBtnTooltip=None, middleTF=None, topTF=None):
        ...
    def _initHeaderBtnStates(self):
        ...
    def _showWaiting(self):
        ...
    def _hideWaiting(self):
        ...
    def _updateDummy(self):
        ...
