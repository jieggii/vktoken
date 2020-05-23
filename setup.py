from setuptools import setup

version = "1.0.1"

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="vktoken",
    author="jieggii",
    license="GPL-3.0",
    python_requires=">=3.6",
    install_requires=["requests", "pyperclip"],
    version=version,
    description="A tool for getting VK access token",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jieggii/vktoken",
    author_email="jieggii.contact@gmail.com",
    packages=["vktoken"],
    project_urls={
        "Source": "https://github.com/jieggii/vktoken",
        "Tracker": "https://github.com/jieggii/vktoken/issues",
    },
    entry_points={"console_scripts": ["vktoken = vktoken.main:main"]},
)
