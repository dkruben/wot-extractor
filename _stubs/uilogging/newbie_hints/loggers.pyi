# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/newbie_hints/loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
import BigWorld as BigWorld
from helpers import dependency as dependency
from wotdecorators import noexcept as noexcept
from uilogging.constants import DEFAULT_LOGGER_NAME as DEFAULT_LOGGER_NAME
from uilogging.base.logger import MetricsLogger as MetricsLogger, ifUILoggingEnabled as ifUILoggingEnabled
from uilogging.newbie_hints.constants import NewbieHintsLogActions as NewbieHintsLogActions, CheckBoxState as CheckBoxState, SettingsNewbieTooltips as SettingsNewbieTooltips, NewbieHintsLogItems as NewbieHintsLogItems, NewbieHintsLogViews as NewbieHintsLogViews, FEATURE_NEWBIE_HINTS as FEATURE_NEWBIE_HINTS, FEATURE_NEWBIE_HINTS_SETTINGS as FEATURE_NEWBIE_HINTS_SETTINGS, TOOLTIP_ID_MAPPING as TOOLTIP_ID_MAPPING, SETTINGS_CHECKBOX_KEYS_MAPPING as SETTINGS_CHECKBOX_KEYS_MAPPING, TOOLTIP_MIN_VIEW_TIME as TOOLTIP_MIN_VIEW_TIME, NEWBIE_SETTINGS_RETICLE_PARAMS as NEWBIE_SETTINGS_RETICLE_PARAMS, NEWBIE_HINTS_RETICLE_MAPPING as NEWBIE_HINTS_RETICLE_MAPPING
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from account_helpers.settings_core.settings_constants import GAME as GAME, AIM as AIM
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from hints.battle.schemas.newbie import NewbieClientHintModel as NewbieClientHintModel
from gui.battle_control.controllers.battle_hints.queues import BattleHint as BattleHint
from gui.Scaleform.framework.tooltip_mgr import ToolTip as ToolTip
_logger: Any

class NewbieHintsSettingsUILogger(MetricsLogger):
    __slots__: tuple
    settingsCore: Any
    def __init__(self):
        ...
    def resetButtonClicked(self):
        ...
    # decorador original: @noexcept
    # decorador original: @ifUILoggingEnabled(...)
    def onSettingsChanged(self, diff):
        ...

class NewbieHintsSettingsTooltipsUILogger(MetricsLogger):
    __slots__: tuple
    appLoader: Any
    _currentTooltip: Any
    def __init__(self):
        ...
    @property
    def tooltipMgr(self):
        ...
    def initialize(self):
        ...
    def finalize(self):
        ...
    # decorador original: @noexcept
    # decorador original: @ifUILoggingEnabled(...)
    def _onShowTooltip(self, tooltipID, args, _):
        ...
    # decorador original: @noexcept
    def _onHideTooltip(self, _):
        ...

class NewbieHintsShownUILogger(MetricsLogger):
    __slots__: tuple
    _hint: Any
    def __init__(self):
        ...
    def initialize(self):
        ...
    def finalize(self):
        ...
    # decorador original: @noexcept
    # decorador original: @ifUILoggingEnabled(...)
    def _onHintShown(self, battleHint):
        ...
    # decorador original: @noexcept
    def _onHintHide(self, battleHint):
        ...
