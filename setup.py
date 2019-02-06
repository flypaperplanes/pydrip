import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    setuptools.setup(
     name='pydrip',
     version='0.1.8',
     author="Matthew Clarkson",
     author_email="mpclarkson@gmail.com",
     description="A Python 3 client for the Drip API.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/flypaperplanes/pydrip",
     packages=['pydrip'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )