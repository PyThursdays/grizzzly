from setuptools import setup


setup(
    name="grizzzly",
    version="0.1.0",
    description="This is your favorite data sharing library! Works great with pandas.",
    package_dir={
        "": "src"
    },
    scripts=[
        "bin/grizzzly"
    ]
)
