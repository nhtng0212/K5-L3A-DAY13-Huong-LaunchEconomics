# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm:
- Lớp:
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

...

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- **Nhiệm vụ A · Mô hình chi phí từ trace ([bang_chi_phi.md](bang_chi_phi.md)):** Xây dựng hàm `mo_hinh` tính chi phí thật cho mỗi yêu cầu thành công từ trace, bao gồm chi phí token, tool, thời gian nhân viên xem lại và làm lại. Phân rã theo 4 phân khúc (`noi_dia`, `hang_nang`, `quoc_te`, `doi_tac`) và đánh giá chi phí cố định 40 triệu đ/tháng.
- **Nhiệm vụ B · Bảng độ nhạy & Tối ưu kinh tế hệ thống ([bang_chi_phi.md](bang_chi_phi.md)):** Thực hiện 9 kịch bản độ nhạy đơn lẻ và kịch bản đổi một cặp để xác định các yếu tố trọng yếu ảnh hưởng đến ngân sách. Phân tích bài toán giới hạn số lần chạy tối ưu toàn hệ thống (B3) và đánh giá ngưỡng hòa vốn khi phải xem lại 100% (B4).
- **Nhiệm vụ C · Bảng lỗi và khắc phục ([bang_loi.md](bang_loi.md)):** Đang cập nhật bởi TV4 và TV5.
- **Nhiệm vụ D · Kế hoạch pilot ([pilot_plan.yaml](pilot_plan.yaml)):** Đang cập nhật bởi TV1.
- **Nhiệm vụ E · Chỉ số và Hồ sơ launch v0 ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)):** TV3 đã hoàn thiện mục E2 (Rủi ro kinh tế); các chỉ số E1 và hồ sơ tổng hợp đang cập nhật bởi TV5.

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- **Chi phí mỗi việc thành công (CPS):** 4.472 đ [simulated] (gấp 16,3 lần hóa đơn token 274,7 đ). Thời gian nhân viên chiếm 92,5% tổng chi phí (làm lại 51,8%, xem lại 40,7%).
- **Phân khúc loại bỏ:** Loại `quoc_te` (22.515 đ [simulated], 1,88× baseline 12.000 đ) và `doi_tac` (10.215 đ [simulated], 0,85×) ra khỏi phạm vi pilot; chỉ giữ `noi_dia` (2.696 đ [simulated], 0,22×) và `hang_nang` (8.221 đ [simulated], 0,69×).
- **Chi phí cố định 40tr/tháng:** Ở quy mô 45k đơn đạt 4.599 đ (0,38×) [simulated]; ở quy mô một nửa đạt 5.784 đ (0,48×) [simulated].
- **Ba yếu tố nhạy nhất:** 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%).
- **Tối ưu hệ thống:** Giới hạn 2 lần chạy là rẻ nhất toàn công ty (6.901.220 đ [simulated]), tiết kiệm hơn giới hạn 1 lần (7.449.781 đ) và 3 lần (7.037.585 đ).
- **Cảnh báo xem lại 100%:** Chi phí đội lên 11.743 đ – 12.414 đ [simulated] (0,98× – 1,03× baseline), triệt tiêu lợi ích kinh tế nếu không hạ tỷ lệ xem lại theo bậc.

## 5. Khó khăn và cách xử lý

...

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

- **Vũ Mạnh Hoạch (TV3 - 2A202603500):** Chịu trách nhiệm 100% Nhiệm vụ A (mô hình chi phí A1–A4) và Nhiệm vụ B (bảng độ nhạy B1–B4), hoàn thiện file `report/team/bang_chi_phi.md`, đóng góp mục E2 (Rủi ro kinh tế) trong `report/team/chi_so.md`, cung cấp các số liệu kinh tế mục 1, 2, 3, 7 cho `report/team/ho_so_launch_v0.md`.
- Các thành viên khác: xem chi tiết tại `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

...

## 8. Tài liệu tham khảo

...
