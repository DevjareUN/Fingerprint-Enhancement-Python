from setuptools import setup, find_packages

setup(
    name='fpenhancer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "opencv-python==4.10.0.82",
        "scikit-image==0.23.2"
    ],
    url='https://github.com/DevjareUN/Fingerprint-Enhancement-Python',
)