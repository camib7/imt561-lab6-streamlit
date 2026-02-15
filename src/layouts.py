import pandas as pd
import streamlit as st

from src.charts import plot_response_hist, plot_borough_bar


def header_metrics(df: pd.DataFrame) -> None:
    """Rendering header metrics. Placeholder values are intentional."""
    c1, c2, c3 = st.columns(3)

    total_complaints = len(df)

    median_response = df["response_time_days"].median()

    most_common = (
        df["complaint_type"].mode().iloc[0]
        if not df["complaint_type"].dropna().empty
        else "—"
    )

    # TODO (IN-CLASS): Replace these placeholders with real metrics from df
    # Suggestions:
    # - Total complaints (len(df))
    # - Median response time
    # - % from Web vs Phone vs App (pick one)
    with c1:
        st.metric(label="Total complaints", value=f"{total_complaints:,}")
    with c2:
        st.metric(label="Median response (days)", value=f"{median_response:.1f}")
    with c3:
        st.metric(label="Most common complaint", value=most_common)


def body_layout_tabs(df: pd.DataFrame) -> None:
    """Tabs layout with 3 default tabs."""
    t1, t2, t3 = st.tabs(["Distribution", "By Borough", "Table"])

    with t1:
        st.subheader("Response Time Distribution")
        plot_response_hist(df)

        # TODO (IN-CLASS): Add a short interpretation sentence under the chart
    st.caption("Most complaints are resolved within a short time, but a few take much longer.")
    with t2:
        st.subheader("Median Response Time by Borough")
        plot_borough_bar(df)

        # TODO (IN-CLASS): Add a second view here (e.g., count by borough)

    st.subheader("Complaint Count by Borough")

    counts = df["borough"].value_counts()
    st.bar_chart(counts)
    with t3:
        st.subheader("Filtered Rows")
        st.dataframe(df, use_container_width=True, height=480)

        # TODO (OPTIONAL): Add st.download_button to export filtered rows
        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download filtered data",
            data=csv,
            file_name="filtered_data.csv",
            mime="text/csv",
        )
