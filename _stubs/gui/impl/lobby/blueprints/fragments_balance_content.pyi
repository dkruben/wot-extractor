# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/blueprints/fragments_balance_content.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import nations as nations
from blueprints.BlueprintTypes import BlueprintTypes as BlueprintTypes
from frameworks.wulf import ViewSettings as ViewSettings
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_balance_content_model import BlueprintBalanceContentModel as BlueprintBalanceContentModel
from gui.impl.gen.view_models.views.lobby.blueprints.fragment_item_model import FragmentItemModel as FragmentItemModel
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_screen_tooltips import BlueprintScreenTooltips as BlueprintScreenTooltips
from gui.impl.lobby.blueprints.blueprints_alliance_tooltip_view import BlueprintsAllianceTooltipView as BlueprintsAllianceTooltipView
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.backport import createTooltipData as createTooltipData, BackportTooltipWindow as BackportTooltipWindow
from gui.shared.utils.requesters.blueprints_requester import getNationalFragmentCD as getNationalFragmentCD
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
logger: Any

class FragmentsBalanceContent(ViewImpl):
    __itemsCache: Any
    __slots__: tuple
    __vehicle: Any
    def __init__(self, vehicleCD):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onUpdateBlueprints(self, _):
        ...
    def __updateModel(self):
        ...
    def __getFragmentCount(self):
        ...
    def __getTooltipData(self, ttId, fragmentCD):
        ...
