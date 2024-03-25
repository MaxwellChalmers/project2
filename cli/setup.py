from setuptools import setup

setup(
    name="main",
    version="0.1.0",
    py_modules=["main"],
    install_requires=["Click", "requests"],
    entry_points={
        "console_scripts": [
            "gif = main:main",
        ],
    },
)
