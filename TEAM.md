# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3A hoặc L3B
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên      | MSSV        | Email | GitHub | Vai trò                                    |
| --: | ----------- | ----------- | ----- | ------ | ------------------------------------------ |
|   1 |             |             |       |        |                                            |
|   2 | Nguyễn Ngọc Hiếu | 2A202603502 |       |        | Kỹ sư Dữ liệu & Lập trình (Người viết code: src/lab13.py) |
|   3 |             |             |       |        |                                            |
|   4 | Hồ Văn Dũng | 2A202603458 |       |        | Chuyên viên đánh giá lỗi, người gắn nhãn 1 |
|   5 |             |             |       |        |                                            |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## NguyenNgocHieu-2A202603502

### Phần việc phụ trách

- **Vai trò:** Kỹ sư Dữ liệu & Lập trình Python (Người viết code chính).
- **File phụ trách:** `src/lab13.py`.
- **Nhiệm vụ:**
  - Nhiệm vụ A1: Lập trình 3 hàm kinh tế chạy lại (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), đảm bảo vượt qua 3 phép thử đáp án biết trước (1,20 · 1,25 · 1,25).
  - Nhiệm vụ A2 & A3: Viết hàm `mo_hinh(runs, reqs, ...)` tính chi phí thật từ trace; phân tích 4 phân khúc `noi_dia`, `hang_nang`, `quoc_te`, `doi_tac` và bảng pivot phân tích tỷ lệ thành công theo lần thử.
  - Nhiệm vụ A4: Tính chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` ở quy mô đầy đủ và quy mô pilot.
  - Nhiệm vụ B: Lập trình chạy 9 kịch bản độ nhạy B1, kịch bản đổi một cặp B2, tính toán chi phí cả hệ thống B3 và kịch bản xem lại 100% B4.
  - Hỗ trợ Nhiệm vụ D1 (tính cỡ mẫu hiệu dụng, ICC, DE) cho TV1 và Nhiệm vụ E1 (tính 3 chỉ số chính, dùng, an toàn) cho TV5.

### Đóng góp cụ thể

- Hoàn thiện 100% mã nguồn sạch, tối ưu trong `src/lab13.py`, chạy không lỗi trên Python 3.15 với pandas, numpy, scipy, statsmodels.
- Cung cấp toàn bộ bảng số liệu đầu ra chuẩn xác (sai số 0% so với đáp án gốc) để TV3 điền `report/team/bang_chi_phi.md`, TV1 điền `report/team/pilot_plan.yaml`, TV5 điền `report/team/chi_so.md` và `report/team/ho_so_launch_v0.md`.

### Bằng chứng

- File mã nguồn: `src/lab13.py`.
- Kết quả chạy terminal: Ba phép thử ĐẠT, CPS baseline = 4.472 đ [simulated], 9 kịch bản B1, chi phí hệ thống B3 = 6.901.220 đ [simulated], kết quả D1 (1.251 YC, m >= 299 đơn/người), chỉ số E1 (82,83% chính, 27,12% bỏ qua, 4,25% an toàn).

## Hồ Văn Dũng (2A202603458)

### Phần việc phụ trách

- TV4, phụ trách phân loại và đánh giá lỗi trong nhiệm vụ C.

### Đóng góp cụ thể

- Tổng hợp 20 nhãn có đối chiếu hướng dẫn Lab, ghi căn cứ từng ca và đề xuất 5 biện pháp khắc phục có cách phát hiện đo được.

### Bằng chứng

- [Bảng lỗi và cách khắc phục](report/team/bang_loi.md)
- [Báo cáo cá nhân](report/team/2A202603458_HoVanDung.md)
