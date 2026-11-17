# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/skills_training_confirm_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.dialogs.dialog_template import DialogTemplateView as DialogTemplateView
from gui.impl.dialogs.dialog_template_button import ConfirmButton as ConfirmButton, CancelButton as CancelButton
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_model import SkillModel as SkillModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.skills_training_confirm_dialog_model import SkillsTrainingConfirmDialogModel as SkillsTrainingConfirmDialogModel
from gui.impl.lobby.crew.crew_helpers.skill_model_setup import skillSimpleModelSetup as skillSimpleModelSetup
from gui.shared.gui_items.tankman_skill import getTankmanSkill as getTankmanSkill

class SkillsTrainingConfirmDialog(DialogTemplateView):
    __slots__: tuple
    LAYOUT_ID: Any
    VIEW_MODEL = SkillsTrainingConfirmDialogModel
    __tankman: Any
    __skillsRole: Any
    __skillsList: Any
    __availableSkillsData: Any
    __isClosed: Any
    def __init__(self, tankman, skillsRole, skillsList, availableSkillsData, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _closeClickHandler(self, args=None):
        ...
    def _getAdditionalData(self):
        ...
