import marimo

__generated_with = "0.18.0"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    from pathlib import Path
    from sklearn.preprocessing import LabelEncoder
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import roc_auc_score
    return (
        LabelEncoder,
        Path,
        RandomForestClassifier,
        pd,
        roc_auc_score,
        train_test_split,
    )


@app.cell
def _(Path, pd):
    # データの取得
    BASE_DIR = Path(__file__).resolve().parent
    train = pd.read_csv(BASE_DIR / "data" / "train.csv")
    test = pd.read_csv(BASE_DIR / "data" / "test.csv")

    train.info()
    return test, train


@app.cell
def _(LabelEncoder, test, train):
    # カテゴリ列を特定
    categorical_columns = train.select_dtypes(include=['object']).columns

    # 各カテゴリ列をエンコード
    label_encoders = {}
    for column in categorical_columns:
        le = LabelEncoder()
        train[column] = le.fit_transform(train[column])
        label_encoders[column] = le

    # カテゴリ列を特定（文字列型またはオブジェクト型）
    categorical_columns = test.select_dtypes(include=['object']).columns

    # 各カテゴリ列をエンコード
    label_encoders = {}
    for column in categorical_columns:
        le = LabelEncoder()
        # ラベルエンコードを適用
        test[column] = le.fit_transform(test[column].astype(str))
        label_encoders[column] = le

    # 前処理後の最初の数行を表示
    train.head()
    return


@app.cell
def _(RandomForestClassifier, train, train_test_split):
    # データ分割
    X=train.drop(columns=["id","loan_status"],axis=1)
    y=train["loan_status"]

    # 学習用データとテスト用データに分割
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # ランダムフォレストを使用してモデル構築
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # テストデータで予測
    y_pred = model.predict(X_test)

    print(y_pred)
    return y_pred, y_test


@app.cell
def _(roc_auc_score, y_pred, y_test):
    # 評価
    roc_auc=roc_auc_score(y_test,y_pred)
    print(roc_auc)
    return


if __name__ == "__main__":
    app.run()
