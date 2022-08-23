from setuptools import setup, find_packages

__version__ = "1.0.0"

with open("README.md") as description_file:
    readme = description_file.read()

with open("requirements.txt") as requirements_file:
    requirements = [line for line in requirements_file]

setup(
    name="ceps_ranger",
    version=__version__,
    author="author",
    description="Python project is a sample project for learning python.",
    python_requires=">=3.8.8",
    url="https://github.com/eronlivramento/leech.git",
    packages=find_packages(),
    long_description=readme,
    include_package_data=True,
    install_requires=requirements,
)
