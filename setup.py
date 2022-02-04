import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", encoding="utf-8") as fh:
    install_requires = fh.read().split('\n')

setuptools.setup(
    name="tncli",
    version="0.0.8",
    author="Andrey Tvorozhkov",
    author_email="andrey@head-labs.com",
    description="Easy to use CLI for fift / func projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/disintar/tncli",
    project_urls={
        "Bug Tracker": "https://github.com/disintar/tncli/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apple Public Source License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    package_dir={"": "src"},
    install_requires=install_requires,
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'tncli = tncli.main:main',
        ],
    }
)
