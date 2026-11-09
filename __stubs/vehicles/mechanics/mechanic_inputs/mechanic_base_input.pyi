# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/mechanic_inputs/mechanic_base_input.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from events_containers.common.containers import ContainersListener as ContainersListener
from events_containers.components.life_cycle import IComponentLifeCycleListenerLogic as IComponentLifeCycleListenerLogic
from events_handler import eventHandler as eventHandler
from events_containers.components.life_cycle import ILifeCycleComponent as ILifeCycleComponent
from vehicles.mechanics.mechanic_inputs.mechanic_input_profile import MechanicInputProfile as MechanicInputProfile

class BaseMechanicInput(ContainersListener, IComponentLifeCycleListenerLogic):
    _profiles: Any
    def __init__(self):
        ...
    # decorador original: @eventHandler
    def onComponentAvatarReady(self, _):
        ...
    # decorador original: @eventHandler
    def onComponentDestroyed(self, _):
        ...
    def _register(self, profile):
        ...
