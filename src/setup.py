from setuptools import setup, find_packages

setup(
    name="coolutils",
    version="1.0.0",
    author="TitanStar73",
    author_email="",
    description="A cool utility library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TitanStar73/coolutils",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    project_urls={
        "Source": "https://github.com/TitanStar73/coolutils",
    },
)
