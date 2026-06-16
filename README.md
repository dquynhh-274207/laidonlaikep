import streamlit as st

st.set_page_config(
    page_title="Ứng dụng tính tiền gửi tiết kiệm",
    page_icon="DIEMQUYNH.JPG"
)
# Tiêu đề ứng dụng
col1, col2 = st.columns([1, 6])

with col1:
    st.image("DIEMQUYNH.JPG", width=432)

with col2:
    st.title("Ứng dụng tính tiền gửi tiết kiệm_Diễm Quỳnh")

# Nhập dữ liệu
C = st.number_input(
    "Nhập số tiền khách hàng gửi tiết kiệm (triệu đồng)",
    min_value=0.0,
    value=100.0
