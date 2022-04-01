from setuptools import setup, find_namespace_packages


with open("README.md", "r") as file:
    readme = file.read()

with open("requirements.txt", "r") as file:
    install_requirements = file.read().splitlines()


setup(
    name="grizzzly",
    version="0.1.2",
    description="This is your favorite data sharing library! Works great with pandas.",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_namespace_packages(where="src"),
    install_requires=install_requirements,
    package_dir={
        "": "src"
    },
    scripts=[
        "bin/grizzzly"
    ]
)
