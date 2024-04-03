import os

from package_1.module_1 import module_1_hello

from package_1.sub_package_1 import *
from package_1.sub_package_1 import subpackage_3_hello

from package_1 import submodule_1_hello

from namespace_package.namespace_module import module_2_hello

# This still does work
# from package_1.subpackage_1.submodule_1 import submodule_1_hello

python_path = os.environ.get('PYTHONPATH', '')

if python_path:
    paths = python_path.split(os.pathsep)
    print("PYTHONPATH contains the following directories:")
    for path in paths:
        print(path)
else:
    print("PYTHONPATH is not set.")

module_1_hello()
module_2_hello()

subpackage_1_hello()
subpackage_3_hello()
# This does not work
# subpackage_1_hello_2()

submodule_1_hello()
