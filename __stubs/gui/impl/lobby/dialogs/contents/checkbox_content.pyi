# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/contents/checkbox_content.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.resources import R as R
from gui.impl.pub.dialog_window import DialogContent as DialogContent
from gui.impl.gen.view_models.ui_kit.check_box_model import CheckBoxModel as CheckBoxModel

class CheckBoxDialogContent(DialogContent):
    def __init__(self, label, selected=False):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, label, selected):
        ...
    def _finalize(self):
        ...
    def __onCheckBoxSelected(self, args=None):
        ...
