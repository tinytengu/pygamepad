from setuptools import setup, find_packages

setup(
    name="pygamepad",
    version="0.1",
    description="A module that allows you to control your gamepad",
    url="http://github.com/tinytengu/pygamepad",
    author="tinytengu",
    author_email="tinytengu@yandex.ru",
    license="GPT-3",
    packages=find_packages(),
    zip_safe=False,
    install_requires=["inputs==0.5"],
)
