"""
Public interface for the ``tools`` package.

This package groups together utility modules for:

* Exploratory data analysis (``eda``)
* Audio processing and mel spectrogram generation (``mel_spectrograms``)
* Spanish phonetic and accent transformations (``phonemes``)
"""

from .eda import nulls, outliers, heatmap_correlation, pca_view
from .mel_spectrograms import load_audio_to_mel, graph_mel_spectrogram
from .phonemes import phoneme, accent, dictionaries, phoneme_graphs, embeddings

__all__ = [
    "nulls",
    "outliers",
    "heatmap_correlation",
    "pca_view",
    "load_audio_to_mel",
    "graph_mel_spectrogram",
    "phoneme",
    "accent",
    "dictionaries",
    "phoneme_graphs",
    "embeddings",
]

