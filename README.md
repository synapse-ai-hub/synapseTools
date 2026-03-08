<p align="center">
  <img src="https://raw.githubusercontent.com/synapse-ai-hub/synapseTools/main/src/LogoBlancoGrande2.png" alt="Logo synapse.ai" width="150">
</p>

<h1 align="center">synapseTools</h1>

<p align="center">
  <a href="https://github.com/synapse-ai-hub/synapseTools/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="License: Apache 2.0" />
  </a>
</p>

<h3 align="center">Data exploration, audio features, and Spanish phonetics in one toolbox</h3>

---

## Overview

`synapseTools` is a utility library maintained by **SYNAPSE AI SAS** that currently includes:

- **Exploratory data analysis (EDA)**: functions for null detection, outlier analysis, correlation heatmaps, and PCA visualization.
- **Audio processing**: mel-spectrogram generation and visualization for audio workflows.
- **Spanish phonetics**: phoneme and accent transformations tailored for Rioplatense Spanish.

This is an **evolving project** designed as the foundation for a comprehensive framework to work with data, AI, and autonomous agents. We are continuously expanding the toolkit with new features and capabilities.

Core principles:

- **Practical** – simple, focused functions with sensible defaults.
- **Composable** – integrate easily into your pipelines and notebooks.
- **Minimal dependencies** – no heavy deep-learning frameworks required unless you opt for specific extras.

---

## Installation

```bash
pip install synapseTools
```

The package targets **Python 3.8+**.

If you want to install only specific feature sets you can use extras:

```bash
# Full installation (equivalent to base install)
pip install "synapseTools[all]"

# Only EDA utilities
pip install "synapseTools[eda]"

# Only audio / mel-spectrogram utilities
pip install "synapseTools[mel]"

# Only phoneme / accent tools
pip install "synapseTools[phonemes]"
```

> For reproducible environments, we recommend using `python -m venv` or a tool
> like `uv`, `poetry`, or `pipenv`.

---

## Modules

### `synapse_tools.eda`

Utilities for quick exploratory data analysis on `pandas.DataFrame` objects.

- **`nulls(data, column)`** – prints count and percentage of nulls in a column.
- **`outliers(data, column, ...)`** – histogram + boxplot + descriptive statistics and IQR-based outlier detection, with optional dictionary output.
- **`heatmap_correlation(data, columns, ...)`** – Spearman/Pearson correlation heatmap with save/show options.
- **`pca_view(data, dimensions, target=None, ...)`** – runs PCA (2D or 3D) with optional scaling and target coloring.

These functions are handy when you want fast, visual feedback about a dataset
without writing a lot of boilerplate plotting code.

### `synapse_tools.mel_spectrograms`

Helpers for turning audio files into mel spectrograms and plotting them.

- **`load_audio_to_mel(file_path, sr=22050, ...)`** – loads an audio file, normalizes it, and returns a mel spectrogram as a NumPy array.
- **`graph_mel_spectrogram(spectrogram, output_dir='', name='Spectrogram', ...)`** – visualizes (and optionally saves) a mel spectrogram image.

This is especially useful in speech and TTS workflows where you need a
repeatable way to extract and inspect mel features.

### `synapse_tools.phonemes`

Rule-based utilities focused on **Rioplatense Spanish** (Argentina / Uruguay).

- **`phoneme(text, punctuation=False)`** – converts Spanish text into a simplified phoneme sequence using deterministic rules.
- **`accent(text, punctuation=False)`** – applies prosodic accentuation based on Spanish stress rules.
- **`dictionaries(text, order_by_frequency=True, pad=True)`** – builds phoneme-to-index and frequency dictionaries for modeling.
- **`phoneme_graphs(tokens, quantity, ...)`** – bar chart of phoneme frequencies.
- **`embeddings(input_dim, output_dim, std, ...)`** – frequency-aware initialization matrix for embedding layers.

These tools are designed to play nicely with downstream NLP / TTS models, where
you often need custom tokenization and embeddings.

---

## Basic usage

```python
import pandas as pd
from synapse_tools import nulls, outliers, heatmap_correlation, load_audio_to_mel, graph_mel_spectrogram, phoneme

# EDA
df = pd.read_csv("data.csv")
nulls(df, "age")
outliers(df, "salary")

# Audio
mel = load_audio_to_mel("audio.wav")
graph_mel_spectrogram(mel, name="example")

# Phonetics (Rioplatense Spanish)
phoneme_text = phoneme("Esta es una oración de prueba.")
print(phoneme_text)
```

---

## Contributing

If you want to contribute, see [CONTRIBUTING.md](https://github.com/synapse-ai-hub/synapseTools/blob/main/CONTRIBUTING.md).

---

## License

This project is licensed under the **Apache 2.0** license. See [LICENSE](https://github.com/synapse-ai-hub/synapseTools/blob/main/LICENSE) for details.