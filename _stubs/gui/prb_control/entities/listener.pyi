# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/listener.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.prb_control.entities.base.legacy.listener import ILegacyListener as ILegacyListener
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.prb_control.entities.base.pre_queue.listener import IPreQueueListener as IPreQueueListener
from gui.prb_control.entities.base.unit.listener import IUnitListener as IUnitListener, IStrongholdListener as IStrongholdListener

class IGlobalListener(ILegacyListener, IUnitListener, IPreQueueListener, IStrongholdListener, IPrbListener):
    def onPrbEntitySwitching(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def startGlobalListening(self):
        ...
    def stopGlobalListening(self):
        ...
