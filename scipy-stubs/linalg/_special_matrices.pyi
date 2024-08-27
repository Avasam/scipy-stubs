from typing import Literal, TypeAlias, overload

import numpy as np
import numpy.typing as npt

import scipy._typing as spt

__all__ = [
    "block_diag",
    "circulant",
    "companion",
    "convolution_matrix",
    "dft",
    "fiedler",
    "fiedler_companion",
    "hadamard",
    "hankel",
    "helmert",
    "hilbert",
    "invhilbert",
    "invpascal",
    "kron",
    "leslie",
    "pascal",
    "toeplitz",
]

_Array_2d: TypeAlias = np.ndarray[tuple[int, int], np.dtype[np.generic]]
_Array_O_2d: TypeAlias = np.ndarray[tuple[int, int], np.dtypes.ObjectDType]
_Array_u8_2d: TypeAlias = np.ndarray[tuple[int, int], np.dtypes.UInt64DType]
_Array_i8_2d: TypeAlias = np.ndarray[tuple[int, int], np.dtypes.Int64DType]
_Array_f8_2d: TypeAlias = np.ndarray[tuple[int, int], np.dtypes.Float64DType]
_Array_c16_2d: TypeAlias = np.ndarray[tuple[int, int], np.dtypes.Complex128DType]

_SymmetryKind: TypeAlias = Literal["symmetric", "upper", "lower"]

def toeplitz(c: npt.ArrayLike, r: npt.ArrayLike | None = None) -> _Array_2d: ...
def circulant(c: npt.ArrayLike) -> _Array_2d: ...
def hankel(c: npt.ArrayLike, r: npt.ArrayLike | None = None) -> _Array_2d: ...
def hadamard(n: spt.AnyInt, dtype: npt.DTypeLike = ...) -> _Array_2d: ...
def leslie(f: npt.ArrayLike, s: npt.ArrayLike) -> _Array_2d: ...
def kron(a: npt.ArrayLike, b: npt.ArrayLike) -> _Array_2d: ...
def block_diag(*arrs: npt.ArrayLike) -> _Array_2d: ...
def companion(a: npt.ArrayLike) -> _Array_2d: ...
def helmert(n: spt.AnyInt, full: bool = False) -> _Array_f8_2d: ...
def hilbert(n: spt.AnyInt) -> _Array_f8_2d: ...

@overload
def invhilbert(n: spt.AnyInt, exact: Literal[False] = False) -> _Array_f8_2d: ...
@overload
def invhilbert(n: spt.AnyInt, exact: Literal[True]) -> _Array_i8_2d | _Array_O_2d: ...

@overload
def pascal(n: spt.AnyInt, kind: _SymmetryKind = "symmetric", exact: Literal[True] = True) -> _Array_u8_2d | _Array_O_2d: ...
@overload
def pascal(n: spt.AnyInt, kind: _SymmetryKind = "symmetric", *, exact: Literal[False]) -> _Array_f8_2d: ...
@overload
def pascal(n: spt.AnyInt, kind: _SymmetryKind, exact: Literal[False], /) -> _Array_f8_2d: ...

@overload
def invpascal(n: spt.AnyInt, kind: _SymmetryKind = "symmetric", exact: Literal[True] = True) -> _Array_i8_2d | _Array_O_2d: ...
@overload
def invpascal(n: spt.AnyInt, kind: _SymmetryKind = "symmetric", *, exact: Literal[False]) -> _Array_f8_2d: ...
@overload
def invpascal(n: spt.AnyInt, kind: _SymmetryKind, exact: Literal[False], /) -> _Array_f8_2d: ...

def dft(n: spt.AnyInt, scale: Literal["sqrtn", "n"] | None = None) -> _Array_c16_2d: ...
def fiedler(a: npt.ArrayLike) -> _Array_2d: ...
def fiedler_companion(a: npt.ArrayLike) -> _Array_2d: ...
def convolution_matrix(a: npt.ArrayLike, n: spt.AnyInt, mode: spt.CorrelateMode = "full") -> _Array_2d: ...
