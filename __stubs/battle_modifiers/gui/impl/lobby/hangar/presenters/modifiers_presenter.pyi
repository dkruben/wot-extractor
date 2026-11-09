# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/client/battle_modifiers/gui/impl/lobby/hangar/presenters/modifiers_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from battle_modifiers.gui.impl.gen.view_models.views.lobby.hangar.modifiers_hangar_view_model import ModifiersHangarViewModel as ModifiersHangarViewModel
from frameworks.wulf.view.array import fillStringsArray as fillStringsArray
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from frameworks.wulf import Array as Array
from battle_modifiers.gui.feature.modifiers_data_provider import ModifiersDataProvider as ModifiersDataProvider

# base nao representavel no stub: ViewComponent[...]
class ModifiersPresenter:
    def __init__(self):
        ...
    def getModifiersDataProvider(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateData(self):
        ...
    def __invalidateModifiersDomains(self, modifiersDomains):
        ...
