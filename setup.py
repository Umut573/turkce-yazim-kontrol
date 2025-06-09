from setuptools import setup, find_packages

setup(
    name="turkyazim",
    version="1.2.0",
    packages=find_packages(),
    install_requires=[
        "zemberek-python",
        "python-Levenshtein",
        "transformers",
        "torch",
        "fastapi",
        "uvicorn",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "turkyazim=turkyazim.cli:main"
        ]
    },
    author="Umut573",
    description="Gelişmiş Türkçe Yazım Denetleyici - Zemberek + BERT + TDK",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kullaniciadi/turkce-yazim-kontrol", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
