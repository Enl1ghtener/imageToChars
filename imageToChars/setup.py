from setuptools import setup, find_packages

VERSION = '1.0'
DESCRIPTION = 'imageToChars package'
LONG_DESCRIPTION = 'Convert image to character drawing'

# ≈‰÷√
setup(
    name="imageToChars",
    version=VERSION,
    author="YuMu chen",
    author_email="<yumuc000@outlook.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
