
<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/CodexEsto/textpipe">
    <img src="assets/textpipeRB.png" alt="Logo" width="230" height="150">
  </a>

  <h3 align="center">textpipe</h3>

  <p align="center">
    Modern text processing pipeline for machine learning applications
    <br />
    <br />
    <a href="https://github.com/CodexEsto/textpipe/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/CodexEsto/textpipe/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

textpipe is an end-to-end text processing pipeline designed for modern NLP workflows. It provides:

- **Configurable Processing**: YAML-based configuration for all processing steps
- **Modular Architecture**: Clean separation of data loading, cleaning, vectorization, and modeling
- **Production Ready**: Built-in logging, error handling, and type validation
- **ML Integration**: Seamless integration with scikit-learn models
- **Customizable Components**:
  - Multiple text cleaning strategies
  - Configurable tokenization (stemming, stopwords)
  - TF-IDF vectorization with automatic feature management
  - Extensible model architecture

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Installation

Install the package with pip:
```bash
pip install textpipe
```

**Update existing installation:**
```bash
pip install textpipe --upgrade
```

### Usage

Basic text processing pipeline example:

```python
from textpipe import Config, load_csv, SentimentPipeline

# Initialize configuration
config = Config.get()

# Load training data
texts, labels = load_csv("data/train.csv")

# Initialize and train pipeline
pipeline = SentimentPipeline(config)
pipeline.train(texts, labels)

# Make predictions
new_texts = ["I love this product!", "Terrible service..."]
predictions = pipeline.predict(new_texts)
print(predictions)
```

Advanced configuration example (`config.yml`):
```yaml
processing:
  language: english
  remove_stopwords: true
  use_stemming: false
  max_features: 5000
  min_text_length: 3
logging:
  level: INFO
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community an amazing place to learn, inspire, and create. Any contributions are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top Contributors:

<a href="https://github.com/CodexEsto/textpipe/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=CodexEsto/textpipe" alt="Project Contributors" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Textpipe Team - your.email@example.com

Project Link: [https://github.com/CodexEsto/textpipe](https://github.com/CodexEsto/textpipe)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- Scikit-learn community for foundational ML components
- NLTK team for language processing resources
- Pandas for data handling capabilities
- All contributors and open-source maintainers who inspired this work

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/CodexEsto/textpipe.svg?style=for-the-badge
[contributors-url]: https://github.com/CodexEsto/textpipe/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/CodexEsto/textpipe.svg?style=for-the-badge
[forks-url]: https://github.com/CodexEsto/textpipe/network/members
[stars-shield]: https://img.shields.io/github/stars/CodexEsto/textpipe.svg?style=for-the-badge
[stars-url]: https://github.com/CodexEsto/textpipe/stargazers
[issues-shield]: https://img.shields.io/github/issues/CodexEsto/textpipe.svg?style=for-the-badge
[issues-url]: https://github.com/CodexEsto/textpipe/issues
[license-shield]: https://img.shields.io/github/license/CodexEsto/textpipe.svg?style=for-the-badge
[license-url]: https://github.com/CodexEsto/textpipe/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/your-profile/
```
