# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/battle/vehicle_ban/ban_progression.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.impl.battle.vehicle_ban.ban_helpers import fillBanProgressionModel as fillBanProgressionModel
from comp7_core.gui.battle_control.controllers.sound_ctrls.comp7_battle_sounds import BAN_PROGRESSION_SOUND_SPACE as BAN_PROGRESSION_SOUND_SPACE
from comp7_core.gui.comp7_core_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from comp7.gui.impl.gen.view_models.views.battle.ban_progression_model import BanProgressionModel as BanProgressionModel
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.window_impl import WindowImpl as WindowImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class BanProgressionView(ViewImpl):
    __slots__: tuple
    _COMMON_SOUND_SPACE = BAN_PROGRESSION_SOUND_SPACE
    __comp7Controller: Any
    __sessionProvider: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateData(self, model=None):
        ...
    def __onPollServerTime(self):
        ...
    def __getVehicleBanCtrl(self):
        ...

class BanProgressionWindow(WindowImpl):
    __slots__: tuple
    def __init__(self, parent=None):
        ...
