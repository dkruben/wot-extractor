# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/resources/models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Optional as Optional, Union as Union, TYPE_CHECKING as TYPE_CHECKING
from gui.game_loading.resources.consts import InfoStyles as InfoStyles
from gui.game_loading.resources.consts import ImageVfxs as ImageVfxs

class BaseResourceModel(object):
    __slots__: tuple
    minShowTimeSec: Any
    def __init__(self, minShowTimeSec):
        ...

class LocalImageModel(BaseResourceModel):
    __slots__: tuple
    imageRelativePath: Any
    vfx: Any
    localizationText: Any
    descriptionText: Any
    transition: Any
    imageAbsolutePath: Any
    def __init__(self, imageRelativePath, vfx=None, localizationText=None, descriptionText=None, minShowTimeSec=0, transition=0, imageAbsolutePath=None):
        ...
    def __repr__(self):
        ...

class LogoModel(BaseResourceModel):
    __slots__: tuple
    type: Any
    showCopyright: Any
    showVersion: Any
    transition: Any
    info: Any
    infoStyle: Any
    def __init__(self, logoType, minShowTimeSec=0, showCopyright=True, showVersion=True, transition=0, info='', infoStyle=...):
        ...
    def __repr__(self):
        ...

class StatusTextModel(BaseResourceModel):
    __slots__: tuple
    text: Any
    def __init__(self, text, minShowTimeSec=0):
        ...
    def __repr__(self):
        ...
