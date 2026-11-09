# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/attachment_reward_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.lobby.customization.customization_rarity_reward_screen.customization_rarity_reward_screen import CustomizationRarityRewardScreen as CustomizationRarityRewardScreen
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur

class AttachmentRewardView(CustomizationRarityRewardScreen):
    _LAYOUT_ID: Any

class AttachmentRewardWindow(LobbyNotificationWindow):
    __slots__: tuple
    _blur: Any
    _args: Any
    def __init__(self, element, isFirstEntry):
        ...
    def isParamsEqual(self, *args):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
