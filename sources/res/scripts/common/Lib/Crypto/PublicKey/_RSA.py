# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/Crypto/PublicKey/_RSA.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/PublicKey/_RSA.py
__revision__ = '$Id$'
from Crypto.PublicKey import pubkey
from Crypto.Util import number

def generate_py(bits, randfunc, progress_func=None, e=65537):
    obj = RSAobj()
    obj.e = long(e)
    if progress_func:
        progress_func('p,q\n')
    p = q = 1L
    while number.size(p * q) < bits:
        p = pubkey.getStrongPrime(bits >> 1, obj.e, 1e-12, randfunc)
        q = pubkey.getStrongPrime(bits - (bits >> 1), obj.e, 1e-12, randfunc)

    if p > q:
        p, q = q, p
    obj.p = p
    obj.q = q
    if progress_func:
        progress_func('u\n')
    obj.u = pubkey.inverse(obj.p, obj.q)
    obj.n = obj.p * obj.q
    if progress_func:
        progress_func('d\n')
    obj.d = pubkey.inverse(obj.e, (obj.p - 1) * (obj.q - 1))
    return obj


class RSAobj(pubkey.pubkey):

    def size(self):
        return number.size(self.n) - 1
