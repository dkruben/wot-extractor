# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/params_schemas/veh_playlists_schema.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from game_params_common.schema import GameParamsSchema as GameParamsSchema
from constants import Configs as Configs
from dict2model import models as models, fields as d2mfields
vehPlaylistsConfigSchema: Any

class VehPlaylistsConfigModel(models.Model):
    __slots__: tuple
    isVehPlaylistsEnabled: Any
    def __init__(self, isVehPlaylistsEnabled):
        ...
