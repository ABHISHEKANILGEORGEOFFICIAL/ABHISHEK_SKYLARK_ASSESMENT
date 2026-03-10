import pandas as pd

def pipeline_summary(df):

    result = {}

    result["total_items"] = len(df)

    # sector distribution
    if "Text 5" in df.columns:
        result["sector_distribution"] = df["Text 5"].value_counts().to_dict()

    # revenue calculation
    if "Text 3" in df.columns:
        df["Text 3"] = pd.to_numeric(df["Text 3"], errors="coerce")
        result["total_revenue"] = df["Text 3"].sum()

    return result

    

def leadership_report(deals_df, workorders_df):

    report = {}

    report["total_deals"] = len(deals_df)

    if "Revenue" in deals_df.columns:
        try:
            deals_df["Revenue"] = deals_df["Revenue"].astype(float)
            report["pipeline_value"] = deals_df["Revenue"].sum()
        except:
            report["pipeline_value"] = "Revenue formatting issue"

    report["active_work_orders"] = len(workorders_df)

    return report