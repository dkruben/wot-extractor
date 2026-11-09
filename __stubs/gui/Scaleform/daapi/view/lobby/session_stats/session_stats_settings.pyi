# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/session_stats/session_stats_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
from account_helpers.settings_core.settings_constants import SESSION_STATS as SESSION_STATS
from gui.Scaleform.daapi.view.lobby.session_stats.session_stats_settings_controller import SessionStatsSettingsController as SessionStatsSettingsController, MAX_STATS as MAX_STATS
from gui.Scaleform.daapi.view.lobby.session_stats.shared import toIntegral as toIntegral
from gui.Scaleform.daapi.view.meta.SessionStatsSettingsMeta import SessionStatsSettingsMeta as SessionStatsSettingsMeta
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip
_EFFICIENCY_BLOCK: dict
_COMMON_BLOCK: dict
_ECONOMIC_BLOCK_VIEW: dict

class SessionStatsSettings(SessionStatsSettingsMeta):
    __sessionStatsSettings: Any
    __currentSettings: Any
    onShowStats: Any
    __lastChangedIdentifier: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def onClickResetBtn(self):
        ...
    def onClickApplyBtn(self):
        ...
    def onClickBackBtn(self):
        ...
    def onSettingsInputChanged(self, identifier, value):
        ...
    def __setSettings(self):
        ...
    def __getHeader(self):
        ...
    def __getCommonBlocks(self):
        ...
    def __getEconomicsBlock(self):
        ...
    def __getBattlesBlock(self):
        ...
    def __getControlsData(self):
        ...
    def __setBattleSettingsStatus(self):
        ...
