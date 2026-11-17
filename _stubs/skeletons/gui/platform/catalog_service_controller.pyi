# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/skeletons/gui/platform/catalog_service_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import adisp as adisp

class IPurchaseCache(object):
    def init(self):
        ...
    def fini(self):
        ...
    # decorador original: @adisp.adisp_async
    def requestPurchaseByID(self, pId, callback=None):
        ...
    def getCachedPurchase(self, pId):
        ...
    def getProductCode(self, pId):
        ...
    def canBeRequestedFromProduct(self, data):
        ...
