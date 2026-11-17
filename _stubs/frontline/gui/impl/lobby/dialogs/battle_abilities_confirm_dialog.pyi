# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/dialogs/battle_abilities_confirm_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView
from gui.impl.gen import R as R
from frontline.gui.impl.gen.view_models.views.lobby.dialogs.battle_abilities_confirm_dialog_model import BattleAbilitiesConfirmDialogModel as BattleAbilitiesConfirmDialogModel
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from PlayerEvents import g_playerEvents as g_playerEvents

class BattleAbilitiesConfirmDialog(FullScreenDialogBaseView):
    __epicMetaGameCtrl: Any
    __slots__: tuple
    LAYOUT_ID: Any
    __skillsInteractor: Any
    __vehicleType: Any
    __isCloseButtonClicked: Any
    def __init__(self, skillsInteractor, vehicleType=''):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _fillViewModel(self):
        ...
    def _getAdditionalData(self):
        ...
    def _onCheckBoxClick(self):
        ...
    def _onSubmitClick(self):
        ...
    def _onCancelClick(self):
        ...
    def _onCloseClick(self):
        ...
