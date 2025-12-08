"""
Setup script para ML Boilerplate.
"""

from setuptools import setup, find_packages
import os

# Ler o README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Ler requirements
def read_requirements(filename):
    """Lê os requirements de um arquivo."""
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Requirements principais
install_requires = read_requirements('requirements.txt')

# Requirements de desenvolvimento
dev_requires = read_requirements('requirements-dev.txt')

setup(
    name="ml-boilerplate",
    version="1.0.0",
    author="ML Boilerplate Team",
    author_email="ml@example.com",
    description="Template completo para projetos de Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ml-boilerplate/ml-boilerplate-python-jupyter",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.12",
    install_requires=install_requires,
    extras_require={
        'dev': dev_requires,
        'all': install_requires + dev_requires,
    },
    include_package_data=True,
    package_data={
        'ml_boilerplate': [
            'config/*.py',
            'notebooks/*.ipynb',
            'data/raw/.gitkeep',
            'data/processed/.gitkeep',
            'data/external/.gitkeep',
            'data/interim/.gitkeep',
            'models/.gitkeep',
            'reports/figures/.gitkeep',
            'tests/.gitkeep',
        ],
    },
    entry_points={
        'console_scripts': [
            'ml-setup=src.setup_project:main',
        ],
    },
    zip_safe=False,
)