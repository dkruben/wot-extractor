# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mapbox/map_box_awards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.mapbox.map_box_awards_view_model import MapBoxAwardsViewModel as MapBoxAwardsViewModel
from gui.impl.lobby.mapbox.sound import getMapboxViewSoundSpace as getMapboxViewSoundSpace, MapBoxSounds as MapBoxSounds, playSound as playSound
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.mapbox.mapbox_bonus_packers import getMapboxBonusPacker as getMapboxBonusPacker, packMapboxRewardModelAndTooltip as packMapboxRewardModelAndTooltip
from gui.mapbox.mapbox_helpers import getMapboxRewardTooltip as getMapboxRewardTooltip

class MapBoxAwardsView(ViewImpl):
    __slots__: tuple
    _COMMON_SOUND_SPACE: Any
    __numBattles: Any
    __reward: Any
    __tooltips: Any
    def __init__(self, numBattles, reward, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...

class MapBoxAwardsViewWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, numBattles, rewards, parent=None):
        ...
