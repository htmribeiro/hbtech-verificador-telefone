from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name="hbtech-verificador-telefone",
    version="0.0.2",
    author="Hamilton Ribeiro",
    author_email="hamilton.ribeiro@hbtechcompany.onmicrosoft.com",
    description="Get info which city a phone number belong to",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/htmribeiro/hbtech-verificador-telefone.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'    
)