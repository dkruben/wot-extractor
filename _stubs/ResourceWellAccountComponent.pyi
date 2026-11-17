# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/ResourceWellAccountComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import json as json
import typing as typing
from resource_well_common.resource_well_account_commands import CMD_RESOURCE_WELL_PUT as CMD_RESOURCE_WELL_PUT, CMD_RESOURCE_WELL_TAKE as CMD_RESOURCE_WELL_TAKE
import AccountCommands as AccountCommands
from BaseAccountExtensionComponent import BaseAccountExtensionComponent as BaseAccountExtensionComponent
from typing import Callable as Callable, Optional as Optional, List as List, Tuple as Tuple

class ResourceWellAccountComponent(BaseAccountExtensionComponent):
    def putResources(self, resources, reward, callback):
        ...
    def takeBack(self, callback):
        ...

def _getAccountRepository():
    ...
