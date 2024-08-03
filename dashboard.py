import firebase_admin
from firebase_admin import credentials, firestore

import streamlit as st


cred = credentials.Certificate("service_account.json")
default_app = firebase_admin.initialize_app(cred)
# Initialize Firestore DB
db = firestore.client()


docs = db.collection("userdata").stream()
for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")

# Sidebar
st.sidebar.title("Analysis")

selected_option = st.sidebar.selectbox(
    "Select Option", ["Bar Chart", "Line Chart", "Scatter Plot"]
)

#  total sale count
# total_usrs = len()

# average purchase amount
# average_purchase_amount = data["Purchase Amount (USD)"].mean()


# st.title("Dashboard")


# st.sidebar.subheader("Total Sale Count")
# st.sidebar.write(total_sale_count)


# st.sidebar.subheader("Average Purchase Amount")
# st.sidebar.write("$" + str(round(average_purchase_amount, 2)))

# if selected_option == "Bar Chart":
#     st.header("Bar Chart")
#     fig = px.bar(
#         data,
#         x="Category",
#         y="Purchase Amount (USD)",
#         color="Gender",
#         title="Distribution of Purchases by Product Category",
#     )
#     st.plotly_chart(fig)

# elif selected_option == "Line Chart":
#     st.header("Line Chart")

#     fig = px.line(
#         data,
#         x="Customer ID",
#         y="Purchase Amount (USD)",
#         color="Gender",
#         title="Trend in Sales Over Time",
#     )
#     st.plotly_chart(fig)

# elif selected_option == "Scatter Plot":
#     st.header("Scatter Plot")

#     fig = px.scatter_3d(
#         data,
#         x="Age",
#         y="Purchase Amount (USD)",
#         z="Customer ID",
#         color="Gender",
#         title="Relationship between Customer Age and Purchase Amount",
#     )
#     st.plotly_chart(fig)
