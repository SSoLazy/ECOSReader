import setuptools

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="open_ecos_reader", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="rkr638@naver.com",
    description="Python package for ECOS, that is open API of the bank of korea.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SSoLazy/OpenECOSReader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
