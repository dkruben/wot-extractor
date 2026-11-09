# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mode_selector/items/random_mode_selector_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_card_types import ModeSelectorCardTypes as ModeSelectorCardTypes
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_random_battle_model import ModeSelectorRandomBattleModel as ModeSelectorRandomBattleModel
from gui.impl.lobby.mode_selector.items import setBattlePassState as setBattlePassState
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem as ModeSelectorLegacyItem
from gui.impl.lobby.mode_selector.items.items_constants import ModeSelectorRewardID as ModeSelectorRewardID

class RandomModeSelectorItem(ModeSelectorLegacyItem):
    __slots__: tuple
    _VIEW_MODEL = ModeSelectorRandomBattleModel
    _CARD_VISUAL_TYPE = ModeSelectorCardTypes.RANDOM
    @property
    def viewModel(self):
        ...
    def _onInitializing(self):
        ...
