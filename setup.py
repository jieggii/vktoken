from setuptools import setup


setup(
    name="vktoken",
    entry_points={"console_scripts": ["vktoken = vktoken.__main__:main"]},
)
