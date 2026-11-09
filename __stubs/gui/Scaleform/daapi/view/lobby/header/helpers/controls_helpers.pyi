# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/header/helpers/controls_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from gui.Scaleform.daapi.view.lobby.header.helpers.fight_btn_tooltips import getEventTooltipData as getEventTooltipData, getMapboxFightBtnTooltipData as getMapboxFightBtnTooltipData, getMapsTrainingTooltipData as getMapsTrainingTooltipData, getRandomTooltipData as getRandomTooltipData, getRankedFightBtnTooltipData as getRankedFightBtnTooltipData
from gui.impl.gen import R as R
from gui.impl.lobby.page.lobby_footer import LobbyFooter as LobbyFooter
from gui.impl.lobby.page.lobby_header import LobbyHeader as LobbyHeader
from gui.shared.system_factory import collectDynamicLobbyHeaderTypes as collectDynamicLobbyHeaderTypes
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.impl.pub.view_component import ViewComponent as ViewComponent

class ILobbyHeaderControlsHelper(object):
    __slots__: tuple
    @classmethod
    def isEventSquadEnable(cls):
        ...
    @classmethod
    def getFightControlTooltipData(cls, prbValidation, isInSquad, isFightBtnDisabled, isNavigationEnabled):
        ...
    @classmethod
    def getSquadControlTooltipData(cls, prbValidation, isInSquad):
        ...
    @classmethod
    def getHeaderType(cls):
        ...
    @classmethod
    def getFooterType(cls):
        ...

class EmptyLobbyHeaderFooterHelper(ILobbyHeaderControlsHelper):
    __slots__: tuple
    @classmethod
    def getFightControlTooltipData(cls, prbValidation, isInSquad, isFightBtnDisabled, isNavigationEnabled):
        ...
    @classmethod
    def getSquadControlTooltipData(cls, prbValidation, isInSquad):
        ...
    @classmethod
    def getHeaderType(cls):
        ...
    @classmethod
    def getFooterType(cls):
        ...

class DefaultLobbyHeaderHelper(ILobbyHeaderControlsHelper):
    __slots__: tuple
    _IN_SQUAD_TOOLTIP_KEY = 'inSquad'
    _OUT_SQUAD_TOOLTIP_KEY = 'squad'
    @classmethod
    def getSquadControlTooltipData(cls, prbValidation, isInSquad):
        ...
    @classmethod
    def getFightControlTooltipData(cls, prbValidation, isInSquad, isFightBtnDisabled, isNavigationEnabled):
        ...
    @classmethod
    def getHeaderType(cls):
        ...
    @classmethod
    def getFooterType(cls):
        ...
    @classmethod
    def _getCommonFightTooltipData(cls, _, __):
        ...
    @classmethod
    def _getDisabledFightTooltipData(cls, prbValidation, isInSquad):
        ...
    @classmethod
    def _getInSquadTooltipData(cls, _):
        ...
    @classmethod
    def _getOutSquadTooltipData(cls, prbValidation):
        ...
    @classmethod
    def _getLobbyHeaderSuitableTypes(cls):
        ...

class RankedLobbyHeaderHelper(DefaultLobbyHeaderHelper):
    __slots__: tuple
    _IN_SQUAD_TOOLTIP_KEY = 'rankedSquad'
    _OUT_SQUAD_TOOLTIP_KEY = 'rankedSquad'
    @classmethod
    def _getDisabledFightTooltipData(cls, prbValidation, isInSquad):
        ...

class MapboxLobbyHeaderHelper(DefaultLobbyHeaderHelper):
    __slots__: tuple
    _IN_SQUAD_TOOLTIP_KEY = 'inMapboxSquad'
    _OUT_SQUAD_TOOLTIP_KEY = 'mapboxSquad'
    @classmethod
    def _getDisabledFightTooltipData(cls, prbValidation, isInSquad):
        ...

class MapsTrainingLobbyHeaderHelper(DefaultLobbyHeaderHelper):
    __slots__: tuple
    @classmethod
    def _getDisabledFightTooltipData(cls, prbValidation, isInSquad):
        ...

class EventLobbyHeaderHelper(DefaultLobbyHeaderHelper):
    __slots__: tuple
    _OUT_SQUAD_TOOLTIP_KEY = 'eventSquad'
    __bonusType: Any
    __bonusCapsOverrides: Any
    def __init__(self, bonusType, bonusCapsOverrides):
        ...
    def isEventSquadEnable(self):
        ...
    @classmethod
    def _getDisabledFightTooltipData(cls, prbValidation, isInSquad):
        ...
