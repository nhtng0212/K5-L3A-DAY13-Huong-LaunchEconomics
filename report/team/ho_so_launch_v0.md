# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò cụ thể, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức.

Nhóm: Nhóm 4 · Lớp: K5-L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated], gấp 16,3 lần hóa đơn token (274,7 đ/yêu cầu; hoặc 4.599 đ [simulated] nếu gồm cố định 40tr/tháng ở 45k đơn). Giờ nhân viên chiếm 92,5% (làm lại 51,8%, xem lại 40,7%) [simulated]; token chiếm 5,6%, tool chiếm 1,9%. | Giả lập | Chuyên viên Phân tích Chi phí (TV3) |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8% khi tăng gấp đôi) · 2. Tỉ lệ xem lại (+40,7% khi tăng gấp đôi) · 3. Lương nhân viên (+23,1% khi tăng 25%). Token chỉ ảnh hưởng 5,6%. | Giả lập | Chuyên viên Phân tích Chi phí (TV3) |
| 3 · So với nhân viên tự làm | Toàn bộ: 4.472 đ [simulated] (0,37× của 12.000 đ); tính cả phần chuyển nhân viên là 5.865 đ/yêu cầu (0,49×). Phạm vi đề xuất: `noi_dia` đạt 2.696 đ (0,22×) và `hang_nang` đạt 8.221 đ (0,69×); loại bỏ `quoc_te` vì đắt hơn 1,88× (22.515 đ). | Giả lập | Chuyên viên Phân tích Chi phí (TV3) |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: Chỉ số chính (đóng 24h & không mở lại 7 ngày) đạt 82,83% (994/1.200); Chỉ số dùng (tỉ lệ bỏ qua gợi ý) là 27,12% (48/177); Chỉ số an toàn (mở lại 7 ngày) là 4,25% (51/1.200, trong phạm vi đề xuất là 3,97%). | Xong, có bằng chứng | Quản trị hồ sơ & chỉ số (TV5) |
| 5 · Bảng lỗi và cách khắc phục | Trùng 18/20 nhãn (90,0%) giữa hai người gắn nhãn độc lập; đủ 5 biện pháp khắc phục đại diện 5 loại lỗi kèm event có `trace_id`, ngưỡng đo lường tự động và vai trò phụ trách; đã thống nhất quy tắc phân loại cho 2 ca lệch. | Xong, có bằng chứng | Chuyên viên đánh giá lỗi (TV4) & Quản trị hồ sơ (TV5) |
| 6 · Pilot plan | Thiết kế thử nghiệm ngẫu nhiên phân tầng theo depot (stratified randomization), chia 20 nhân viên đối chứng và 20 nhân viên can thiệp (đạt chuẩn 20 cụm/nhóm), rollout 3 bước 10% → 25% → 50%, MDE 6 điểm (859 đơn/nhóm), 3 luật dừng chuẩn NẾU – TRONG – THÌ – KHÔNG THÌ. | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | 1. Làm lại x2 (+51,8%, lên 6.787 đ [simulated]) · 2. Xem lại 100% (11.743 đ – 12.414 đ [simulated], 0,98×–1,03× baseline) · 3. Khối lượng đơn thấp (+1.185 đ đến +2.370 đ/việc cố định). | Giả lập | PM trợ lý hoàn phí & Trưởng nhóm CSKH |

**Đề xuất:** **Go có điều kiện** (chấp thuận triển khai giai đoạn pilot cho phạm vi yêu cầu `noi_dia` và `hang_nang`).

Để chính thức bấm nút khởi động pilot vào ngày 2026-12-01, nhóm cam kết hoàn thành 4 điều kiện tiên quyết sau:

1. **Sửa khóa chống trùng và đối soát sổ cái (xử lý triệt để ca lỗi 7 và 20):** Áp dụng ràng buộc duy nhất (unique constraint) cho `idempotency_key` tại dịch vụ sổ cái hoàn tiền, tự động chặn hoàn trùng và cảnh báo khi lỗi 503.  
   *Người phụ trách:* Kỹ sư trưởng agent. *Hạn hoàn thành:* 2026-11-28.
2. **Ký duyệt chấp thuận mức chênh MDE 6 điểm:** Giám đốc vận hành phê duyệt văn bản chấp nhận mức MDE mục tiêu là 6 điểm (859 đơn/nhóm, tương ứng statistical power đạt 0,64 ở mức chênh 5 điểm) để đảm bảo tính khả thi với quy mô 20 nhân viên/nhóm hiện có của công ty.  
   *Người phụ trách:* Giám đốc vận hành LogiX-VN. *Hạn hoàn thành:* 2026-11-29.
3. **Kích hoạt hạ tầng giám sát 10 event có `trace_id` và thay thế số liệu giả lập:** Bật đầy đủ logging cho 10 event chuẩn vào hệ thống telemetry; thay thế số phút xem lại/làm lại giả lập (`_simulated`) bằng số liệu đo đạc thực tế từ event `staff_review_decision` và `staff_rework_completed` ngay sau tuần rollout đầu tiên (bước 10%).  
   *Người phụ trách:* Kỹ sư trưởng agent & Kỹ sư dữ liệu. *Hạn hoàn thành:* 2026-12-08.
4. **Ban hành quy trình kiểm soát xem lại theo bậc:** Thiết lập cơ chế tự động giảm tỷ lệ yêu cầu phải xem lại (từ 100% xuống kiểm tra xác suất 20%) khi tỷ lệ nhân viên sửa/bỏ qua gợi ý ổn định dưới 15% liên tiếp 3 ngày, nhằm ngăn ngừa kịch bản chi phí vượt trần 12.000 đ.  
   *Người phụ trách:* Trưởng nhóm CSKH. *Hạn hoàn thành:* 2026-11-30.
