# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/platoon/view/fun_platoon_members_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.platoon.members_window_model import PrebattleTypes as PrebattleTypes
from gui.impl.lobby.platoon.platoon_helpers import getPlatoonBonusState as getPlatoonBonusState
from gui.impl.lobby.platoon.view.platoon_members_view import SquadMembersView as SquadMembersView
from gui.impl.lobby.platoon.view.subview.platoon_chat_subview import ChatSubview as ChatSubview

class FunRandomMembersView(SquadMembersView, FunAssetPacksMixin, FunSubModesWatcher):
    _prebattleType = PrebattleTypes.FUNRANDOM
    # decorador original: @hasDesiredSubMode(...)
    def _getTitle(self):
        ...
    def _setHeaderBg(self, fileName, model):
        ...
    def _onFindPlayers(self):
        ...
    def _addSubviews(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _updateFindPlayersButton(self, *args):
        ...
    def __onSubModeSelected(self, *_):
        ...
