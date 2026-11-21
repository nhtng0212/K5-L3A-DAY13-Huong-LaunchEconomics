# Báo cáo nhóm · Lab 13 (AI20K K5)
## Định giá Agent & Lập kế hoạch Pilot (LogiX-VN, Gate 2a)

Báo cáo ngắn gọn tổng kết hồ sơ duyệt Gate 2a cho Trợ lý hoàn phí LogiX-VN. Số liệu chi tiết nằm trong các file hồ sơ tương ứng tại thư mục `report/team/`.

---

## 1. Thông tin nhóm

- **Tên nhóm:** Huong (Nhóm 4 — LogiX-VN)
- **Lớp:** K5-L3A
- **Repo nhóm:** [K5-L3A-DAY13-Huong-LaunchEconomics](https://github.com/nhtng0212/K5-L3A-DAY13-Huong-LaunchEconomics) (Nhánh nộp: `main`)
- **Thành viên:** 5 người (Xem chi tiết tại [TEAM.md](../../TEAM.md))

---

## 2. Mục tiêu và cách tiếp cận

- **Mục tiêu:** Xây dựng bộ Hồ sơ Launch v0 hoàn chỉnh bảo vệ trước Hội đồng Gate 2a, trả lời 4 câu hỏi kinh doanh sống còn: Có đáng chạy không? Khi hỏng thì sao? Pilot thiết kế thế nào để ra quyết định? và Nhân viên có dùng không?
- **Cách tiếp cận:**
  1. *Kinh tế học Agent (Cost-of-Pass):* Không chỉ đo hóa đơn token mà tính toán chi phí can thiệp toàn diện của con người (xem lại, làm lại, chuyển giao).
  2. *Thiết kế thử nghiệm ngẫu nhiên phân cụm (Cluster RCT):* Khắc phục rủi ro lan tỏa tác động (spillover) bằng cách phân cụm theo 20 nhân viên can thiệp và 20 nhân viên đối chứng, phân tầng qua 12 depot.
  3. *Quản trị rủi ro đa tầng:* Phân loại lỗi theo nguyên nhân gốc của Google PAIR, thiết lập hệ thống giám sát 10 event telemetry có `trace_id` và 3 luật dừng tự động (Stop Rules) cùng cơ chế Rollback trong 30 phút.

---

## 3. Giải pháp thực hiện

- **Nhiệm vụ A · Mô hình chi phí từ trace ([bang_chi_phi.md](bang_chi_phi.md)):** Lập trình hàm `mo_hinh` trong `src/lab13.py` tính chi phí thật cho mỗi yêu cầu thành công từ trace 1.624 lần chạy. Phân tích 4 phân khúc (`noi_dia`, `hang_nang`, `quoc_te`, `doi_tac`) và phân bổ chi phí cố định 40 triệu đ/tháng.
- **Nhiệm vụ B · Bảng độ nhạy & Tối ưu kinh tế hệ thống ([bang_chi_phi.md](bang_chi_phi.md)):** Thực hiện 9 kịch bản độ nhạy đơn lẻ và kịch bản đổi một cặp; xác định 3 yếu tố nhạy cảm nhất. Giải quyết bài toán đánh đổi chi phí cả hệ thống (B3) và đánh giá ngưỡng hòa vốn khi phải xem lại 100% (B4).
- **Nhiệm vụ C · Bảng lỗi và cách khắc phục ([bang_loi.md](bang_loi.md)):** Hai thành viên (TV4 và TV5) gắn nhãn độc lập 20 ca lỗi theo 5 nhóm của Google PAIR, đạt độ đồng thuận 90,0% (18/20 ca); thống nhất quy tắc cho 2 ca lệch và xây dựng 5 biện pháp khắc phục đo lường được có người phụ trách cụ thể.
- **Nhiệm vụ D · Kế hoạch pilot ([pilot_plan.yaml](pilot_plan.yaml)):** Thiết kế kế hoạch pilot phân cụm ngẫu nhiên phân tầng; chứng minh giới hạn cỡ mẫu lý thuyết ($n_{\text{effective}} < 1.000$), đưa ra đánh đổi nâng MDE lên 6 điểm ($m \ge 299$ đơn/người), thiết lập 3 luật dừng chuẩn NẾU – TRONG – THÌ – KHÔNG THÌ và rollback 30 phút.
- **Nhiệm vụ E · Chỉ số, Rủi ro kinh tế & Hồ sơ launch v0 ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)):** Đặc tả và tính thử 3 chỉ số từ 1.200 yêu cầu, thiết lập 10 event có `trace_id`, định lượng 3 rủi ro kinh tế và tổng hợp trang Hồ sơ Launch v0 chuẩn 7 mục chốt đề xuất **Go có điều kiện**.

---

## 4. Kết quả chính

| Chỉ số / Hạng mục | Giá trị tính toán | Nhãn | So với Baseline / Nhận xét |
| :--- | :--- | :--- | :--- |
| **Chi phí mỗi việc thành công (CPS)** | **4.472 đ** | simulated | Gấp **16,3 lần** hóa đơn token (274,7 đ); thời gian nhân viên chiếm 92,5% (làm lại 51,8%, xem lại 40,7%). |
| **Phạm vi pilot đề xuất** | `noi_dia` (2.696 đ) + `hang_nang` (8.221 đ) | simulated | Đạt lần lượt **0,22×** và **0,69×** so với 12.000 đ. |
| **Phân khúc loại bỏ** | `quoc_te` (22.515 đ) và `doi_tac` (10.215 đ) | simulated | Loại vì `quoc_te` đắt gấp **1,88×** và chạy lại không hiệu quả; `doi_tac` đạt 0,85× có điều khoản riêng. |
| **Chi phí cố định 40tr/tháng** | 4.599 đ (ở 45k đơn) / 5.784 đ (ở 22,5k đơn) | simulated | Đạt 0,38× và 0,48× baseline; không làm đổi kết luận kinh tế. |
| **Top 3 yếu tố nhạy nhất** | 1. Ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương NV (+23,1%) | simulated | Hóa đơn token chỉ ảnh hưởng 5,6%. |
| **Tối ưu hệ thống (B3)** | Giới hạn **2 lần chạy** (6.901.220 đ) | simulated | Rẻ nhất toàn công ty; tiết kiệm hơn giới hạn 1 lần (7.449.781 đ) và 3 lần (7.037.585 đ). |
| **Cảnh báo xem lại 100% (B4)** | 11.743 đ (0,98×) đến 12.414 đ (1,03×) | simulated | Xem lại 100% đắt hơn người tự làm nếu làm lại 15,3 phút. Phải giảm xem lại theo bậc. |
| **Độ đồng thuận gắn nhãn (C)** | **18/20 ca = 90,0%** | đo từ trace | Vượt ngưỡng 80% của Rubric CP3; đủ 5 ca khắc phục đo lường được. |
| **Chỉ số chạy thử 2 tuần (E1)** | Chính: **82,83%** · Dùng: **27,12%** · An toàn: **4,25%** | đo từ trace | Đủ 10 event có `trace_id` liên kết thông suốt. |
| **Đề xuất cuối cùng** | **Go có điều kiện** | quyết định | Chấp thuận pilot `noi_dia` + `hang_nang` với 4 điều kiện ràng buộc. |

---

## 5. Khó khăn và cách xử lý

1. **Nút thắt cỡ mẫu khi chia theo cụm nhân viên (CP4):** 
   - *Khó khăn:* Với 40 nhân viên ($c=20$), trần cỡ mẫu hiệu dụng $n_{\text{effective}} < c/\text{ICC} = 1.000$, không thể đủ mẫu phát hiện mức chênh 5 điểm ($n=1.251, \text{power}=0,80$).
   - *Cách xử lý:* Nhóm không thỏa hiệp chia theo yêu cầu (vì sợ tràn tác động) cũng không chia theo depot (chỉ có 6 cụm). Nhóm chọn phương án kỹ thuật minh bạch: nâng MDE lên 6 điểm ($n=859, m \ge 299$), đồng thời công khai đánh đổi mức power giảm còn 0,64 nếu hiệu quả thật chỉ là 5 điểm.
2. **Nguy cơ lỗ kinh tế khi xem lại 100% (CP2):**
   - *Khó khăn:* Nếu áp dụng quy trình kiểm soát rủi ro bằng cách duyệt 100% yêu cầu trong tuần đầu, chi phí sẽ tăng lên 1,03× baseline.
   - *Cách xử lý:* Đưa vào điều kiện tiên quyết số 4 tại Hồ sơ launch: Trưởng nhóm CSKH phải ban hành cơ chế hạ bậc xem lại (từ 100% xuống kiểm tra ngẫu nhiên 20%) ngay khi tỉ lệ nhân viên sửa/bỏ ổn định dưới 15%.
3. **Độ lệch phân loại nguyên nhân gốc lỗi (CP3):**
   - *Khó khăn:* Ban đầu 2 người gắn nhãn lệch ở Ca 6 và Ca 8 do nhầm giữa biểu hiện bề mặt và nguyên nhân gốc.
   - *Cách xử lý:* Thảo luận dựa trên hướng dẫn Google PAIR: Ca 6 gốc do khách chọn sai form (Do người dùng), Ca 8 vi phạm chính sách hiển thị văn bản công khai (Hệ thống), nâng tỷ lệ đồng thuận lên 90,0%.

---

## 6. Tổng hợp đóng góp thành viên

- **Nguyễn Hoàng Tùng (TV1 - Nhóm trưởng):** Điều phối tiến độ, chịu trách nhiệm 100% Nhiệm vụ D (`pilot_plan.yaml`), tính toán cỡ mẫu cụm D1, trả lời D2, soạn thảo 3 luật dừng, đại diện bảo vệ và chủ trì phiên duyệt chéo Gate 2a.
- **Nguyễn Ngọc Hiếu (TV2 - Kỹ sư Dữ liệu & Code):** Chịu trách nhiệm 100% mã nguồn `src/lab13.py`, lập trình 3 hàm A1 đạt chuẩn, hàm `mo_hinh` A2, A3, 9 kịch bản độ nhạy B1-B4, xuất toàn bộ dữ liệu chính xác cho cả nhóm.
- **Vũ Mạnh Hoạch (TV3 - Chuyên viên Chi phí):** Chịu trách nhiệm 100% phân tích `report/team/bang_chi_phi.md`, kiểm tra đối chứng số liệu trace, phân tích chi phí hệ thống B3, kịch bản xem lại B4, đóng góp mục rủi ro kinh tế E2 trong `chi_so.md`.
- **Hồ Văn Dũng (TV4 - Chuyên viên Đánh giá Lỗi):** Chịu trách nhiệm chính Nhiệm vụ C, gắn nhãn độc lập 20 ca lỗi, xây dựng căn cứ phân loại và bảng 5 ca khắc phục trong `report/team/bang_loi.md`.
- **Nguyễn Văn Tùng (TV5 - Quản trị Hồ sơ & Chỉ số):** Chịu trách nhiệm chính CP5, gắn nhãn độc lập 20 ca lỗi (TV5), hoàn thiện 100% `report/team/chi_so.md` (3 chỉ số, 10 event có `trace_id`), tổng hợp `report/team/ho_so_launch_v0.md` 1 trang 7 mục và soạn phiếu chấm Gate 2a (`phieu_cham.md`).

---

## 7. Hạn chế và hướng cải thiện

- **Hạn chế:** Các chỉ số thời gian xem lại và làm lại hiện dựa trên số liệu giả lập (`_simulated`). Cỡ mẫu bị giới hạn bởi số lượng 40 nhân sự khiến power đạt 0,64 ở mức chênh 5 điểm.
- **Hướng cải thiện:** Ngay tuần đầu rollout pilot (bước 10%), kích hoạt event logging để thu thập dữ liệu thời gian thao tác thực tế của nhân viên CSKH thay thế hoàn toàn cho số `_simulated`.

---

## 8. Tài liệu tham khảo

1. Erol et al., *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359).
2. Google PAIR, *People + AI Guidebook*, Chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com).
3. Statsmodels Documentation, Module `statsmodels.stats.power.NormalIndPower`.
