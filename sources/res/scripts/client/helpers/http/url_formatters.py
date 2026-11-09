# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/http/url_formatters.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/http/url_formatters.py
from __future__ import absolute_import
import typing
from future.moves.urllib import parse

class URL_PARTS_IDS(object):
    SCHEME = 0
    NETLOC = 1
    PATH = 2
    PARAMS = 3
    QUERY = 4
    FRAGMENT = 5


def addParamsToUrlQuery(url, params, keepBlankValues=False):
    urlParts = list(parse.urlparse(url))
    query = parse.parse_qs(urlParts[URL_PARTS_IDS.QUERY], keep_blank_values=keepBlankValues)
    query.update(params)
    urlParts[URL_PARTS_IDS.QUERY] = parse.urlencode(query, True)
    return parse.urlunparse(urlParts)


def separateQuery(url):
    urlParts = list(parse.urlparse(url))
    mainUrlParts = urlParts[:URL_PARTS_IDS.QUERY] + ['', '']
    queryParts = [''] * 4 + urlParts[URL_PARTS_IDS.QUERY:]
    return (parse.urlunparse(mainUrlParts), parse.urlunparse(queryParts))
