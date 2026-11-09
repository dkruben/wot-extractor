# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/temperature/common/mechanic_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState

class ITemperatureComponentParams(object):
    @property
    def coolingPerSec(self):
        ...
    @property
    def maxTemperature(self):
        ...

class ITemperatureMechanicState(IMechanicState):
    @property
    def state(self):
        ...
    @property
    def currentTemperature(self):
        ...
    @property
    def maxTemperature(self):
        ...
    @property
    def temperatureProgress(self):
        ...
