# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/battle_control/controllers/repositories.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fort_rush.gui.battle_control.controllers import respawn_ctrl as respawn_ctrl
from fort_rush.gui.battle_control.controllers.spectator_ctrl import FortRushSpectatorViewController as FortRushSpectatorViewController
from gui.battle_control.controllers.repositories import SharedControllersRepository as SharedControllersRepository, ClassicControllersRepository as ClassicControllersRepository
from gui.battle_control.controllers.spectator_ctrl import SpectatorViewController as SpectatorViewController

class FortRushControllerRepository(ClassicControllersRepository):
    __slots__: tuple
    @classmethod
    def create(cls, setup):
        ...

class FortRushSharedControllersRepository(SharedControllersRepository):
    __slots__: tuple
    def addViewController(self, ctrl, setup):
        ...
