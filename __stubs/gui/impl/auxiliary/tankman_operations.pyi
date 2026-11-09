# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/auxiliary/tankman_operations.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import typing as typing
from builtins import range as range
from future.utils import iteritems as iteritems
from typing import TYPE_CHECKING as TYPE_CHECKING
from frameworks.wulf import Array as Array
from gui.customization.shared import getPurchaseMoneyState as getPurchaseMoneyState, isTransactionValid as isTransactionValid, MoneyForPurchase as MoneyForPurchase
from gui.goodies import IGoodiesCache as IGoodiesCache
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import TooltipType as TooltipType
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyType as CurrencyType, CurrencySize as CurrencySize
from gui.impl.gen.view_models.views.lobby.crew.common.crew_skill_model import CrewSkillModel as CrewSkillModel
from gui.impl.gen.view_models.views.lobby.crew.common.dynamic_tooltip_model import DynamicTooltipModel as DynamicTooltipModel
from gui.impl.gen.view_models.views.lobby.crew.crew_constants import CrewConstants as CrewConstants
from gui.impl.gen.view_models.views.lobby.crew.dialogs.dialog_tankman_model import DialogTankmanModel as DialogTankmanModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.price_card_model import PriceCardModel as PriceCardModel, CardType as CardType, CardState as CardState
from gui.impl.lobby.crew.crew_helpers.skill_model_setup import skillModelSetup as skillModelSetup
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.money import Currency as Currency, Money as Money, MONEY_ZERO_CREDITS as MONEY_ZERO_CREDITS, MONEY_ZERO_GOLD as MONEY_ZERO_GOLD
from helpers import dependency as dependency
from items.tankmen import TankmanDescr as TankmanDescr, MAX_SKILL_LEVEL as MAX_SKILL_LEVEL, MAX_SKILLS_EFFICIENCY as MAX_SKILLS_EFFICIENCY
import Settings as Settings
from gui.impl.gen.view_models.views.lobby.crew.common.crew_skill_list_model import CrewSkillListModel as CrewSkillListModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.dialog_tankman_base_model import DialogTankmanBaseModel as DialogTankmanBaseModel
from gui.shared.gui_items import Tankman as Tankman
from gui.shared.gui_items.tankman_skill import TankmanSkill as TankmanSkill
_DEFAULT_TITLE_LOC = R.strings.dialogs.priceCard
_RESET_LOC = R.strings.dialogs.perksReset.priceCard
_RETRAIN_LOC = R.strings.dialogs.retrain.priceCard
_IMAGE = R.images.gui.maps.icons.common.components.price_card
_LEVEL_TO_HIGHLIGHT = 100
_MINIMUM_TO_HIGHLIGHT = 1
FREE = 'free'
MONEY_FREE: Any
ITEM_PRICE_FREE: Any

def _toPercents(value):
    ...
def getPriceData(itemPrice, rIconPath, rTitlePath, isFreeReset):
    ...
def getOperationCardState(itemPrice):
    ...
def getPriceDescriptionData(itemPrice, value, descLoc, isHighlight=False, **kwargs):
    ...
def getSkillResetPriceDescriptionData(itemPrice, xpReuseFractionPerc, descLoc, isHighlight=False, **kwargs):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def packRecertificationForm(wulfList, goodiesCache=None, isFreeReset=False):
    ...
def packPriceList(wulfList, priceData, packCustomValues=None, rIconPath=..., rTitlePath=...):
    ...
def packPriceCard(priceDataItem, packCustomValues=None, rIconPath=..., rTitlePath=...):
    ...
def packPrice(priceModel, priceDataItem, rIconPath=..., rTitlePath=...):
    ...
def packSkillResetPrice(priceModel, priceDataItem, rIconPath=..., rTitlePath=...):
    ...
def packTooltipModel(model, data):
    ...
def getUserPrefsDropSkills():
    ...
def setUserPrefsDropSkills(val):
    ...
def packSkillReset(wulfList, priceData):
    ...
def packSkillResetPriceCard(priceDataItem, rIconPath=..., rTitlePath=...):
    ...
def packSkillResetCustomValues(cardVM, customData):
    ...
def packBaseTankman(vmTankman, tankman):
    ...
def packRetrainTankman(vmTankman, tankman, skillEfficiency=None):
    ...
def packSkills(skillsData, tankman, skillEfficiency=None):
    ...
def packMajorSkills(skillsData, tankman, customGetters=None):
    ...
def packBonusSkills(skillsData, tankman):
    ...
def getSkillModel(tman, skill, role, customGetters=None):
    ...
def getNewSkillModel(level=...):
    ...
def packMassRetrain(wulfList, priceData):
    ...
def packSingleRetrain(wulfList, priceData):
    ...
