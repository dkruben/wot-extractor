# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/helpers/resources.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.impl.gen import R as R
from helpers import dependency as dependency
from open_bundle.gui.constants import OPEN_BUNDLE_ENTRY_POINT_NAME as OPEN_BUNDLE_ENTRY_POINT_NAME
from open_bundle.skeletons.open_bundle_controller import IOpenBundleController as IOpenBundleController
from typing import Iterable as Iterable
from frameworks.wulf import PyResAccessor as PyResAccessor
_TEXT_PATH_PREFIX = 'open_bundle_lobby_{}'
_IMAGES_PATH_PREFIX = 'open_bundle.gui.maps.icons.bundles.{}'
_DEFAULT_BUNDLE_TYPE = 'default'

# decorador original: @dependency.replace_none_kwargs(...)
def getTextResource(bundleID, path, openBundle=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getBannerImagesPath(bundleID, openBundle=None):
    ...
def _getResourceFromPath(resource, path):
    ...
