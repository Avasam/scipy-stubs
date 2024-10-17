from typing_extensions import Self, override

from scipy._typing import Untyped

__all__ = [
    "StateSpace",
    "TransferFunction",
    "ZerosPolesGain",
    "bode",
    "dbode",
    "dfreqresp",
    "dimpulse",
    "dlsim",
    "dlti",
    "dstep",
    "freqresp",
    "impulse",
    "lsim",
    "lti",
    "place_poles",
    "step",
]

class LinearTimeInvariant:
    inputs: Untyped
    outputs: Untyped
    def __new__(cls, *system: Untyped, **kwargs: Untyped) -> Self: ...
    def __init__(self) -> None: ...
    @property
    def dt(self) -> Untyped: ...
    @property
    def zeros(self) -> Untyped: ...
    @property
    def poles(self) -> Untyped: ...

class lti(LinearTimeInvariant):
    def __new__(cls, *system: Untyped) -> Self: ...
    def __init__(self, *system: Untyped) -> None: ...
    def impulse(self, X0: Untyped | None = None, T: Untyped | None = None, N: Untyped | None = None) -> Untyped: ...
    def step(self, X0: Untyped | None = None, T: Untyped | None = None, N: Untyped | None = None) -> Untyped: ...
    def output(self, U: Untyped, T: Untyped, X0: Untyped | None = None) -> Untyped: ...
    def bode(self, w: Untyped | None = None, n: int = 100) -> Untyped: ...
    def freqresp(self, w: Untyped | None = None, n: int = 10000) -> Untyped: ...
    def to_discrete(self, dt: Untyped, method: str = "zoh", alpha: Untyped | None = None) -> Untyped: ...

class dlti(LinearTimeInvariant):
    def __new__(cls, *system: Untyped, **kwargs: Untyped) -> Self: ...
    def __init__(self, *system: Untyped, **kwargs: Untyped) -> None: ...
    def impulse(self, x0: Untyped | None = None, t: Untyped | None = None, n: Untyped | None = None) -> Untyped: ...
    def step(self, x0: Untyped | None = None, t: Untyped | None = None, n: Untyped | None = None) -> Untyped: ...
    def output(self, u: Untyped, t: Untyped, x0: Untyped | None = None) -> Untyped: ...
    def bode(self, w: Untyped | None = None, n: int = 100) -> Untyped: ...
    def freqresp(self, w: Untyped | None = None, n: int = 10000, whole: bool = False) -> Untyped: ...

class TransferFunction(LinearTimeInvariant):
    inputs: int
    outputs: int
    def __new__(cls, *system: Untyped, **kwargs: Untyped) -> Self: ...
    def __init__(self, *system: Untyped, **kwargs: Untyped) -> None: ...
    @property
    def num(self) -> Untyped: ...
    @num.setter
    def num(self, num: Untyped) -> None: ...
    @property
    def den(self) -> Untyped: ...
    @den.setter
    def den(self, den: Untyped) -> None: ...
    def to_tf(self) -> Untyped: ...
    def to_zpk(self) -> Untyped: ...
    def to_ss(self) -> Untyped: ...

class TransferFunctionContinuous(TransferFunction, lti):
    @override
    def to_discrete(self, dt: Untyped, method: str = "zoh", alpha: Untyped | None = None) -> Untyped: ...

class TransferFunctionDiscrete(TransferFunction, dlti): ...

class ZerosPolesGain(LinearTimeInvariant):
    inputs: int
    outputs: int
    def __new__(cls, *system: Untyped, **kwargs: Untyped) -> Self: ...
    def __init__(self, *system: Untyped, **kwargs: Untyped) -> None: ...
    @property
    def gain(self) -> Untyped: ...
    @gain.setter
    def gain(self, gain: Untyped) -> None: ...
    def to_tf(self) -> Untyped: ...
    def to_zpk(self) -> Untyped: ...
    def to_ss(self) -> Untyped: ...

class ZerosPolesGainContinuous(ZerosPolesGain, lti):
    @override
    def to_discrete(self, dt: Untyped, method: str = "zoh", alpha: Untyped | None = None) -> Untyped: ...

class ZerosPolesGainDiscrete(ZerosPolesGain, dlti): ...

class StateSpace(LinearTimeInvariant):
    __array_priority__: float
    __array_ufunc__: Untyped
    inputs: Untyped
    outputs: Untyped
    def __new__(cls, *system: Untyped, **kwargs: Untyped) -> Self: ...
    def __init__(self, *system: Untyped, **kwargs: Untyped) -> None: ...
    def __mul__(self, other: Untyped) -> Untyped: ...
    def __rmul__(self, other: Untyped) -> Untyped: ...
    def __neg__(self) -> Untyped: ...
    def __add__(self, other: Untyped) -> Untyped: ...
    def __sub__(self, other: Untyped) -> Untyped: ...
    def __radd__(self, other: Untyped) -> Untyped: ...
    def __rsub__(self, other: Untyped) -> Untyped: ...
    def __truediv__(self, other: Untyped) -> Untyped: ...
    @property
    def A(self) -> Untyped: ...
    @A.setter
    def A(self, A: Untyped) -> None: ...
    @property
    def B(self) -> Untyped: ...
    @B.setter
    def B(self, B: Untyped) -> None: ...
    @property
    def C(self) -> Untyped: ...
    @C.setter
    def C(self, C: Untyped) -> None: ...
    @property
    def D(self) -> Untyped: ...
    @D.setter
    def D(self, D: Untyped) -> None: ...
    def to_tf(self, **kwargs: Untyped) -> Untyped: ...
    def to_zpk(self, **kwargs: Untyped) -> Untyped: ...
    def to_ss(self) -> Untyped: ...

class StateSpaceContinuous(StateSpace, lti):
    @override
    def to_discrete(self, dt: Untyped, method: str = "zoh", alpha: Untyped | None = None) -> Untyped: ...

class Bunch:
    def __init__(self, **kwds: Untyped) -> None: ...

class StateSpaceDiscrete(StateSpace, dlti): ...

def lsim(system: Untyped, U: Untyped, T: Untyped, X0: Untyped | None = None, interp: bool = True) -> Untyped: ...
def impulse(system: Untyped, X0: Untyped | None = None, T: Untyped | None = None, N: Untyped | None = None) -> Untyped: ...
def step(system: Untyped, X0: Untyped | None = None, T: Untyped | None = None, N: Untyped | None = None) -> Untyped: ...
def bode(system: Untyped, w: Untyped | None = None, n: int = 100) -> Untyped: ...
def freqresp(system: Untyped, w: Untyped | None = None, n: int = 10000) -> Untyped: ...
def place_poles(
    A: Untyped,
    B: Untyped,
    poles: Untyped,
    method: str = "YT",
    rtol: float = 0.001,
    maxiter: int = 30,
) -> Untyped: ...
def dlsim(system: Untyped, u: Untyped, t: Untyped | None = None, x0: Untyped | None = None) -> Untyped: ...
def dimpulse(system: Untyped, x0: Untyped | None = None, t: Untyped | None = None, n: Untyped | None = None) -> Untyped: ...
def dstep(system: Untyped, x0: Untyped | None = None, t: Untyped | None = None, n: Untyped | None = None) -> Untyped: ...
def dfreqresp(system: Untyped, w: Untyped | None = None, n: int = 10000, whole: bool = False) -> Untyped: ...
def dbode(system: Untyped, w: Untyped | None = None, n: int = 100) -> Untyped: ...
