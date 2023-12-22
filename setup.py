from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name='st_deta_connection',
    version='0.0.3',
    description="A Streamlit component to connect to Deta Base and insert and fetch data from it.",
    packages=find_packages(),
    long_description=long_description,
    url="https://github.com/mohitrajsinha/st_deta_connection",
    long_description_content_type="text/markdown",
    author='Mohit Raj Sinha',
    author_email="mhtrajsinha@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'deta>=1.2.0',
        'streamlit>=1.29.0',
        'streamlit-option-menu>=0.3.6',
    ]
)