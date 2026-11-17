# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/comp7_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.Scaleform.genConsts.COMP7_HANGAR_ALIASES import COMP7_HANGAR_ALIASES as COMP7_HANGAR_ALIASES
from constants_utils import ConstInjector as ConstInjector
from gui.prb_control import settings as settings
from messenger import m_constants as m_constants
COMP7_HANGAR_ALIAS = COMP7_HANGAR_ALIASES.COMP7_LOBBY_HANGAR
COMP7_ENTRY_POINT_ALIAS = 'Comp7EntryPoint'
INFO_PAGE_WCI = 'infoPageWci'
INFO_PAGE_OLS = 'infoPageOls'

class FUNCTIONAL_FLAG(settings.FUNCTIONAL_FLAG, ConstInjector):
    COMP7 = 536870912

class PREBATTLE_ACTION_NAME(settings.PREBATTLE_ACTION_NAME, ConstInjector):
    _const_type: Any
    COMP7 = 'comp7'
    COMP7_SQUAD = 'comp7Squad'

class SELECTOR_BATTLE_TYPES(settings.SELECTOR_BATTLE_TYPES, ConstInjector):
    _const_type: Any
    COMP7 = 'comp7'

class REQUEST_TYPE(settings.REQUEST_TYPE, ConstInjector):
    ...

class SCH_CLIENT_MSG_TYPE(m_constants.SCH_CLIENT_MSG_TYPE, ConstInjector):
    ...
