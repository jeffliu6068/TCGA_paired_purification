from setuptools import setup

setup(
    name='tcga_paired_purification',
    version='0.1',
    author='Jeff Liu',
    author_email='jeffliu6068@gmail.com',
    packages=['tcga_paired_purification'],
    url='https://github.com/jeffliu6068/TCGA_paired_purification',
    license='LICENSE.txt',
    description='Implementation of the TCGA purification protocol',
    long_description=open('README.md').read(),
    install_requires=[
        'pandas',
        'scipy',
        'numpy',
        'matplotlib',
        'seaborn',
        'sklearn',
        'tqdm'
    ],
)
