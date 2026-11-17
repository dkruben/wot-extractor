# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_skill_tree/rarity_reward_screen/rarity_reward_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowLayer as WindowLayer, WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.veh_skill_tree.rarity_reward_screen_model import RarityRewardScreenModel as RarityRewardScreenModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.shared import events as events, g_eventBus as g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from gui.sounds.filters import switchHangarOverlaySoundFilter as switchHangarOverlaySoundFilter

class RarityRewardScreen(ViewImpl):
    __slots__: tuple
    _REWARD_SOUND_ID = 'elements_cust_reward'
    __element: Any
    __sound: Any
    def __init__(self, element):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onClose(self):
        ...

class RarityRewardWindow(LobbyWindow):
    __slots__: tuple
    _blur: Any
    def __init__(self, element):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
