# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/blueprints/blueprints_conversion_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
import nations as nations
from blueprints.BlueprintTypes import BlueprintTypes as BlueprintTypes
from frameworks.wulf import ViewSettings as ViewSettings, Array as Array
from gui import SystemMessages as SystemMessages
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_balance_content_model import BlueprintBalanceContentModel as BlueprintBalanceContentModel
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_convert_model import BlueprintConvertModel as BlueprintConvertModel
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_price import BlueprintPrice as BlueprintPrice
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_screen_tooltips import BlueprintScreenTooltips as BlueprintScreenTooltips
from gui.impl.gen.view_models.views.lobby.blueprints.fragment_item_model import FragmentItemModel as FragmentItemModel
from gui.impl.lobby.blueprints import getBlueprintTooltipData as getBlueprintTooltipData
from gui.impl.lobby.blueprints.blueprints_alliance_tooltip_view import BlueprintsAllianceTooltipView as BlueprintsAllianceTooltipView
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogView as FullScreenDialogView
from gui.shared import event_dispatcher as event_dispatcher, sound_helpers as sound_helpers
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.shared.utils.requesters.blueprints_requester import getNationalFragmentCD as getNationalFragmentCD

class BlueprintsConversionView(FullScreenDialogView):
    __vehicle: Any
    __fragmentsCount: Any
    __allyFragmentsBalance: Any
    def __init__(self, vehicleCD, fragmentsCount):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createToolTip(self, event):
        ...
    def _initialize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onSelectItem(self, args=None):
        ...
    def __onSliderShift(self, args=None):
        ...
    def _getAdditionalData(self):
        ...
    def __setUsedFragmentsPrice(self, mainPriceModel, usedAdditionalPrice):
        ...
    def __setNationalPriceOptions(self, optionsArray):
        ...
    def __setBalanceBlock(self, fragmentsBalance):
        ...
    def __updateBallanceBlock(self, fragmentsBallance):
        ...
    def __updateNotEnoughFields(self, priceOptions, usedPrices):
        ...
    def __onBlueprintsSettingsChanged(self, _):
        ...
    def __onBlueprintsModeChanged(self, _):
        ...
    def __onBlueprintsBalanceChanged(self, *_):
        ...
    def __updateBlocks(self):
        ...
    def __triggerSyncInitiator(self, model):
        ...
    @property
    def __blueprints(self):
        ...
    def __getInitialNationalUsageCounts(self):
        ...
