# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/battle/views/leave_battle_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.dialogs.dialog_template import DialogTemplateView as DialogTemplateView
from gui.impl.dialogs.dialog_template_button import ConfirmButton as ConfirmButton, CancelButton as CancelButton
from gui.impl.gen import R as R
from battle_royale.gui.impl.gen.view_models.views.battle.views.leave_battle_view_model import LeaveBattleViewModel as LeaveBattleViewModel

class LeaveBattleView(DialogTemplateView):
    __slots__: tuple
    LAYOUT_ID: Any
    VIEW_MODEL = LeaveBattleViewModel
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
