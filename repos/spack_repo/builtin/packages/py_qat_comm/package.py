# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *

from packaging.tags import sys_tags


class PyQatComm(PythonPackage):
    """Module qat-comm [6b072af] - Compiled by Bull"""

    homepage = "https://www.bull.com/en/solutions/quantum-computing"

    supplier = "Organization: Bull SAS"

    maintainers("LydDeb")

    supported_tag = ["manylinux_2_28_x86_64"]

    version(
        "1.9.0-cp313", sha256="39accae71c6b08923ea60705fdab506d9c8a2212e6b12cf1a5eb94010fa3c19b"
    )
    version(
        "1.9.0-cp312", sha256="3fce6c0dbe63c6263a71417fa46d87e4ae39af03dee6f8c2c16a2e94c85cca78"
    )
    version(
        "1.9.0-cp311", sha256="238a1746657f5adf8b98cf1e704159d07c293247a226f0d79d4d004bd064b285"
    )
    version(
        "1.9.0-cp310", sha256="1ec5692296a56794128266d615032713c728ec56a8a94ec5d3fafd3d496e9426"
    )

    conflicts("platform=darwin")
    conflicts("platform=windows")

    depends_on("python@3.13", type=("build", "run"), when="@1.9.0-cp313")
    depends_on("python@3.12", type=("build", "run"), when="@1.9.0-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@1.9.0-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@1.9.0-cp310")

    with default_args(type="run"):
        depends_on("thrift@0.21.0 +python")
        depends_on("py-numpy@2")

    def url_for_version(self, version):
        split_name = self.name.split("-")[1:]
        dash_name = "-".join(split_name)
        underscored_name = "_".join(split_name)
        first_letter = dash_name[0]
        platform_tag = next(sys_tags()).platform
        if platform_tag in self.supported_tag:
            url = "https://pypi.io/packages/{1}/{3}/{4}/{5}-{0}-{1}-{1}-{2}.whl"
            pkg_ver = version.up_to_3
            cp_ver = version.string.split("-")[1]
            return url.format(
                pkg_ver, cp_ver, platform_tag, first_letter, dash_name, underscored_name
            )
        else:
            raise ValueError(f"Unsupported tag {tag}")
