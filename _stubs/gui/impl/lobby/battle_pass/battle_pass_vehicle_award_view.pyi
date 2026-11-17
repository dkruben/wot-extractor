# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/battle_pass_vehicle_award_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from frameworks.wulf import ViewSettings as ViewSettings
from gui.battle_pass.sounds import BattlePassSounds as BattlePassSounds
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_vehicle_award_view_model import BattlePassVehicleAwardViewModel as BattlePassVehicleAwardViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.sounds.filters import switchHangarOverlaySoundFilter as switchHangarOverlaySoundFilter
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from skeletons.gui.shared import IItemsCache as IItemsCache

class BattlePassVehicleAwardView(ViewImpl):
    __slots__: tuple
    __itemsCache: Any
    __battlePass: Any
    def __init__(self, layoutID, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, data, *args, **kwargs):
        ...
    def _finalize(self):
        ...

class BattlePassVehicleAwardWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, data):
        ...
