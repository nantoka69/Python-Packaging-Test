from setuptools import setup
setup(
    name='Python Packaging Test',
    version='1.1.0',
    packages=['package_1', 'package_2'],
    package_dir={'package_1': 'source_root_1', 'package_2': 'source_root_2'},
    url='http://www.nantoka.de',
    license='MIT',
    author='Dr. Jörg Richter',
    author_email='python-book@nantoka.de',
    description='A test package for using setuptools'
)
