import setuptools

from dyepy import (
    __name__, __author__, __email__, __github__, __version__, __desc__
)


with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    description=__desc__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=__github__,
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=['typing'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
