import setuptools

setuptools.setup(
    name="docs_exp",
    version="0.1.0",
    url="https://github.com/piqueen314/docs_exp",

    author="cece hedrick",
    author_email="cecehedrick@gmail.com",

    description="An opinionated, minimal cookiecutter template for Python packages",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
