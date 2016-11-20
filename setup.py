from setuptools import setup, find_packages
from subprocess import call


setup(name='java_pip_test',
      version='0.1',
      description='Hello World From Java using PIP packaging',
      url='https://github.com/PerArneng/javapiptest',
      author='Per Arneng',
      author_email='per.arneng@scalebit.com',
      license='APACHE 2.0',
      packages=['target'],
      entry_points={
            'console_scripts': ['java_pip_test=target.bootstrap:main'],
      },
      package_data={'target': ['*.jar']},
      zip_safe=False)

