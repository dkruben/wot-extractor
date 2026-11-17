# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_post_progression/dialogs/research_confirm.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.common.base_sub_model_view import BaseSubModelView as BaseSubModelView
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.bonus_model import BonusModel as BonusModel
from gui.impl.gen.view_models.common.bonus_value_model import BonusValueModel as BonusValueModel
from gui.impl.gen.view_models.views.lobby.post_progression.dialogs.research_steps_dialog import ResearchStepsDialog as ResearchStepsDialog
from gui.impl.gen.view_models.views.lobby.post_progression.dialogs.short_modification_model import ShortModificationModel as ShortModificationModel, ModificationType as ModificationType
from gui.impl.gen.view_models.views.lobby.post_progression.dialogs.short_step_model import ShortStepModel as ShortStepModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogView as FullScreenDialogView
from gui.impl.wrappers.user_compound_price_model import BuyPriceModelBuilder as BuyPriceModelBuilder
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_parameters.functions import aggregateKpi as aggregateKpi
from gui.veh_post_progression.models.ext_money import EXT_MONEY_ZERO as EXT_MONEY_ZERO, getFullXPFromXPPrice as getFullXPFromXPPrice, ExtendedCurrency as ExtendedCurrency
from gui.veh_post_progression.models.purchase import PurchaseProvider as PurchaseProvider
from post_progression_common import ACTION_TYPES as ACTION_TYPES
_logger: Any
_ACTION_TYPE_TO_MODIFICATION_TYPE: dict

# base nao representavel no stub: FullScreenDialogView[...]
class PostProgressionResearchConfirm:
    _buyContent: Any
    _mainContent: Any
    __vehicle: Any
    __stepIDs: Any
    __price: Any
    __steps: Any
    __xpBalance: Any
    __postProgression: Any
    def __init__(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onInventoryResync(self, reason, diff):
        ...
    def __updateData(self):
        ...

class PostProgressionResearchBottomContent(BaseSubModelView):
    def onLoading(self, price, balance, vehicle):
        ...
    def update(self, price, balance, vehicle):
        ...

class PostProgressionResearchMainContent(BaseSubModelView):
    def onLoading(self, steps, postProgression):
        ...
    def update(self, steps, postProgression):
        ...
    def __fillStepModel(self, step):
        ...
    def __fillBonusesArray(self, bonusesArray, kpiList):
        ...
    def __fillModificationModel(self, step):
        ...

def convertPrice(mayConsume, balance, price):
    ...
