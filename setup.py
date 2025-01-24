from setuptools import find_packages, setup

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name='huggingpics',
    packages=find_packages(exclude=['examples']),
    version='0.0.1',
    license='MIT',
    description='🤗🖼️ HuggingPics: Fine-tune Vision Transformers for anything using images found on the web.',
    author='potnoodledev',
    author_email='me@potnoodle.dev',
    url='https://github.com/potnoodledev/huggingpics',
    install_requires=requirements,
)