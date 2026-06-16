import streamlit as st
import os

# Cấu hình giao diện và tiêu đề tab trình duyệt
st.set_page_config(
    page_title="Ứng dụng tính tiền gửi tiết kiệm - Diễm Quỳnh", 
    page_icon="💰",
    layout="centered"
)

st.title("💰 Ứng dụng tính tiền gửi tiết kiệm_Diễm Quỳnh")

# 🔎 TÍNH NĂNG SIÊU THÁM TỬ: Quét tự động tất cả các file trong thư mục
danh_sach_file = os.listdir('.')
anh_tim_thay = None
danh_sach_anh_trong_thu_muc = []

# Lọc ra tất cả các file có đuôi ảnh hợp lệ
duoi_anh_hop_le = ('.jpg', '.png', '.jpeg', '.webp', '.gif', '.heic', '.jfif')
for file_name in danh_sach_file:
    if file_name.lower().endswith(duoi_anh_hop_le):
        danh_sach_anh_trong_thu_muc.append(file_name)

# 1. Thử tìm xem có ảnh nào tên chứa chữ "quynh" hoặc "diem" không
for file_anh in danh_sach_anh_trong_thu_muc:
    ten_lower = file_anh.lower()
    if "quynh" in ten_lower or "diem" in ten_lower:
        anh_tim_thay = file_anh
        break

# 2. Nếu không có chữ "quynh" mà trong thư mục chỉ có duy nhất 1 file ảnh, dùng luôn ảnh đó
if not anh_tim_thay and len(danh_sach_anh_trong_thu_muc) == 1:
    anh_tim_thay = danh_sach_anh_trong_thu_muc[0]

# 3. Nếu vẫn không được, thử tìm các tên phổ biến mặc định
if not anh_tim_thay:
    ten_mac_dinh = ["diemquynh.jpg", "diemquynh.png", "DIEMQUYNH.JPG", "DIEMQUYNH.PNG", "THAONHI.JPG"]
    for ten in ten_mac_dinh:
        if os.path.exists(ten):
            anh_tim_thay = ten
            break

# Hiển thị ảnh nếu tìm thấy
if anh_tim_thay:
    st.image(anh_tim_thay, width=300, caption="Ảnh đại diện xinh xắn của Diễm Quỳnh nè! ✨")
    # Hiển thị thông báo nhỏ báo tên file ảnh đã nhận diện thành công
    st.toast(f"🎉 Đã tìm thấy và hiển thị ảnh: '{anh_tim_thay}'")
else:
    # Nếu không tìm thấy file ảnh nào, hiện giao diện hỗ trợ Quỳnh sửa lỗi trực quan
    st.warning("⚠️ **Không tìm thấy file ảnh nào trong kho GitHub của bạn!**")
    
    st.info(
        "💡 **Cách sửa lỗi cực nhanh:**\n\n"
        "1. Bạn hãy đổi tên bức ảnh trên máy tính/điện thoại thành **`diemquynh.jpg`** (viết thường toàn bộ, viết liền không dấu).\n"
        "2. Lên GitHub bấm nút **Add file** ➔ **Upload files** rồi tải bức ảnh đó lên.\n"
        "3. Kéo xuống dưới cùng trang GitHub bấm nút màu xanh **Commit changes** là xong!"
    )
    
    # In ra danh sách file thực tế đang có trên GitHub để Quỳnh đối chiếu
    st.write("---")
    st.write("🔍 **Danh sách các file thực tế đang có trên GitHub của bạn hiện tại:**")
    st.code("\n".join(danh_sach_file), language="text")

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
```
eof
