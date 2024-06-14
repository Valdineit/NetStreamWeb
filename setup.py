from setuptools import setup, find_packages

setup(
    version="1.0",
    name="NetStream",
    packages=find_packages(),
    py_modules=["NetStream"],
    install_requires=[
        'openai-whisper',
    ],
    description="Automatically generate and embed subtitles into your videos",
    entry_points={
        'console_scripts': ['NetStream=auto_subtitle.cli:main'],
    },
    include_package_data=True,
)
