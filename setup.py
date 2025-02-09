from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="leetdaily-cli",
    version="0.3.0",
    author="Prabhakaran K",
    author_email="prabhakaran.code@gmail.com",
    description="A CLI tool to view and interact with LeetCode's daily challenge.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/system1970/Leetcode-Daily-CLI",  # Replace with your GitHub repo URL
    packages=find_packages(),
    install_requires=[
        "requests",
        "click",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "daily=leetdaily.cli:daily",
            "submit=leetdaily.cli:submit",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)