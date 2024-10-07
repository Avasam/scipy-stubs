# This module is not meant for public use and will be removed in SciPy v2.0.0.
from typing_extensions import Self, deprecated

__all__ = ["LinearOperator", "expm", "inv", "spsolve"]

@deprecated("will be removed in SciPy v2.0.0")
class LinearOperator:
    __array_ufunc__: object
    ndim: object

    def __new__(cls, dtype: object, shape: object) -> Self: ...
    def __init__(self, /, dtype: object, shape: object) -> None: ...
    def matvec(self, /, x: object) -> object: ...
    def rmatvec(self, /, x: object) -> object: ...
    def matmat(self, /, X: object) -> object: ...
    def rmatmat(self, /, X: object) -> object: ...
    def __call__(self, /, x: object) -> object: ...
    def __mul__(self, x: object, /) -> object: ...
    def __truediv__(self, other: object, /) -> object: ...
    def dot(self, /, x: object) -> object: ...
    def __matmul__(
        self,
        other: object,
        /,
    ) -> object: ...
    def __rmatmul__(
        self,
        other: object,
        /,
    ) -> object: ...
    def __rmul__(self, x: object) -> object: ...
    def __pow__(self, p: object) -> object: ...
    def __add__(self, x: object, /) -> object: ...
    def __neg__(self, /) -> object: ...
    def __sub__(self, x: object, /) -> object: ...
    def adjoint(self, /) -> object: ...
    @property
    def H(self, /) -> object: ...
    def transpose(self, /) -> object: ...
    @property
    def T(self) -> object: ...

@deprecated("will be removed in SciPy v2.0.0")
def spsolve(A: object, b: object, permc_spec: object = ..., use_umfpack: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def expm(A: object) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def inv(A: object) -> object: ...
