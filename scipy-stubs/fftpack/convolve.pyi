from scipy._typing import Untyped

__all__ = ["convolve", "convolve_z", "destroy_convolve_cache", "init_convolution_kernel"]

def convolve(inout: Untyped, omega: Untyped, swap_real_imag: bool = False, overwrite_x: bool = False) -> Untyped: ...
def convolve_z(inout: Untyped, omega_real: Untyped, omega_imag: Untyped, overwrite_x: bool = False) -> Untyped: ...
def init_convolution_kernel(
    n: int,
    kernel_func: Untyped,
    d: int = 0,
    zero_nyquist: int | None = None,
    kernel_func_extra_args: Untyped = (),
) -> Untyped: ...
def destroy_convolve_cache() -> None: ...
