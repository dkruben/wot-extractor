# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/game_control/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from battle_royale.gui.game_control.awards_controller import BRProgressionStageHandler as BRProgressionStageHandler
from battle_royale.gui.game_control.progression_controller import BRProgressionController as BRProgressionController
from battle_royale.gui.game_control.battle_royale_controller import BattleRoyaleController as _BattleRoyale
from battle_royale.gui.game_control.battle_royale_tournament_controller import BattleRoyaleTournamentController as _BRTournament
import skeletons.gui.game_control as _interface
from gui.shared.system_factory import registerAwardControllerHandler as registerAwardControllerHandler, registerGameControllers as registerGameControllers
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE
from soft_exception import SoftException as SoftException

def registerBRGameControllers():
    ...
def registerBRProgressionAwardControllers():
    ...
