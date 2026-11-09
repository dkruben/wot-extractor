# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/recruit_window/confirm_irrelevant_perk_reset_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.auxiliary.tankman_operations import packMajorSkills as packMajorSkills
from gui.impl.dialogs.dialog_template_button import ConfirmButton as ConfirmButton, CancelButton as CancelButton
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.views.lobby.crew.crew_constants import CrewConstants as CrewConstants
from gui.impl.gen.view_models.views.lobby.crew.dialogs.recruit_window.confirm_irrelevant_dialog_model import ConfirmIrrelevantDialogModel as ConfirmIrrelevantDialogModel
from gui.impl.lobby.crew.crew_helpers.skill_model_setup import ModelProps as ModelProps
from gui.impl.lobby.crew.dialogs.base_crew_dialog_template_view import BaseCrewDialogTemplateView as BaseCrewDialogTemplateView
from gui.impl.lobby.crew.dialogs.recruit_window.recruit_dialog_utils import getIcon as getIcon, getIconBackground as getIconBackground, getIconName as getIconName, getTitleFromTokenData as getTitleFromTokenData
_CUSTOM_PROPS_GETTERS: dict

class ConfirmIrrelevantPerkResetDialog(BaseCrewDialogTemplateView):
    __slots__: tuple
    LAYOUT_ID: Any
    VIEW_MODEL = ConfirmIrrelevantDialogModel
    __tokenData: Any
    __selectedRole: Any
    __vehicle: Any
    __tankman: Any
    __tankmanAfter: Any
    def __init__(self, ctx, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
