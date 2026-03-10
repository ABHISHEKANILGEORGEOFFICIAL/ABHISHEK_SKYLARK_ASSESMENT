import streamlit as st
import plotly.express as px

from monday_api import fetch_board_data
from data_processor import convert_to_dataframe, clean_data, detect_data_issues
from analytics import pipeline_summary, leadership_report
from llm_agent import generate_response

st.set_page_config(page_title="Founder BI Agent")

st.title("📊 Monday.com Founder Intelligence Agent")

st.write("Ask business questions about deals and work orders.")

deals_board_id = st.text_input("Deals Board ID")
workorders_board_id = st.text_input("Work Orders Board ID")

query = st.text_input("Ask a question")

if st.button("Run Analysis"):

    st.write("Fetching data from Monday.com...")

    deals_raw = fetch_board_data(deals_board_id)
    work_raw = fetch_board_data(workorders_board_id)

    deals_df = convert_to_dataframe(deals_raw)
    work_df = convert_to_dataframe(work_raw)

    deals_df = clean_data(deals_df)
    work_df = clean_data(work_df)

    issues = detect_data_issues(deals_df)

    if issues:
        st.warning("Data Quality Issues Detected")
        for i in issues:
            st.write("-", i)

    analysis_output = None

    if "pipeline" in query.lower():

        analysis_output = pipeline_summary(deals_df)

        st.subheader("Pipeline Summary")
        st.json(analysis_output)

        if "sector_distribution" in analysis_output:

            chart_data = analysis_output["sector_distribution"]

            fig = px.bar(
                x=list(chart_data.keys()),
                y=list(chart_data.values()),
                labels={"x": "Sector", "y": "Deals"},
                title="Deals by Sector"
            )

            st.plotly_chart(fig)

    elif "leadership" in query.lower():

        analysis_output = leadership_report(deals_df, work_df)

        st.subheader("Leadership Update")
        st.json(analysis_output)

    else:

        st.write("Try questions like:")
        st.write("- How is our pipeline?")
        st.write("- Show leadership update")

    if analysis_output:

        response = generate_response(query, analysis_output)

        st.subheader("AI Insight")
        st.write(response)