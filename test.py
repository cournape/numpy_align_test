import sys
sys.path.insert(0, "dummy")

import numpy as np

import _dummy

# You often need to run several iterations to get an array which is not 16
# bytes aligned
for i in range(10):
    n = 4
    x = np.zeros(n * 3, dtype="D")
    print x.flags.aligned
    print hex(x.__array_interface__["data"][0])
    _dummy.zfoo(x, n)
