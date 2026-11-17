# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/overview_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import json as json
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport.backport_tooltip import createBackportTooltipContent as createBackportTooltipContent
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.gen.view_models.views.lobby.loadout.crew.slot_model import SlotModel as SlotModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleMechanicsArray as fillVehicleMechanicsArray
from gui.impl.lobby.vehicle_hub.sub_presenters.sub_presenter_base import SubPresenterBase as SubPresenterBase
from gui.shared.event_dispatcher import showVehicleHubMechanicsVideo as showVehicleHubMechanicsVideo
from gui.shared.gui_items.Tankman import NO_TANKMAN as NO_TANKMAN
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.overview_model import OverviewModel as OverviewModel, BenefitsEnum as BenefitsEnum

class OverviewSubPresenter(SubPresenterBase):
    @property
    def viewModel(self):
        ...
    def setVehicleHubCtx(self, vhCtx):
        ...
    def initialize(self, vhCtx, *args, **kwargs):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def __updateModel(self):
        ...
    def __updateVehicleMechanics(self, model=None):
        ...
    def __updateCrewMembers(self, model=None):
        ...
    def __getBenefits(self):
        ...
    # decorador original: @args2params(...)
    def __onShowSpecialMechanicsVideo(self, mechanicsName):
        ...
