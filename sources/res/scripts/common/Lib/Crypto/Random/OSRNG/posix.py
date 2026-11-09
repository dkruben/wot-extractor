# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/Crypto/Random/OSRNG/posix.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/Random/OSRNG/posix.py
__revision__ = '$Id$'
__all__ = ['DevURandomRNG']
import errno, os, stat
from rng_base import BaseRNG
from Crypto.Util.py3compat import b

class DevURandomRNG(BaseRNG):

    def __init__(self, devname=None):
        if devname is None:
            self.name = '/dev/urandom'
        else:
            self.name = devname
        f = open(self.name, 'rb', 0)
        fmode = os.fstat(f.fileno())[stat.ST_MODE]
        if not stat.S_ISCHR(fmode):
            f.close()
            raise TypeError('%r is not a character special device' % (self.name,))
        self.__file = f
        BaseRNG.__init__(self)
        return

    def _close(self):
        self.__file.close()

    def _read(self, N):
        data = b('')
        while len(data) < N:
            try:
                d = self.__file.read(N - len(data))
            except IOError as e:
                if e.errno == errno.EINTR:
                    continue
                raise

            if d is None:
                return data
            if len(d) == 0:
                return data
            data += d

        return data


def new(*args, **kwargs):
    return DevURandomRNG(*args, **kwargs)
