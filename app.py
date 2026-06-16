import streamlit as st
import os

# 1. Thiết lập giao diện tab trình duyệt
st.set_page_config(
    page_title="Ứng dụng tính tiền gửi tiết kiệm - Diễm Quỳnh", 
    page_icon="💰",
    layout="centered"
)

st.title("💰 Ứng dụng tính tiền gửi tiết kiệm_Diễm Quỳnh")

# 2. CODE THÁM TỬ: Tự động quét tìm bất kỳ file ảnh nào có trong thư mục
dinh_dang_anh = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".heic")
files_trong_thu_muc = os.listdir(".")

file_anh_tim_thay = None
for f in files_trong_thu_muc:
    # Bỏ qua các file hệ thống ẩn bắt đầu bằng dấu chấm
    if f.lower().endswith(dinh_dang_anh) and not f.startswith("."):
        file_anh_tim_thay = f
        break

# 3. Hiển thị ảnh nếu tìm thấy, nếu không thấy thì báo danh sách file thực tế để sửa lỗi
if file_anh_tim_thay:
    st.image(file_anh_tim_thay, width=350, caption=f"Ảnh của Diễm Quỳnh ({file_anh_tim_thay}) ✨")
else:
    st.warning("⚠️ Quỳnh ơi, hệ thống chưa tìm thấy bất kỳ file ảnh nào trên GitHub cả!")
    st.write("---")
    st.subheader("📂 Các file hiện tại đang có trên GitHub của bạn là:")
    st.write("Bạn nhìn danh sách dưới này xem đã có file ảnh nào chưa nhé:")
    for f in files_trong_thu_muc:
        if not f.startswith("."):
            st.code(f)
    st.info("👉 Nếu chưa có file ảnh nào ở trên, hãy làm tiếp **Bước 3** ở dưới để tải ảnh lên nha!")

st.write("---")

# 4. Công cụ tính toán lãi kép
st.subheader("🧮 Công cụ tính toán lãi kép")

sotien = st.number_input(
    "Nhập số tiền khách hàng gửi tiết kiệm (triệu đồng)", 
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
    "Nhập số tháng khách hàng gửi tiết kiệm", 
    min_value=1, 
    value=12, 
    step=1
)

if st.button("Tính toán"):
    ketqua = sotien * (1 + (laisuat / 100) * (thang / 12))
    st.balloons()  # Hiệu ứng bong bóng chúc mừng bay lên cực đẹp
    st.success(f"🎉 Số tiền bạn nhận được cả gốc lẫn lãi sau {thang} tháng gửi là: **{ketqua:.2f}** triệu đồng")
