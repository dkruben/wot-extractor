# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/free_skill_confirmation_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl import backport as backport
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.dialogs.sub_views.common.simple_text import ImageSubstitution as ImageSubstitution
from gui.impl.dialogs.sub_views.content.simple_text_content import SimpleTextContent as SimpleTextContent
from gui.impl.dialogs.sub_views.icon.icon_set import IconSet as IconSet
from gui.impl.dialogs.sub_views.title.simple_text_title import SimpleTextTitle as SimpleTextTitle
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as Placeholder
from gui.impl.lobby.crew.dialogs.base_crew_dialog_template_view import BaseCrewDialogTemplateView as BaseCrewDialogTemplateView
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.tankman_skill import TankmanSkill as TankmanSkill

class FreeSkillConfirmationDialog(BaseCrewDialogTemplateView):
    __appLoader: Any
    __slots__: tuple
    _itemsCache: Any
    __skill: Any
    def __init__(self, skill, layoutID=None, uniqueID=None):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
