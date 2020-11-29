import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycuteweb",
    version="0.1.0",
    author="Matteo Meneghetti",
    author_email="matteo@meneghetti.dev",
    description="Package which aims to display webapps or websites on a desktop window",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matteomeneghetti/pycuteweb",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    install_requires=["pyside2"],
    python_requires='>=3.6'
)