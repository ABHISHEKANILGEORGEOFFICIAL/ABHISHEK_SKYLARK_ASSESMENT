import pandas as pd


def convert_to_dataframe(api_data):

    if "data" not in api_data:
        print(api_data)
        raise Exception("Monday API error. Check API key, board ID, or permissions.")

    items = api_data["data"]["boards"][0]["items_page"]["items"]

    rows = []

    for item in items:

        row = {"Item Name": item["name"]}

        for col in item["column_values"]:
            title = col["column"]["title"]
            value = col["text"]

            row[title] = value

        rows.append(row)

    df = pd.DataFrame(rows)

    return df


def clean_data(df):

    # Fill missing values
    df = df.fillna("Unknown")

    # Strip spaces
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    return df


def detect_data_issues(df):

    issues = []

    if df.isnull().sum().sum() > 0:
        issues.append("Some values are missing.")

    for col in df.columns:
        if df[col].dtype == "object":
            if (df[col] == "Unknown").sum() > 0:
                issues.append(f"Missing values in column {col}")

    return issues