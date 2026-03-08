<p align="center">
  <img src="https://raw.githubusercontent.com/synapse-ai-hub/synapse-tools/main/src/LogoBlancoGrande2.png" alt="Logo synapse.ai" width="150">
</p>

<h1 align="center">synapse-tools</h1>

<p align="center">
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="License: Apache 2.0" />
  </a>
</p>

<h3 align="center">Data exploration, audio features, and Spanish phonetics in one toolbox</h3>

---

## Overview

`synapse-tools` is a small utility library maintained by **SYNAPSE AI SAS** that
groups together tools we use every day for:

- **Exploratory data analysis (EDA)**: quick checks for nulls, outliers, correlations and PCA views.
- **Audio processing**: mel-spectrogram generation and visualization, ready for TTS / speech workflows.
- **Spanish phonetics**: rule-based phoneme and accent transformations tuned for Rioplatense Spanish.

It is designed to be:

- **Practical** – simple functions with sensible defaults.
- **Composable** – you can plug them into your own pipelines and notebooks.
- **Focused** – only tools we actually use in projects, without heavy deep-learning dependencies.

---

## Installation

```bash
pip install synapse-tools
```

The package targets **Python 3.8+**.

If you want to install only specific feature sets you can use extras:

```bash
# Full installation (equivalent to base install)
pip install "synapse-tools[all]"

# Only EDA utilities
pip install "synapse-tools[eda]"

# Only audio / mel-spectrogram utilities
pip install "synapse-tools[mel]"

# Only phoneme / accent tools
pip install "synapse-tools[phonemes]"
```

> For reproducible environments, we recommend using `python -m venv` or a tool
> like `uv`, `poetry`, or `pipenv`.

---

## Modules

### `tools.eda`

Utilities for quick exploratory data analysis on `pandas.DataFrame` objects.

- **`nulls(data, column)`** – prints count and percentage of nulls in a column.
- **`outliers(data, column, ...)`** – histogram + boxplot + descriptive statistics and IQR-based outlier detection, with optional dictionary output.
- **`heatmap_correlation(data, columns, ...)`** – Spearman/Pearson correlation heatmap with save/show options.
- **`pca_view(data, dimensions, target=None, ...)`** – runs PCA (2D or 3D) with optional scaling and target coloring.

These functions are handy when you want fast, visual feedback about a dataset
without writing a lot of boilerplate plotting code.

### `tools.mel_spectrograms`

Helpers for turning audio files into mel spectrograms and plotting them.

- **`load_audio_to_mel(file_path, sr=22050, ...)`** – loads an audio file, normalizes it, and returns a mel spectrogram as a NumPy array.
- **`graph_mel_spectrogram(spectrogram, output_dir='', name='Spectrogram', ...)`** – visualizes (and optionally saves) a mel spectrogram image.

This is especially useful in speech and TTS workflows where you need a
repeatable way to extract and inspect mel features.

### `tools.phonemes`

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
from tools import nulls, outliers, heatmap_correlation, load_audio_to_mel, graph_mel_spectrogram, phoneme

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

If you want to contribute, see [CONTRIBUTING.md](./CONTRIBUTING.md).

---

## License

This project is licensed under the **Apache 2.0** license. See [LICENSE](./LICENSE) for details.