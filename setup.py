import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycuteweb",
    version="0.1.0",
    author="Matteo Meneghetti",
    author_email="matteo@meneghetti.dev",
    description="Display webapps, websites, or HTML content on a desktop window",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matteomeneghetti/pycuteweb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pyside2"],
    python_requires='>=3.6'
)