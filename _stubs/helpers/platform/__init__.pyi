# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/platform/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from constants import WGC_PUBLICATION as WGC_PUBLICATION
from helpers import dependency as dependency
from helpers.platform.base import BasePublishPlatform as BasePublishPlatform
from helpers.platform.steam import SteamPublishPlatform as SteamPublishPlatform
from skeletons.gui.login_manager import ILoginManager as ILoginManager
from skeletons.helpers.platform import IPublishPlatform as IPublishPlatform
_MAPPING: dict

# decorador original: @dependency.replace_none_kwargs(...)
def getPublishPlatform(loginManager=None):
    ...
