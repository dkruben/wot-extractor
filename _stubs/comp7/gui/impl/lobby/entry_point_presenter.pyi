# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/entry_point_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import COMP7_UI_SECTION as COMP7_UI_SECTION, COMP7_UMG_PROGRESSION_POINTS_SEEN as COMP7_UMG_PROGRESSION_POINTS_SEEN
from comp7.gui.impl.gen.view_models.views.lobby.entry_point_model import EntryPointModel as EntryPointModel
from comp7.gui.impl.lobby.comp7_helpers import comp7_model_helpers as comp7_model_helpers, comp7_shared as comp7_shared, comp7_qualification_helpers as comp7_qualification_helpers, account_settings as account_settings
from comp7.gui.impl.lobby.tooltips.progression_tooltip import ProgressionTooltip as ProgressionTooltip
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_model_helpers import getSeasonNameEnum as getSeasonNameEnum
from comp7.gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import Comp7OverlapCtrlMixin as Comp7OverlapCtrlMixin
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7.gui.shared.event_dispatcher import showComp7MetaRootTab as showComp7MetaRootTab
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin

# base nao representavel no stub: ViewComponent[...]
class EntryPointPresenter(TooltipPositionerMixin, Comp7OverlapCtrlMixin, IGlobalListener):
    __comp7Controller: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _updateViewModel(self, *_, **__):
        ...
    def __updateRating(self, *_, **__):
        ...
    def _rawUpdate(self):
        ...
    def __updateQualificationData(self, model):
        ...
    def __updateProgressionData(self, model):
        ...
    def _getEvents(self):
        ...
    @staticmethod
    def __onOpenMetaClick():
        ...
    def __onAnimationEnd(self):
        ...
    def __onEntryPointAnimationSeen(self):
        ...
    @staticmethod
    def setUmgProgressionPointsSeen(curPoints):
        ...
    @staticmethod
    def getPrevUmgProgressionPointsSeen():
        ...
