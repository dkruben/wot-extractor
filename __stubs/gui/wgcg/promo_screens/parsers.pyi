# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/promo_screens/parsers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.


class PromoDataParser(object):
    _ALL_FIELDS_MAP: dict
    _DATA_FIELDS_MAP: dict
    _DATA_FIELD_NAME = 'data'
    _INT_FIELDS: tuple
    _INT64_FIELDS: tuple
    _BOOL_FIELDS: tuple
    @classmethod
    def parse(cls, data):
        ...
    @classmethod
    def parseXML(cls, data):
        ...
    @classmethod
    def __abstractParse(cls, data, extractor):
        ...
    @classmethod
    def __extractFromXML(cls, data, key):
        ...
    @staticmethod
    def __extractFromArray(data, key):
        ...
