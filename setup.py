from setuptools import setupa, find_namespace_packages


with open("README.md", "r") as file:
    readme = file.read()


setup(
    name="grizzzly",
    version="0.1.0",
    description="This is your favorite data sharing library! Works great with pandas.",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_namespace_packages(where="src"),
    package_dir={
        "": "src"
    },
    scripts=[
        "bin/grizzzly"
    ]
)
