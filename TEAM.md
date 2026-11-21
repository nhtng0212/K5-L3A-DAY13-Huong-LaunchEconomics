# Team

## Thông tin nhóm

- Tên nhóm: Huong (Nhóm 4 - LogiX-VN)
- Lớp: K5-L3A
- Repo nhóm: `K5-L3A-DAY13-Huong-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/nhtng0212/K5-L3A-DAY13-Huong-LaunchEconomics, nhánh `main`

## Thành viên

| STT | Họ tên           | MSSV        | Email                            | GitHub                                 | Vai trò                                                        |
| --: | ---------------- | ----------- | -------------------------------- | -------------------------------------- | -------------------------------------------------------------- |
|   1 | Nguyễn Hoàng Tùng| [Điền MSSV] | nguyentungpcbv@gmail.com         | nhtng0212                              | Nhóm trưởng & Kiến trúc sư Pilot (Lead / Pilot Architect, TV1) |
|   2 | Nguyễn Ngọc Hiếu | 2A202603502 |                                  |                                        | Kỹ sư Dữ liệu & Code (Data / Code Specialist, TV2)             |
|   3 | Vũ Mạnh Hoạch    | 2A202603500 | 26ai.hoachvm@vinuni.edu.vn       | vumanhhoach2003                        | Chuyên viên Phân tích Chi phí (Cost & Economics Analyst, TV3)  |
|   4 | Hồ Văn Dũng      | 2A202603458 | hdung7047@gmail.com              | [DungZai](https://github.com/DungZai)  | Chuyên viên đánh giá lỗi, người gắn nhãn 1 (TV4)               |
|   5 | Nguyễn Văn Tùng  | 2A202603471 | tungnv.2a202603471@vinuni.edu.vn |                                        | Quản trị Hồ sơ & Chỉ số, người gắn nhãn 2 (TV5)                |

Phân vai tác chiến nhóm 5 người:

- **Nhóm trưởng (TV1):** Quản trị tiến độ, kiến trúc kế hoạch pilot (`pilot_plan.yaml`), tính toán cỡ mẫu D1, D2, luật dừng và chủ trì duyệt chéo Gate 2a.
- **Kỹ sư dữ liệu & code (TV2):** Viết và chạy `src/lab13.py` (3 phép thử, trace, độ nhạy, cỡ mẫu D1, chỉ số E1).
- **Chuyên viên chi phí (TV3):** Kiểm số đối chứng, hoàn thiện `bang_chi_phi.md` và phân tích rủi ro kinh tế E2.
- **Chuyên viên đánh giá lỗi (TV4):** Gắn nhãn độc lập 20 ca ở CP3, căn cứ phân loại và hoàn thiện bảng khắc phục trong `bang_loi.md`.
- **Quản trị hồ sơ & chỉ số (TV5):** Gắn nhãn độc lập 20 ca ở CP3, đặc tả chỉ số `chi_so.md`, giữ và chốt `ho_so_launch_v0.md`, phiếu chấm hội đồng `phieu_cham.md`.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/2A202603471_NguyenVanTung.md`.

---

## Nguyễn Hoàng Tùng ([Điền MSSV])

### Phần việc phụ trách

- Nhóm trưởng (TV1), Kiến trúc sư Pilot: Phụ trách toàn bộ Nhiệm vụ D (`report/team/pilot_plan.yaml`), quản trị tiến độ nhóm, điều phối ma trận phân công 5 người và chủ trì phản biện tại hội đồng duyệt chéo Gate 2a.

### Đóng góp cụ thể

- Soạn thảo và ban hành tài liệu phân công tác chiến chi tiết [PHAN_CONG_NHOM.md](PHAN_CONG_NHOM.md) với prompt mẫu cho Agent của 5 thành viên, tối ưu hóa workflow song song không nghẽn việc.
- Trực tiếp tính toán lý thuyết và phân tích cỡ mẫu cụm D1 trong `pilot_plan.yaml`:
  * Xác định bất đẳng thức trần cỡ mẫu hiệu dụng khi chia theo nhân viên (20+20): $n_{\text{effective}} < c/\text{ICC} = 20/0,02 = 1.000 < 1.251$ (không thể phát hiện mức chênh 5 điểm với power 0,80).
  * Đề xuất phương án đánh đổi: nâng MDE lên 6 điểm ($0,70 \rightarrow 0,76$), yêu cầu $m \ge 299$ đơn/người ($n = 859$ đơn/nhóm, $\text{DE} = 6,96$), công khai điểm bất lợi power đạt 0,64 nếu tác động thực tế chỉ là 5 điểm.
  * Bác bỏ phương án chia theo Depot ($c=6$) do thiếu mẫu nghiêm trọng (tối đa 300) và vi phạm điều kiện tối thiểu 20 cụm.
- Trả lời trọn vẹn 5 câu hỏi D2 về bảo đảm tách tác động (concurrent control, stratified randomization theo 12 depot, spillover mitigation bằng tài khoản cá nhân, predeclared ngày 2027-01-05, đủ 20 cụm).
- Thiết kế 3 luật dừng tự động (Stop Rules) chuẩn cú pháp NẾU – TRONG – THÌ – KHÔNG THÌ, căn cứ trên baseline mở lại thực tế 4,25% để chọn ngưỡng an toàn 6%.
- Thiết lập cơ chế ngắt khẩn cấp (Rollback) 30 phút qua feature flag fallback về luồng nhân viên thủ công.
- Chuẩn bị bộ câu hỏi và kịch bản phản biện số liệu bảo vệ tại hội đồng Gate 2a.

### Bằng chứng

- [Kế hoạch pilot (pilot_plan.yaml)](report/team/pilot_plan.yaml)
- [Bảng phân công nhóm tác chiến (PHAN_CONG_NHOM.md)](PHAN_CONG_NHOM.md)
- [Báo cáo cá nhân](report/team/MSSV_NguyenHoangTung.md)

---

## NguyenNgocHieu-2A202603502

### Phần việc phụ trách

- **Vai trò:** Kỹ sư Dữ liệu & Lập trình Python (Người viết code chính, TV2).
- **File phụ trách:** `src/lab13.py`.
- **Nhiệm vụ:**
  - Nhiệm vụ A1: Lập trình 3 hàm kinh tế chạy lại (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), đảm bảo vượt qua 3 phép thử đáp án biết trước (1,20 · 1,25 · 1,25).
  - Nhiệm vụ A2 & A3: Viết hàm `mo_hinh(runs, reqs, ...)` tính chi phí thật từ trace; phân tích 4 phân khúc `noi_dia`, `hang_nang`, `quoc_te`, `doi_tac` và bảng pivot phân tích tỷ lệ thành công theo lần thử.
  - Nhiệm vụ A4: Tính chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` ở quy mô đầy đủ và quy mô pilot.
  - Nhiệm vụ B: Lập trình chạy 9 kịch bản độ nhạy B1, kịch bản đổi một cặp B2, tính toán chi phí cả hệ thống B3 và kịch bản xem lại 100% B4.
  - Hỗ trợ Nhiệm vụ D1 (tính cỡ mẫu hiệu dụng, ICC, DE) cho TV1 và Nhiệm vụ E1 (tính 3 chỉ số chính, dùng, an toàn) cho TV5.

### Đóng góp cụ thể

- Hoàn thiện 100% mã nguồn sạch, tối ưu trong `src/lab13.py`, chạy không lỗi trên Python 3.10+ với pandas, numpy, scipy, statsmodels.
- Cung cấp toàn bộ bảng số liệu đầu ra chuẩn xác (sai số 0% so với đáp án gốc) để TV3 điền `report/team/bang_chi_phi.md`, TV1 điền `report/team/pilot_plan.yaml`, TV5 điền `report/team/chi_so.md` và `report/team/ho_so_launch_v0.md`.

### Bằng chứng

- File mã nguồn: `src/lab13.py`.
- Kết quả chạy terminal: Ba phép thử ĐẠT, CPS baseline = 4.472 đ [simulated], 9 kịch bản B1, chi phí hệ thống B3 = 6.901.220 đ [simulated], kết quả D1 (1.251 YC, m >= 299 đơn/người), chỉ số E1 (82,83% chính, 27,12% bỏ qua, 4,25% an toàn).
- [Báo cáo cá nhân](report/team/2A202603502_NguyenNgocHieu.md)

---

## VuManhHoach-2A202603500

### Phần việc phụ trách

- **Vai trò:** Chuyên viên Phân tích Chi phí (Cost & Economics Analyst - TV3) / Người kiểm số độc lập.
- **File phụ trách:** `report/team/bang_chi_phi.md`, mục E2 trong `report/team/chi_so.md`.
- **Nhiệm vụ:**
  - Nhiệm vụ A: Phân tích mô hình chi phí từ trace A1–A4, tính chi phí cố định 40tr/tháng cho phạm vi `noi_dia` + `hang_nang`.
  - Nhiệm vụ B: Phân tích bảng 9 kịch bản độ nhạy B1, đổi một cặp B2, tối ưu chi phí cả hệ thống B3 và kịch bản xem lại 100% B4.
  - Nhiệm vụ E2: Soạn thảo 3 kịch bản rủi ro kinh tế trong `report/team/chi_so.md`.
  - Cung cấp số liệu mục 1, 2, 3 và 7 cho `report/team/ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Hoàn thiện 100% nội dung phân tích trong `report/team/bang_chi_phi.md` với đầy đủ số liệu và nhãn `[simulated]`.
- Phân tích sự đánh đổi chi phí cả hệ thống (B3): chỉ ra mức giới hạn 2 lần chạy rẻ nhất toàn công ty (6.901.220 đ [simulated]).
- Phân tích rủi ro xem lại 100% (B4) và xây dựng 3 kịch bản rủi ro kinh tế (E2) cho Gate 2a.

### Bằng chứng

- [Bảng chi phí và phân tích độ nhạy](report/team/bang_chi_phi.md)
- [Báo cáo cá nhân](report/team/2A202603500_VuManhHoach.md)

---

## Hồ Văn Dũng (2A202603458)

### Phần việc phụ trách

- TV4, phụ trách phân loại và đánh giá lỗi trong nhiệm vụ C (Người gắn nhãn 1 - Labeler 1).

### Đóng góp cụ thể

- Tổng hợp 20 nhãn có đối chiếu hướng dẫn Lab, ghi căn cứ từng ca và đề xuất 5 biện pháp khắc phục có cách phát hiện đo được.

### Bằng chứng

- [Bảng lỗi và cách khắc phục](report/team/bang_loi.md)
- [Báo cáo cá nhân](report/team/2A202603458_HoVanDung.md)

---

## Nguyễn Văn Tùng (2A202603471)

### Phần việc phụ trách

- TV5 — Quản trị Hồ sơ & Chỉ số, Người gắn nhãn 2 (Labeler 2).
- Chịu trách nhiệm hoàn thiện **Checkpoint 5 (CP5)**: Nhiệm vụ E1 (Đặc tả chỉ số, danh sách 10 event telemetry có `trace_id`), Nhiệm vụ E2 (Rủi ro kinh tế định lượng), hoàn thiện Hồ sơ Launch v0 (`ho_so_launch_v0.md`), tham gia Hội đồng duyệt chéo Gate 2a (`phieu_cham.md`), và phối hợp hoàn thành Nhiệm vụ C (Gắn nhãn độc lập 20 ca lỗi).

### Đóng góp cụ thể

- Thực hiện gắn nhãn độc lập 20 ca lỗi (CP3), đạt tỷ lệ đồng thuận ban đầu 90% (18/20 ca) với TV4, thống nhất căn cứ phân loại cho 2 ca lệch theo nguyên nhân gốc.
- Đặc tả và tính toán chính xác 3 chỉ số trong đợt chạy thử (Chính: 82,83%; Dùng: 27,12%; An toàn: 4,25%), đề xuất 2 chỉ số mới về sử dụng và an toàn kiểm toán.
- Thiết kế 10 event telemetry có `trace_id` liên kết trực tiếp với các chỉ số đo lường.
- Lập bảng lượng hóa 3 rủi ro kinh tế lớn từ bảng độ nhạy kèm dấu hiệu theo dõi và vai trò phụ trách.
- Tổng hợp Hồ sơ Launch v0 một trang chuẩn 7 mục, gắn nhãn trạng thái `Giả lập` chuẩn xác, đề xuất quyết định "Go có điều kiện" kèm 4 điều kiện ràng buộc cụ thể.
- Hoàn thiện phiếu chấm hội đồng Gate 2a chấm phản biện nhóm bạn với thang điểm 30/30.

### Bằng chứng

- [Hồ sơ Launch v0](report/team/ho_so_launch_v0.md)
- [Đặc tả chỉ số & Rủi ro kinh tế](report/team/chi_so.md)
- [Bảng lỗi và cách khắc phục](report/team/bang_loi.md)
- [Phiếu chấm hội đồng Gate 2a](report/team/phieu_cham.md)
- [Báo cáo cá nhân](report/team/2A202603471_NguyenVanTung.md)
