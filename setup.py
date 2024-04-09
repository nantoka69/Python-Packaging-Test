from setuptools import setup, find_packages, find_namespace_packages

setup(
    name='nantoka-python-packaging-complex',
    version='1.1.1',
    packages=find_packages('source_root_1') + find_namespace_packages('source_root_2'),
    package_dir={
        '': 'source_root_1',
        'namespace_package': 'source_root_2/namespace_package'
    },
    install_requires=[
        'matplotlib>=3.8.0',
        "numpy~=1.26.4",
        "python-simple-packaging-test @ https://github.com/nantoka69/Python-Simple-Packaging-Test/releases/download/v1.0.0/python_simple_packaging_test-1.0.0-py3-none-any.whl"
    ],
    package_data={
        'package_1': ['data/*.json', 'data/*.html']
    },
    url='http://www.nantoka.de',
    license='MIT',
    author='Dr. Jörg Richter',
    author_email='python-book@nantoka.de',
    description='A complex test for setuptools'
)
