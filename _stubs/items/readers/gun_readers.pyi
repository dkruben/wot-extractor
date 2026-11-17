# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/readers/gun_readers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import TYPE_CHECKING as TYPE_CHECKING, Tuple as Tuple, Optional as Optional
import ResMgr as ResMgr
from items import _xml as _xml
from items.components import component_constants as component_constants
from items.components import gun_components as gun_components
from items.components.shell_components import Stun as Stun
from items.stun import g_cfg as stunConfig
from items.readers import shared_readers as shared_readers
from constants import IS_EDITOR as IS_EDITOR
from items.vehicles import Cache as Cache

def readRecoilEffect(xmlCtx, section, cache):
    ...
def readStunParams(section, xmlCtx=None, useDefaults=False):
    ...
