from distutils.core import setup

long_desc = """
A library that allows to use the K-Means algorithm using having the possibility to choose between multiple metrics to calculate the distance between the data points in the feature space.

This implementation is a fork of David Perez Delgado, you can find the original code in the following url:
https://github.com/dperede/KMeans-Multidistance

I forked this project in order to solve many problems. The original repository does not seem to be updated.

"""

setup(
    name='KMeans-python',
    version='1.0.3',
    description='K-Means implementation with multiple distance choices',
    long_description=long_desc,
    author='Mathias Quillot',
    author_email='mathiasquillot@gmail.com',
    url='https://github.com/mquillot/KMeans-python',
    download_url='https://github.com/mquillot/KMeans-python/archive/v1.0.3.tar.gz',
    install_requires=[
      'numpy>=1.15.4',
      'matplotlib>=3.0.2',
      'scikit-learn>=0.20.1'
    ],
    packages=['kmeans-python']
)
