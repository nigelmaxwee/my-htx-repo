# my-htx-repo
# Automated Speech Recognition (ASR)

## Objective
<p align="justify">
To fine-tune an Automatic Speech Recognition (ASR) model using the Common Voice dataset and evaluate its performance against the pre-trained wav2vec2-large-960h model. Additionally, by implementing hotword detection, we aim to identify critical phrases such as "be careful," "destroy," and "stranger," leveraging a text embedding model for similarity analysis. The goal is to develop a customized, high-accuracy ASR system that can effectively recognize domain-specific vocabulary in real-world applications.
</p>

## Dataset
</p>
Download link: https://www.dropbox.com/scl/fi/i9yvfqpf7p8uye5o8k1sj/common_voice.zip?rlkey=lz3dtjuhekc3xw4jnoeoqy5yu&e=1&dl=0
</p>

## Directories

<pre> ``` 📦 your-project-root/ ├── .gitattributes ├── .gitignore ├── README.md ├── essay-ssl.pdf ├── training-report.pdf │ ├── asr/ │ ├── asr_api.py │ ├── cv-decode.py │ ├── cv-valid-dev.csv │ ├── Dockerfile │ ├── requirements.txt │ ├── wav2vec2-large-960h-cv/ │ │ ├── config.json │ │ ├── model.safetensors │ │ ├── preprocessor_config.json │ │ ├── special_tokens_map.json │ │ ├── tokenizer_config.json │ │ └── vocab.json │ ├── baseline_dev_set_metrics.csv │ ├── cv_train_2a.ipynb │ ├── finetuned_dev_set_metrics.csv │ ├── loss_history.csv │ ├── test_set_metrics.csv │ ├── train_val_loss_plot.png │ ├── wer_cer_metrics.csv │ └── wer_cer_plot.png │ ├── data/ │ ├── cv-valid-dev/ │ ├── cv-valid-train/ │ ├── cv-valid-dev.csv │ └── cv-valid-train.csv │ ├── hotword-detection/ │ ├── cv_hotword_5a.ipynb │ ├── cv_hotword_similarity_5b.ipynb │ ├── cv-valid-dev_filtered_keywords.csv │ ├── cv-valid-dev_predictions.csv │ ├── cv-valid-dev-similarity.csv │ └── detected.txt │ ├── requirements.txt └── requirements2.txt ``` </pre>

## Step 1. Clone GitHub repository 
```
git clone https://github.com/nigelmaxwee/my-htx-repo.git
cd my-htx-repo
```

