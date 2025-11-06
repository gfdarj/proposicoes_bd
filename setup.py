from setuptools import setup, find_packages

setup(
    name="proposicoes_db",
    version="1.0.0",
    author="Gilberto Almeida",
    author_email="gfdarj@gmail.com",  # opcional
    description="Biblioteca Python para integração com banco de dados MS Access",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gfdarj/proposicoes_db",  # opcional
    packages=find_packages(),  # encontra automaticamente a subpasta proposicoes_db/
    python_requires=">=3.13",
    install_requires=[
        "pyodbc>=4.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ],
)
