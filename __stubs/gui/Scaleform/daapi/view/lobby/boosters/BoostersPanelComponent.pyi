# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/boosters/BoostersPanelComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.meta.SlotsPanelMeta import SlotsPanelMeta as SlotsPanelMeta
from gui.Scaleform.genConsts.BOOSTER_CONSTANTS import BOOSTER_CONSTANTS as BOOSTER_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.goodies.goodie_items import MAX_ACTIVE_BOOSTERS_COUNT as MAX_ACTIVE_BOOSTERS_COUNT
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.game_control import IBoostersController as IBoostersController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
_GUI_SLOTS_PROPS: dict
ADD_BOOSTER_ID = 'add'
_ADD_AVAILABLE_BOOSTER_ID = 'addAvailable'
_EMPTY_BOOSTER_ID = 'empty'

class BoostersPanelComponent(SlotsPanelMeta):
    boosters: Any
    goodiesCache: Any
    _isPanelInactive: Any
    _wasPopulated: Any
    _slotsMap: Any
    _slotProps: Any
    def __init__(self):
        ...
    def setSettings(self, isPanelInactive=True):
        ...
    def setSlotProps(self, slotProps):
        ...
    def getBoosterSlotID(self, idx):
        ...
    def getSlotTooltipBody(self, orderID):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __getAvailableBoosters(self):
        ...
    def _buildList(self):
        ...
    def getEmptySlotParams(self, idx, addAndActiveBoostersCount):
        ...
    def __makeBoosterVO(self, idx, booster):
        ...
    def __makeEmptyBoosterVO(self, idx, slotLinkage, icon):
        ...
    def __onUpdateGoodies(self, *args):
        ...
