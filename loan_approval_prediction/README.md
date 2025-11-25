# Loan Approval Prediction

https://www.kaggle.com/competitions/playground-series-s4e10/overview

## Setup

### kaggle.json

Kaggleの[Settingページ](https://www.kaggle.com/settings)の`Legacy API Credentials`からkaggle.jsonを取得してください。

```bash
mv /path/to/download/kaggle.json /Users/{your name}/.kaggle/kaggle.json
chmod 600 /Users/{your name}/.kaggle/kaggle.json
```

### download dataset

```bash
uv run kaggle competitions download -c playground-series-s4e10 -p loan_approval_prediction/data
unzip loan_approval_prediction/data/playground-series-s4e10.zip -d loan_approval_prediction/data
```

## Run sample model notebook

```bash
uv run marimo edit loan_approval_prediction/sample_nb.py
```