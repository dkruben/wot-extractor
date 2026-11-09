# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/resources/cdn/config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from dict2model import fields as fields
from dict2model import schemas as schemas
from dict2model import validate as validate
from dict2model import exceptions as exceptions
from gui.game_loading import loggers as loggers
from gui.game_loading.resources.cdn.consts import SequenceOrders as SequenceOrders, SequenceCohorts as SequenceCohorts, MAX_CONFIG_SEQUENCE_SLIDES_COUNT as MAX_CONFIG_SEQUENCE_SLIDES_COUNT, MAX_CONFIG_SEQUENCES_COUNT as MAX_CONFIG_SEQUENCES_COUNT
from gui.game_loading.resources.consts import ImageVfxs as ImageVfxs
from gui.game_loading.resources.cdn.models import ConfigSequenceModel as ConfigSequenceModel, ConfigModel as ConfigModel, ConfigSlideModel as ConfigSlideModel
_logger: Any
slideSchema: Any
sequenceSchema: Any
configSchema: Any

def _validateSequenceLifeTime(model):
    ...
def _validateSequencesNames(model):
    ...
def dumpSequenceModel(model):
    ...
def createSequenceModel(rawData):
    ...
def createConfigModel(rawData):
    ...
