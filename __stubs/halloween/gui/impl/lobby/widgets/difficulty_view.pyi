# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/widgets/difficulty_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewStatus as ViewStatus
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control import prbEntityProperty as prbEntityProperty
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from account_helpers import AccountSettings as AccountSettings
from halloween.gui.halloween_account_settings import AccountSettingsKeys as AccountSettingsKeys
from halloween.gui.halloween_gui_constants import DifficultyLevel as DifficultyLevel
from halloween.gui.impl.gen.view_models.views.lobby.widgets.difficulty_item_model import DifficultyItemModel as DifficultyItemModel, StateEnum as StateEnum
from halloween.gui.impl.gen.view_models.views.lobby.widgets.difficulty_view_model import DifficultyViewModel as DifficultyViewModel
from halloween.gui.impl.lobby.tooltips.difficulty_tooltip import DifficultyTooltipView as DifficultyTooltipView
from halloween.gui.prb_control.entities.squad.entity import HalloweenSquadEntity as HalloweenSquadEntity
from halloween.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from helpers import dependency as dependency

# base nao representavel no stub: ViewComponent[...]
class DifficultyView(IGlobalListener):
    _difficultyCtrl: Any
    def __init__(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def onUnitPlayerRolesChanged(self, pInfo, pPermissions):
        ...
    def onUnitPlayerAdded(self, pInfo):
        ...
    def onUnitPlayerRemoved(self, pInfo):
        ...
    def onUnitFlagsChanged(self, flags, timeLeft):
        ...
    def __fillViewModel(self):
        ...
    def __selectLevel(self, level):
        ...
    def __updateLevelStatus(self, level):
        ...
    def __onUpdateDifficultyLevelsViewState(self, *args, **kwargs):
        ...
    def __onSwitchLevel(self, args):
        ...
