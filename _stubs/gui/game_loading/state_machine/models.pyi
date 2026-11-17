# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/state_machine/models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.game_loading.resources.consts import Milestones as Milestones
from gui.game_loading.resources.models import StatusTextModel as StatusTextModel
from gui.game_loading.state_machine.const import ContentState as ContentState

class ImageViewSettingsModel(object):
    __slots__: tuple
    showVfx: Any
    contentState: Any
    ageRatingPath: Any
    info: Any
    showSmallLogo: Any
    minimalDuration: Any
    def __init__(self, showVfx=True, contentState=..., ageRatingPath='', info='', showSmallLogo=True, minimalDuration=0.0):
        ...
    def __repr__(self):
        ...

class ProgressSettingsModel(object):
    __slots__: tuple
    startPercent: Any
    limitPercent: Any
    ticksInProgress: Any
    minTickTimeSec: Any
    def __init__(self, startPercent, limitPercent, ticksInProgress, minTickTimeSec):
        ...
    def __repr__(self):
        ...

class LoadingMilestoneModel(object):
    __slots__: tuple
    name: Any
    percent: Any
    forceApply: Any
    status: Any
    def __init__(self, name, percent, forceApply, status):
        ...
    def __repr__(self):
        ...
