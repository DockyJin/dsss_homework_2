from setuptools import setup,find_packages

setup(
    name="math_quiz",
    version="0.1",
    author="dsss_homework_2",
    author_email="dockyjin@gamil.com",
    description="a math quiz in python",
    packages=find_packages(),
    python_requires=">3",
    install_requires=["numpy","turtles"]
)
