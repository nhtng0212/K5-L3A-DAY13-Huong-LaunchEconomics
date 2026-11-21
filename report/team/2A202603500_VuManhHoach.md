# Báo cáo cá nhân — VuManhHoach-2A202603500

## 1. Thông tin thành viên

- Họ tên: Vũ Mạnh Hoạch
- MSSV: 2A202603500
- Email: 26ai.hoachvm@vinuni.edu.vn
- GitHub: vumanhhoach2003
- Vai trong nhóm: Chuyên viên Phân tích Chi phí (Cost & Economics Analyst - TV3) / Người kiểm số độc lập

## 2. Phần việc phụ trách

- Chịu trách nhiệm chính Nhiệm vụ A (Kinh tế của việc chạy lại, mô hình chi phí từ trace A1–A4).
- Chịu trách nhiệm chính Nhiệm vụ B (Bảng độ nhạy B1, đổi cặp B2, tối ưu chi phí cả hệ thống B3, kịch bản xem lại 100% B4).
- Soạn thảo nội dung mục E2 (Rủi ro kinh tế) trong `report/team/chi_so.md`.
- Cung cấp số liệu chi phí và độ nhạy cho Thành viên 5 điền mục 1, 2, 3 và 7 trong `report/team/ho_so_launch_v0.md`.

## 3. Đóng góp cụ thể

- Xây dựng mô hình tính toán chi phí và hoàn thiện 100% báo cáo `report/team/bang_chi_phi.md`.
- Tính toán chính xác 3 phép thử đáp án biết trước A1 (1,20 · 1,25 · 1,25).
- Phân rã chi phí thực tế từ trace (A2): chỉ ra chi phí mỗi việc thành công là 4.472 đ [simulated], gấp 16,3 lần hóa đơn token (274,7 đ), trong đó thời gian nhân viên chiếm 92,5% tổng chi phí.
- Phân tích chi phí theo loại yêu cầu (A3): chứng minh loại `quoc_te` (22.515 đ [simulated], 1,88× so với tự làm 12.000 đ) không đáng chạy và chạy lại không giúp cải thiện chất lượng; đề xuất thu hẹp phạm vi pilot về `noi_dia` (0,22×) và `hang_nang` (0,69×).
- Phân tích độ nhạy 9 kịch bản (B1) và chỉ ra 3 yếu tố nhạy nhất: Số ca làm lại (+51,8%) > Tỉ lệ xem lại (+40,7%) > Lương nhân viên (+23,1%).
- Phân tích sự đánh đổi kinh tế toàn hệ thống (B3): chứng minh mức giới hạn 2 lần chạy là tối ưu nhất cho công ty (6.901.220 đ [simulated]), tránh rơi vào bẫy tối ưu cục bộ của riêng trợ lý ở mức 1 lần chạy (đẩy thêm 85 việc sang nhân viên).
- Cảnh báo rủi ro xem lại 100% (B4) và thiết lập 3 kịch bản rủi ro kinh tế kèm hành động khắc phục cụ thể cho Gate 2a.

## 4. Bằng chứng

- File sản phẩm chính: `report/team/bang_chi_phi.md` (hoàn thiện đầy đủ tất cả các bảng và câu hỏi).
- Mục E2 (Rủi ro kinh tế) trong file: `report/team/chi_so.md`.
- Các đoạn code kiểm tra đối chiếu độc lập chạy bằng Python trên dữ liệu `logix_runs.csv` và `logix_requests.csv` khớp 100% đáp án chuẩn.

## 5. Công cụ AI đã dùng

- Công cụ: Antigravity Assistant (Gemini 3.8 Flash).
- Mục đích: Hỗ trợ kiểm tra công thức, rà soát nhãn `simulated`, kiểm soát độ dài câu trả lời $\le$ 3 dòng và tuân thủ quy chế chỉ duyệt kế hoạch pilot (không dùng từ chạy chính thức).
- Cách tự kiểm tra: Chạy script Python trên môi trường local đối chiếu với từng bảng số liệu trong tài liệu hướng dẫn `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, đảm bảo độ lệch không quá 2%.

## 6. Tự đánh giá

- Hoàn thành đầy đủ, chính xác và đúng hạn mọi đầu việc độc lập được giao.
- Tuân thủ nghiêm ngặt 5 quy tắc sống còn của lab.
- Đánh giá mức độ đóng góp: Hoàn thành xuất sắc nhiệm vụ được phân công.
