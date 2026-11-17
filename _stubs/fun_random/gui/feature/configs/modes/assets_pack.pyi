# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/configs/modes/assets_pack.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from dict2model import fields as fields, models as models, schemas as schemas
from gui.impl.gen import R as R
funHangarEventBannerConfigurationSchema: Any
funProgressionViewConfigurationSchema: Any
funModeAssetsPackConfigurationSchema: Any

class FunModeAssetsPackConfigurationModel(models.Model):
    __slots__: tuple
    assetsPointer: Any
    hangarEventBanner: Any
    progressionView: Any
    def __init__(self, assetsPointer, hangarEventBanner, progressionView):
        ...
    def getIconsResRoot(self):
        ...
    def getLocalsResRoot(self):
        ...

class FunHangarEventBannerConfigModel(models.Model):
    __slots__: tuple
    borderColor: Any
    def __init__(self, borderColor):
        ...

class FunProgressionViewConfigModel(models.Model):
    __slots__: tuple
    pointsTitleFontColors: Any
    pointsValueFontColor: Any
    stagesFontColors: Any
    rewardCounterFontColor: Any
    def __init__(self, pointsTitleFontColors, pointsValueFontColor, stagesFontColors, rewardCounterFontColor):
        ...
