# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/OpenBundleAccountComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import AccountCommands as AccountCommands
from BaseAccountExtensionComponent import BaseAccountExtensionComponent as BaseAccountExtensionComponent
from open_bundle_common.open_bundle_account_commands import CMD_OPEN_BUNDLE_PROCESS_NEXT_STEP as CMD_OPEN_BUNDLE_PROCESS_NEXT_STEP
from typing import Callable as Callable, Optional as Optional

class OpenBundleAccountComponent(BaseAccountExtensionComponent):
    def processNextStep(self, bundleID, stepNumber, callback):
        ...

def _getAccountRepository():
    ...
