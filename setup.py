from setuptools import setup, find_packages

setup(
    name="swathcake",
    version="0.0.3",
    author="Lorenz Blum",
    maintainer=['Lorenz Blum', 'Witold Wolski'],
    author_email="blum@id.ethz.ch",
    maintainer_email=["blum@id.ethz.ch",'wewolski@gmail.com'],
    description="SWATH analysis workflow with OpenSWATH,pyprophet and featurealigner, starting from mzXML files",
    license="BSD",
    packages=find_packages(),
    url='https://github.com/applicake-tools/swathcake',
    install_requires=['Unimod','applicake', 'pyteomics', 'ruffus', 'configobj']
)
