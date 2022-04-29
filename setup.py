from setuptools import setup, find_packages


with open("README.md", "r") as file:
    readme = file.read()

with open("requirements.txt", "r") as file:
    install_requirements = file.read().splitlines()


setup(
    name="grizzzly",
    version="0.6.0",
    description="This is your favorite data sharing library! Works great with pandas.",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    install_requires=install_requirements,
    package_dir={
        "": "src"
    },
    entry_points={
        "console_scripts": [
            "grizzzly=grizzzly:start_cli"
        ]
    },
    scripts=[
        "bin/grizzzly"
    ]
)
