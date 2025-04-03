from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agentic_workspace",
    version="0.1.0",
    author="QuyThanh",
    author_email="tothanh1feb3.quinn@gmail.com",
    description="A Python module for parsing LLM outputs using Pydantic models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YinsenLabs/AgenticWorkspace",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    install_requires=[
        "pydantic>=2.0",
        "google-genai>=1.7.0",
        "python-dotenv>=1.0.1",
    ],
    extras_require={
        "dev": [
            "pytest>=8.1.1",
        ]
    },
    python_requires=">=3.8",
)
