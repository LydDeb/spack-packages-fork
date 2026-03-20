# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNvidiaPhysicsnemoSym(PythonPackage, CudaPackage):
    """A deep learning framework for AI-driven multi-physics systems."""

    homepage = "https://developer.nvidia.com/physicsnemo"
    git = "https://github.com/NVIDIA/physicsnemo-sym.git"
    pypi = "nvidia_physicsnemo_sym/nvidia_physicsnemo_sym-2.4.0.tar.gz"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("2.4.0", sha256="f07e601c50806bdad80c0509a3a7aafcf644d4fe936e689901f3b1baaec4e08c")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type=("build"))
    depends_on("py-setuptools-scm", type=("build"))
    depends_on("py-cython@0.29:", type=("build", "run"))
    depends_on("py-chaospy@4.3.7:", type=("build", "run"))
    depends_on("py-h5py@3.7.0:", type=("build", "run"))
    depends_on("py-hydra-core@1.2.0:", type=("build", "run"))
    depends_on("py-mistune@2.0:", type=("build", "run"))
    depends_on("ninja", type=("build", "run"))
    depends_on("py-notebook@7.2.2:", type=("build", "run"))
    depends_on("py-numpoly@:1.3.4", type=("build", "run"))
    depends_on("py-numpy-stl@2.16:", type=("build", "run"))
    depends_on("py-nvidia-physicsnemo@2.0.0:", type=("build", "run"))
    depends_on("py-opencv-python@4.8.1.78:", type=("build", "run"))
    depends_on("py-pillow@10.3:", type=("build", "run"))
    depends_on("py-pint@0.19.2:", type=("build", "run"))
    depends_on("py-scikit-learn@1.2.0:", type=("build", "run"))
    depends_on("py-symengine@0.10.0:", type=("build", "run"))
    depends_on("py-sympy@1.12:", type=("build", "run"))
    depends_on("py-tensorboard@2.8.0:", type=("build", "run"))
    depends_on("py-termcolor@2.1.1:", type=("build", "run"))
    depends_on("py-timm@1.0.3:", type=("build", "run"))
    depends_on("py-torch-optimizer@0.3.0:", type=("build", "run"))
    depends_on("py-transforms3d@0.3.1:", type=("build", "run"))
    depends_on("vtk@9.2.6: +python", type=("build", "run"))
