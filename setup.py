from setuptools import setup
import pathlib

long_description = pathlib.Path(__file__).parent.joinpath("README.md").read_text()

setup(
    name="cv2operator",
    packages=["cv2operator"],
    version="1.0.1",
    license="MIT",
    author="fukuda, minoru",
    url="https://github.com/moicci/cv2operator",
    description="a simple library to input various shapes like polygon rectangle and so on.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="opencv cv2 operation",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ]
)
