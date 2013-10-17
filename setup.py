from setuptools import setup, find_packages

version = '1.0.0'
setup(
    name='specifications',
    version=version,
    description='Composite Specification implementation',
    author='Doug Hurst',
    author_email='dalan.hurst@gmail.com',
    maintainer='Doug Hurst',
    license='MIT',
    url='https://github.com/dalanhurst/python-specifications',
    packages=find_packages(exclude=['tests']),
    download_url='http://pypi.python.org/packages/source/r/specifications/specifications-%s.tar.gz' % version,
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries"]
)
