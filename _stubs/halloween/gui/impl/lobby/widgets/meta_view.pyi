# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/widgets/meta_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from adisp import adisp_process as adisp_process
from frameworks.wulf import ViewEvent as ViewEvent, WindowLayer as WindowLayer
from gui.impl.backport import createTooltipData as createTooltipData, BackportTooltipWindow as BackportTooltipWindow
from gui.impl.common.fade_manager import UseFading as UseFading
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from halloween.gui.impl.gen.view_models.views.lobby.widgets.meta_view_model import MetaViewModel as MetaViewModel
from halloween.gui.impl.lobby.hw_helpers import getArtefactState as getArtefactState, fillProminentBonus as fillProminentBonus, PROMINENT_REWARD_TOOLTIP_ID as PROMINENT_REWARD_TOOLTIP_ID
from halloween.gui.impl.lobby.tooltips.event_mission_tooltip import MissionsTooltip as MissionsTooltip
from halloween.gui.impl.lobby.tooltips.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from halloween.gui.impl.lobby.tooltips.vehicle_tooltip import VehicleTooltipView as VehicleTooltipView
from halloween.gui.shared.event_dispatcher import showDecryptWindowView as showDecryptWindowView, showBundleWindow as showBundleWindow
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.uilogging.loggers import HWMetricsLogger as HWMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys
from helpers import dependency as dependency
from halloween.gui.game_control.halloween_artefacts_controller import Artefact as Artefact
from frameworks.wulf import View as View
_R_BACKPORT_TOOLTIP: Any

# base nao representavel no stub: ViewComponent[...]
class MetaWidgetView(TooltipPositionerMixin):
    _hwArtifactsCtrl: Any
    __artefactID: Any
    __parent: Any
    __prominentBonus: Any
    __uiLogger: Any
    def __init__(self, parent=None):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    def updateData(self, selectedArtefactIndex):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onKeyUpdated(self):
        ...
    def __onSlideToNext(self):
        ...
    # decorador original: @UseFading(...)
    def __onView(self):
        ...
    def __onSkip(self):
        ...
    # decorador original: @adisp_process
    def __skipArtefact(self):
        ...
    def __onDecrypt(self):
        ...
    # decorador original: @adisp_process
    def __decryptArtefact(self):
        ...
