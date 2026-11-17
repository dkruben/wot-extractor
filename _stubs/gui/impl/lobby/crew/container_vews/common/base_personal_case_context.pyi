# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/common/base_personal_case_context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
from gui.impl.lobby.container_views.base.context import TankmanContext as TankmanContext
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.money import Currency as Currency, Money as Money
from helpers import dependency as dependency
from items.tankmen import getSpecialVoiceTag as getSpecialVoiceTag
from skeletons.gui.game_control import ISpecialSoundCtrl as ISpecialSoundCtrl
from typing import Optional as Optional, Dict as Dict, Any as Any

class BasePersonalCaseContext(TankmanContext):
    __slots__: tuple
    _specialSounds: _Any
    _tankmanCurrentVehicle: _Any
    _tankmanNativeVehicle: _Any
    _retrainPrice: _Any
    _voiceoverParams: _Any
    def __init__(self, tankmanID, *args, **kwargs):
        ...
    @property
    def tankmanCurrentVehicle(self):
        ...
    @property
    def tankmanNativeVehicle(self):
        ...
    @property
    def retrainPrice(self):
        ...
    @property
    def voiceoverParams(self):
        ...
    def update(self, tankmanID):
        ...
    def _getRetrainPrice(self):
        ...
    def _getUniqueVoiceoverParams(self):
        ...
