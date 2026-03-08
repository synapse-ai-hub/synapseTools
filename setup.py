from pathlib import Path

from setuptools import find_packages, setup


ROOT = Path(__file__).parent


setup(
    name="synapseTools",
    version="0.1.2",
    description=(
        "Utility toolkit for data exploration, audio mel-spectrogram generation, "
        "and Spanish phonetic processing."
    ),
    long_description=(ROOT / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="SYNAPSE AI SAS",
    author_email="servicios@groupsynapseai.com",
    url="https://github.com/synapse-ai-hub/synapseTools",
    packages=find_packages(exclude=("tests", "tests.*", "examples", "examples.*")),
    install_requires=[
        "numpy>=1.24",
        "pandas>=1.5",
        "matplotlib>=3.7",
        "seaborn>=0.12",
        "scikit-learn>=1.3",
        "librosa>=0.10",
    ],
    extras_require={
        "eda": ["pandas>=1.5", "matplotlib>=3.7", "seaborn>=0.12", "scikit-learn>=1.3"],
        "mel": ["librosa>=0.10", "matplotlib>=3.7", "numpy>=1.24"],
        "phonemes": ["pandas>=1.5", "matplotlib>=3.7", "seaborn>=0.12", "numpy>=1.24"],
        "all": [
            "numpy>=1.24",
            "pandas>=1.5",
            "matplotlib>=3.7",
            "seaborn>=0.12",
            "scikit-learn>=1.3",
            "librosa>=0.10",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.9",
)