from setuptools import setup, find_packages, find_namespace_packages

setup(
    name='nantoka-python-packaging-complex',
    version='1.1.0',
    packages=find_packages('source_root_1') + find_namespace_packages('source_root_2'),
    package_dir={
        '': 'source_root_1',
        'namespace_package': 'source_root_2/namespace_package'
    },
    install_requires=[
        'matplotlib>=3.8.0',
        "numpy~=1.26.4",
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
