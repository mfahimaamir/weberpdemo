import streamlit as st
import pandas as pd
import altair as alt
import random
from faker import Faker

fake = Faker("en-US")

#st.set_page_config(layout="wide")
st.subheader("Client Side Filtering using Altair Selections")
df = pd.DataFrame(range(1, 10001), columns=["ID"])
df["country"] = df.apply(lambda r: fake.country(), axis=1)
df["transaction"] = df.apply(lambda x: random.random() * 100, axis=1)

df = (
    df[["transaction", "country"]]
    .groupby("country")
    .sum("transaction")
    .reset_index("country")
)
df["transaction"] = df.apply(lambda x: round(x["transaction"], 2), axis=1)

slider = alt.binding_range(
    min=df["transaction"].min(),
    max=df["transaction"].max(),
    step=1,
    name="Transactions Lower or Equal than:",
)
selector = alt.selection_single(
    fields=["threshold"],
    bind=slider,
    init={"threshold": df["transaction"].max()},
)

base = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x="country:N",
        y="transaction",
        color=alt.condition(
            alt.datum.transaction <= selector.threshold,
            alt.value("blue"),
            alt.value("lightgray"),
        ),
    )
    .add_selection(selector)
).properties(width=1000)
selected = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x="country:N",
        y="transaction:Q",
        color=alt.value("orange"),
    )
    .transform_filter(alt.datum.transaction <= selector.threshold)
).properties(width=1000)

st.altair_chart(base & selected, use_container_width=True)