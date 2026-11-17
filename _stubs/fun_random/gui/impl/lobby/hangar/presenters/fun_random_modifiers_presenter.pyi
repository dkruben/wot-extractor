# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_modifiers_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from battle_modifiers.gui.impl.lobby.hangar.presenters.modifiers_presenter import ModifiersPresenter as ModifiersPresenter
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from fun_random.gui.impl.lobby.tooltips.fun_random_domain_tooltip_view import FunRandomDomainTooltipView as FunRandomDomainTooltipView
from gui.impl.gen import R as R

class FunRandomModifiersPresenter(ModifiersPresenter, FunSubModesWatcher):
    # decorador original: @hasDesiredSubMode(...)
    def getModifiersDataProvider(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _updateData(self, *_):
        ...
