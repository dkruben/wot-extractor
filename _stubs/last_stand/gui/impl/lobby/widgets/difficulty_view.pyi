# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/widgets/difficulty_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control import prbEntityProperty as prbEntityProperty
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prb_control.entities.base.unit.listener import IUnitListener as IUnitListener
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from account_helpers import AccountSettings as AccountSettings
from helpers import dependency as dependency
from last_stand.gui.game_control.ls_difficulty_missions_controller import getFormattedMissionsList as getFormattedMissionsList
from last_stand.gui.ls_account_settings import AccountSettingsKeys as AccountSettingsKeys
from last_stand.gui.ls_gui_constants import DifficultyLevel as DifficultyLevel
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.difficulty_item_model import DifficultyItemModel as DifficultyItemModel, StateEnum as StateEnum
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.difficulty_view_model import DifficultyViewModel as DifficultyViewModel
from last_stand.gui.impl.lobby.tooltips.difficulty_tooltip import DifficultyTooltipView as DifficultyTooltipView
from last_stand.gui.prb_control.entities.squad.entity import LastStandSquadEntity as LastStandSquadEntity
from last_stand.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand.skeletons.ls_difficulty_missions_controller import ILSDifficultyMissionsController as ILSDifficultyMissionsController
from last_stand_common.last_stand_constants import DEFAULT_DIFFICULTY_MODIFIER as DEFAULT_DIFFICULTY_MODIFIER

# base nao representavel no stub: ViewComponent[...]
class DifficultyView(IGlobalListener, IUnitListener):
    _difficultyCtrl: Any
    lsCtrl: Any
    lsMissionsCtrl: Any
    _platoonCtrl: Any
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
    def onUnitFlagsChanged(self, flags, timeLeft):
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
    def __fillViewModel(self):
        ...
    def __selectLevel(self, level):
        ...
    def __updateLevelStatus(self, level):
        ...
    def __onUpdateDifficultyLevelsViewState(self, *args, **kwargs):
        ...
    def __onSwitchLevel(self, result):
        ...
    def __select(self, level):
        ...
    def __updateMissionsStatus(self):
        ...
