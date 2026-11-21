# Báo cáo cá nhân — Nguyễn Văn Tùng (2A202603471)

## 1. Thông tin thành viên

- **Họ tên:** Nguyễn Văn Tùng
- **MSSV:** 2A202603471
- **Email:** tungnv.2a202603471@vinuni.edu.vn
- **Vai trong nhóm:** TV5 — Quản trị Hồ sơ & Chỉ số (Gatekeeper / Metric & Labeler 2)

## 2. Phần việc phụ trách

- Chịu trách nhiệm chính **Checkpoint 5 (CP5)** — Nhiệm vụ E (Đặc tả chỉ số, danh sách event có `trace_id`, rủi ro kinh tế và hoàn thiện Hồ sơ Launch v0 bảo vệ tại Gate 2a) cùng hoạt động Duyệt chéo Gate 2a.
- Phối hợp thực hiện **Checkpoint 3 (CP3)** với vai trò Người gắn nhãn 2 (Labeler 2): thực hiện gắn nhãn độc lập 20 ca lỗi theo 5 loại của Google PAIR, đối chiếu tỷ lệ đồng thuận với TV4 và thống nhất quy tắc phân loại.

## 3. Đóng góp cụ thể

1. **Gắn nhãn độc lập 20 ca lỗi (CP3):**
   - Độc lập phân loại 20 ca lỗi không qua trao đổi trước, đạt tỷ lệ đồng thuận ban đầu 90% (18/20 ca) với TV4 (vượt ngưỡng yêu cầu $\ge 80\%$).
   - Thảo luận và thống nhất căn cứ phân loại cho 2 ca lệch (Ca 6 thống nhất là lỗi *Do người dùng*; Ca 8 thống nhất là lỗi *Hệ thống* dựa trên nguyên tắc nguyên nhân gốc).
2. **Đặc tả chỉ số E1 (`report/team/chi_so.md`):**
   - Tính toán chính xác 3 chỉ số từ tập dữ liệu 1.200 yêu cầu: Chỉ số chính đạt 82,83% (994/1.200); Chỉ số dùng đạt 27,12% (48/177); Chỉ số an toàn đạt 4,25% (51/1.200).
   - Đề xuất 1 chỉ số Dùng mới (Tỉ lệ yêu cầu trong nhóm can thiệp được mở bằng trợ lý) và 1 chỉ số An toàn mới (Tỉ lệ đơn hoàn sai tiền qua kiểm toán mẫu hằng tuần để phát hiện lỗi ngầm).
   - Chuẩn hóa ngôn ngữ báo cáo: dùng cụm từ *"chỉ số trong đợt chạy thử là..."*, tuyệt đối không dùng *"trợ lý đã nâng chỉ số"* khi chưa có đối chứng.
3. **Thiết kế danh sách 10 event telemetry có `trace_id`:**
   - Xây dựng bảng 10 event chi tiết bao quát toàn bộ vòng đời yêu cầu (từ tiếp nhận, agent thực thi, hiển thị gợi ý, nhân viên duyệt/làm lại, ghi sổ cái, đóng ticket, mở lại đến kiểm toán ngẫu nhiên).
   - Thiết lập bảng kiểm tra chéo liên kết từng chỉ số với event tương ứng để đảm bảo mọi chỉ số đều đo lường được trong thực tế.
4. **Lượng hóa rủi ro kinh tế E2:**
   - Trích xuất số liệu trực tiếp từ bảng độ nhạy (B1, B4, A4) để định lượng 3 rủi ro lớn: Số ca làm lại tăng gấp đôi (+51,8%), Bắt buộc xem lại 100% (chi phí tăng vọt lên 11.743 đ – 12.414 đ, vượt mốc 12.000 đ), Khối lượng sụt giảm một nửa (chi phí cố định phân bổ tăng lên 2.370 đ/việc).
   - Đề xuất hành động ứng phó cụ thể và gán vai trò chịu trách nhiệm trực tiếp.
5. **Tổng hợp Hồ sơ Launch v0 (`report/team/ho_so_launch_v0.md`):**
   - Hoàn thiện trang hồ sơ 7 mục cô đọng trong 1 trang A4. Gắn nhãn trạng thái `Giả lập` nghiêm ngặt cho các mục dựa trên dữ liệu simulated (mục 1, 2, 3, 7).
   - Đưa ra quyết định đề xuất **Go có điều kiện** đi kèm 4 cam kết giải pháp cụ thể (sửa lỗi hoàn trùng, phê duyệt MDE 6 điểm, kích hoạt logging 10 event, ban hành quy trình giảm xem lại theo bậc) có người phụ trách và ngày hoàn thành rõ ràng.
   - Tuân thủ tuyệt đối quy tắc không viết như thể trợ lý đã được duyệt chạy chính thức.
6. **Tham gia Hội đồng duyệt chéo Gate 2a (`report/team/phieu_cham.md`):**
   - Đóng vai hội đồng chấm chéo hồ sơ Nhóm 5, đánh giá khách quan dựa trên bằng chứng định lượng, đặt câu hỏi phản biện sâu về rủi ro chi phí khi xem lại 100% và ghi nhận câu trả lời.

## 4. Bằng chứng

- Hồ sơ Launch v0 hoàn chỉnh: [report/team/ho_so_launch_v0.md](ho_so_launch_v0.md)
- Đặc tả chỉ số, danh sách event và rủi ro kinh tế: [report/team/chi_so.md](chi_so.md)
- Bảng gắn nhãn độc lập và tỷ lệ đồng thuận: [report/team/bang_loi.md](bang_loi.md)
- Phiếu chấm phản biện hội đồng: [report/team/phieu_cham.md](phieu_cham.md)

## 5. Công cụ AI đã dùng

- **Antigravity AI (Gemini 3.8 Flash / Claude 4.6):** Hỗ trợ tra cứu công thức tính chỉ số, rà soát đối chiếu chéo các trường dữ liệu và định dạng báo cáo markdown chuẩn rubric Gate 2a.
- **Python script:** Viết mã Python độc lập trực tiếp trên terminal để xác thực 100% độ chính xác của các con số chỉ số từ hai file `logix_requests.csv` và `logix_runs.csv`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ, chính xác toàn bộ sản phẩm đầu ra của CP5 theo đúng yêu cầu đề bài và hướng dẫn chi tiết của lab.
- Tất cả các số liệu giả lập đều được gắn nhãn `[simulated]` rõ ràng, bảo đảm tính trung thực khoa học.
- Đạt chuẩn không vi phạm bất kỳ quy tắc nào của lab, sẵn sàng bảo vệ thành công hồ sơ trước hội đồng Gate 2a.
