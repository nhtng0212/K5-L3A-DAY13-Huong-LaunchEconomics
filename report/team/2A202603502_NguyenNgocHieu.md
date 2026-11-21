# Báo cáo cá nhân — 2A202603502_NguyenNgocHieu

## 1. Thông tin thành viên

- Họ tên: Nguyễn Ngọc Hiếu
- MSSV: 2A202603502
- Email: hieun2@vinuni.edu.vn (hoặc email theo hệ thống trường)
- Vai trong nhóm: Thành viên 2 (TV2) — Kỹ sư Dữ liệu & Lập trình (Người viết code chính). Phụ trách file `src/lab13.py`.

## 2. Phần việc phụ trách

- **Nhiệm vụ A1:** Lập trình 3 hàm kinh tế chạy lại (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`). Đảm bảo vượt qua 3 phép thử đáp án biết trước (1,20 · 1,25 · 1,25).
- **Nhiệm vụ A2 & A3:** Xây dựng hàm `mo_hinh(runs, reqs, ...)` tính toán chi phí thật từ trace trên 1.200 yêu cầu (1.624 lần chạy); phân rã chi phí và tỷ lệ thành công theo 4 phân khúc (`noi_dia`, `hang_nang`, `quoc_te`, `doi_tac`) và phân tích tỷ lệ thành công giảm dần theo attempt.
- **Nhiệm vụ A4:** Mô hình hóa chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` ở 2 kịch bản: quy mô đầy đủ (45.000 đơn) và quy mô pilot (giảm một nửa).
- **Nhiệm vụ B1–B4:** Lập trình tự động chạy 9 kịch bản độ nhạy B1, kịch bản kết hợp B2, bảng so sánh chi phí toàn hệ thống B3 giữa 1, 2, 3 lần chạy, và kịch bản xem lại 100% B4 (với 9 phút và 15,3 phút làm lại).
- **Hỗ trợ Nhiệm vụ D1 & E1:** Viết script tính cỡ mẫu thử nghiệm lâm sàng A/B (hàm `co_mau`, hệ số thiết kế DE, cỡ mẫu hiệu dụng có tính ICC) cho TV1 và tính toán 3 chỉ số thực tế (chính, dùng, an toàn) cho TV5.

## 3. Đóng góp cụ thể

- **Xử lý dữ liệu chuẩn xác:** Áp dụng đúng cờ `keep_default_na=False` khi nạp file `logix_requests.csv` để tránh ô trống bị ép kiểu thành `NaN`.
- **Cài đặt mô hình chi phí A2:** 
  - Tính đúng tử số gồm toàn bộ token và tool của mọi lần chạy (kể cả lần lỗi).
  - Nhân đúng đơn giá token đầu vào (26 đ / 1.000 token) và đầu ra (130 đ / 1.000 token).
  - Tách bạch rõ các thành phần chi phí giả lập (`phut_xem_lai_simulated`, `phut_lam_lai_simulated`) và gắn nhãn `[simulated]` đầy đủ.
  - Mẫu số đếm chuẩn 978 yêu cầu có `ket_qua == 'thanh_cong'`, ra CPS = 4.472 đ [simulated] (gấp 16,3 lần hóa đơn token).
- **Phân tích độ nhạy B:** 
  - Chỉ ra số ca làm lại (+51,8%) và tỷ lệ xem lại (+40,7%) là 2 biến số nhạy cảm nhất đối với bài toán kinh tế.
  - Chứng minh giới hạn 2 lần chạy là tối ưu nhất cho chi phí toàn công ty (6.901.220 đ [simulated]).
- **Xuất dữ liệu cho nhóm:** Cung cấp bảng in terminal sạch đẹp, trực quan, hỗ trợ TV3 điền bảng chi phí, TV1 điền kế hoạch pilot và TV5 hoàn thành hồ sơ launch v0.

## 4. Bằng chứng

- **File mã nguồn:** `src/lab13.py` (đã cập nhật đầy đủ và chạy thành công không có lỗi).
- **Các con số then chốt tính toán được (lệch 0% so với đáp án chuẩn):**
  - Ba phép thử A1: ĐẠT (`1.20`, `1.25`, `1.25`).
  - CPS trace: **4.472 đ** [simulated] (Token: 245.585 đ, Tool: 84.000 đ, Xem lại: 1.780.000 đ, Làm lại: 2.264.000 đ).
  - Hóa đơn / yêu cầu: **274,7 đ** $\to$ CPS gấp **16,3 lần** hóa đơn.
  - CPS theo phân khúc: `noi_dia` 2.696 đ (0,22x), `hang_nang` 8.221 đ (0,69x), `quoc_te` 22.515 đ (1,88x), `doi_tac` 10.215 đ (0,85x).
  - Kịch bản đổi một cặp B2: **6.543 đ** (+46,3% [simulated]).
  - Chi phí hệ thống B3: Max 2 lần chạy = **6.901.220 đ** [simulated].
  - Cỡ mẫu D1: 1.251 YC/nhóm; 20 nhân viên/nhóm đạt $m \ge 299$ đơn/người ở mức chênh 6 điểm.
  - Chỉ số E1: Chính = 82,83% (994/1.200), Bỏ qua = 27,12% (48/177), An toàn = 4,25% (51/1.200).

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity AI Assistant.
- **Mục đích sử dụng:**
  - Hỗ trợ rà soát công thức tính kỳ vọng số lần chạy hình học cụt (truncated geometric distribution) trong A1.
  - Viết code vector hóa dữ liệu với Pandas để xử lý nhanh trace của 1.624 lần chạy và lọc theo từng điều kiện `max_lan_chay`.
  - Hỗ trợ giải phương trình bậc nhất tìm số đơn tối thiểu $m \ge 299$ trong bài toán thiết kế mẫu phân cụm (Cluster Randomization với ICC = 0,02).
- **Kiểm chứng độc lập của bản thân:**
  - Tự tay tính nhẩm đối chiếu bằng tay 3 phép thử A1.
  - Kiểm tra thủ công tính chất cộng tuyến tính trong bảng độ nhạy B: mức tăng của kịch bản kết hợp (+46,3%) bằng đúng tổng 2 mức tăng riêng rẽ (+5,6% + 40,7%).
  - Kiểm tra điều kiện ràng buộc `keep_default_na=False` trên file CSV để đảm bảo không mất dữ liệu ở các chuỗi rỗng.

## 6. Tự đánh giá

- **Mức độ hoàn thành:** 100% nhiệm vụ được giao cho vị trí Kỹ sư Code & Dữ liệu.
- **Kỷ luật dữ liệu:** Tuân thủ tuyệt đối quy tắc ghi nhãn `[simulated]`, chỉ dùng thuật ngữ kế hoạch pilot theo đúng quy định Gate 2a, hoàn thành code đúng tiến độ để các thành viên khác có số liệu làm báo cáo.
- **Điểm tự đánh giá:** 10/10.
