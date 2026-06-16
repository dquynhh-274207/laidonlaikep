import streamlit as st
import os

# Cấu hình giao diện và tiêu đề tab trình duyệt
st.set_page_config(
    page_title="Ứng dụng tính tiền gửi tiết kiệm - Diễm Quỳnh", 
    page_icon="💰",
    layout="centered"
)

st.title("💰 Ứng dụng tính tiền gửi tiết kiệm_Diễm Quỳnh")

# Danh sách các tên file ảnh của Diễm Quỳnh trên GitHub
cac_ten_file_anh_pho_bien = [
    "diemquynh.jpg", 
    "diemquynh.png", 
    "DIEMQUYNH.JPG", 
    "DIEMQUYNH.PNG"
]

anh_tim_thay = None

# Tự động quét xem file ảnh nào đang có sẵn trên kho GitHub của bạn
for ten_file in cac_ten_file_anh_pho_bien:
    if os.path.exists(ten_file):
        anh_tim_thay = ten_file
        break

# Hiển thị ảnh nếu tìm thấy, ngược lại thì hiện hướng dẫn nhẹ nhàng chứ không báo lỗi đỏ
if anh_tim_thay:
    st.image(anh_tim_thay, width=300, caption="Ảnh đại diện xinh xắn của Diễm Quỳnh nè! ✨")
else:
    st.info(
        "💡 **Tin nhắn từ trợ lý:** Quỳnh ơi! Bạn chưa tải file ảnh lên GitHub "
        "hoặc đặt tên ảnh chưa đúng rồi.\n\n"
        "👉 Hãy chọn một bức ảnh trên máy, đổi tên file thành **`diemquynh.jpg`** "
        "rồi tải lên GitHub (bằng nút *Add file -> Upload files*) là ảnh sẽ hiện ở đây ngay nha!"
    )

st.write("---")

st.subheader("🧮 Công cụ tính toán lãi kép")

sotien = st.number_input(
    "Nhập số tiền gửi tiết kiệm ban đầu (triệu đồng)", 
    min_value=0.0, 
    value=100.0, 
    step=1.0
)

laisuat = st.number_input(
    "Nhập lãi suất gửi tiết kiệm theo năm (%)", 
    min_value=0.0, 
    value=6.0, 
    step=0.1
)

thang = st.number_input(
    "Nhập số tháng gửi tiết kiệm", 
    min_value=1, 
    value=12, 
    step=1
)

if st.button("Tính toán ngay"):
    # Công thức tính lãi suất đơn giản áp dụng cho kỳ hạn tháng
    ketqua = sotien * (1 + (laisuat / 100) * (thang / 12))
    st.balloons()  # Hiệu ứng bong bóng bay mừng thành công
    st.success(f"🎉 Số tiền bạn nhận được cả gốc lẫn lãi sau {thang} tháng gửi là: **{ketqua:.2f}** triệu đồng")
