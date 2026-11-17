# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_mode_state_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher, FunAssetPacksMixin as FunAssetPacksMixin
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_mode_state_model import FunRandomModeStateModel as FunRandomModeStateModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent

# base nao representavel no stub: ViewComponent[...]
class FunRandomModeStatePresenter(FunAssetPacksMixin, FunSubModesWatcher):
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getCallbacks(self):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def __invalidateAll(self, *_):
        ...
