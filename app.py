import streamlit as st

st.title("Đánh Giá Khả Năng Cho Vay")

# Nhập dữ liệu
STV = st.number_input(
    "NHẬP SỐ TIỀN MUỐN VAY (TRIỆU ĐỒNG):",
    min_value=0.0,
    value=100.0
)

TGV = st.number_input(
    "NHẬP THỜI GIAN VAY (SỐ NĂM):",
    min_value=0.1,
    value=5.0
)

LSV = st.number_input(
    "NHẬP LÃI SUẤT CHO VAY (SỐ THẬP PHÂN):",
    min_value=0.0,
    value=0.1,
    format="%.4f"
)

TN = st.number_input(
    "NHẬP THU NHẬP HÀNG THÁNG (TRIỆU ĐỒNG/THÁNG):",
    min_value=0.0,
    value=20.0
)

SNTGD = st.number_input(
    "NHẬP SỐ NGƯỜI TRONG GIA ĐÌNH:",
    min_value=0,
    value=2
)

PTMC = st.number_input(
    "NHẬP SỐ TIỀN PHẢI TRẢ CHO KHOẢN VAY CŨ (TRIỆU ĐỒNG):",
    min_value=0.0,
    value=0.0
)

GTTSDB = st.number_input(
    "NHẬP GIÁ TRỊ TSĐB (TRIỆU ĐỒNG):",
    min_value=0.1,
    value=200.0
)

STKKH = st.number_input(
    "NHẬP TUỔI KHÁCH HÀNG:",
    min_value=0,
    value=30
)

# Hằng số
CPSH = 5

# Nút tính toán
if st.button("Đánh giá khoản vay"):
    try:
        PTMM = (STV / (TGV * 12)) + (STV * (LSV / 12))
        DTI = (PTMC + PTMM) / (TN - SNTGD * CPSH)
        LTV = STV / GTTSDB

        st.subheader("Kết quả")

        st.write(f"**Chỉ số DTI:** {DTI*100:.2f}%")
        st.write(f"**Chỉ số LTV:** {LTV*100:.2f}%")

        if DTI <= 0.7 and LTV <= 0.7 and 18 <= STKKH <= 70:
            st.success("ĐƯỢC CHO VAY")
        else:
            st.error("KHÔNG ĐƯỢC CHO VAY")

    except ZeroDivisionError:
        st.error("Dữ liệu không hợp lệ, vui lòng kiểm tra lại.")
