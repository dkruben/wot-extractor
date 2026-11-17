# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/messenger/formatters/battle_results_formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from fun_random.gui.shared.fun_system_factory import collectBattleResultsMessageSubFormatter as collectBattleResultsMessageSubFormatter
from messenger.formatters.service_channel import WaitItemsSyncFormatter as WaitItemsSyncFormatter, BattleResultsFormatter as BattleResultsFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData

class FunBattleResultsFormatter(WaitItemsSyncFormatter):
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...

class FunRandomBattleResultsSubFormatter(BattleResultsFormatter):
    ...
