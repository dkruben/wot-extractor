# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/gui_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants_utils import ConstInjector as ConstInjector
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers import flag_constants as flag_constants

class QuestFlagTypes(flag_constants.QuestFlagTypes, ConstInjector):
    _const_type: Any
    EPIC = 'epicQuests'

class ViewAlias(VIEW_ALIAS, ConstInjector):
    _const_type: Any
