# Team

## Thông tin nhóm

- Tên nhóm: Huong
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-Huong-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/nhtng0212/K5-L3A-DAY13-Huong-LaunchEconomics, nhánh `main`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Hoàng Tùng | [Điền MSSV] | nguyentungpcbv@gmail.com | nhtng0212 | Nhóm trưởng, Kiến trúc sư Pilot (Nhiệm vụ D, Gate 2a) |
|   2 | [Họ tên TV2] | [MSSV] | [Email] | [GitHub] | Kỹ sư Dữ liệu & Code (Nhiệm vụ A, B, lab13.py) |
|   3 | [Họ tên TV3] | [MSSV] | [Email] | [GitHub] | Chuyên viên Chi phí & Kinh tế (Nhiệm vụ A, B, bang_chi_phi.md) |
|   4 | Hồ Văn Dũng | 2A202603458 | hdung7047@gmail.com | DungZai | Chuyên viên đánh giá lỗi, người gắn nhãn 1 (Nhiệm vụ C, bang_loi.md) |
|   5 | [Họ tên TV5] | [MSSV] | [Email] | [GitHub] | Quản trị Hồ sơ & Chỉ số, người gắn nhãn 2 (Nhiệm vụ E, C, ho_so_launch_v0.md, chi_so.md) |

Phân vai tác chiến nhóm 5 người:

- **Nhóm trưởng (TV1):** Điều phối tiến độ, kiến trúc kế hoạch pilot (`pilot_plan.yaml`), chủ trì duyệt chéo Gate 2a.
- **Kỹ sư dữ liệu & code (TV2):** Viết và chạy `src/lab13.py` (3 phép thử, trace, độ nhạy, cỡ mẫu).
- **Chuyên viên chi phí (TV3):** Kiểm số đối chứng, hoàn thiện `bang_chi_phi.md` và rủi ro kinh tế.
- **Chuyên viên đánh giá lỗi (TV4):** Gắn nhãn độc lập 20 ca ở CP3, hoàn thiện `bang_loi.md`.
- **Quản trị hồ sơ & chỉ số (TV5):** Gắn nhãn độc lập 20 ca ở CP3, đặc tả chỉ số `chi_so.md`, giữ và chốt `ho_so_launch_v0.md`.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

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

## Hồ Văn Dũng (2A202603458)

### Phần việc phụ trách

- TV4, phụ trách phân loại và đánh giá lỗi trong nhiệm vụ C.

### Đóng góp cụ thể

- Tổng hợp 20 nhãn có đối chiếu hướng dẫn Lab, ghi căn cứ từng ca và đề xuất 5 biện pháp khắc phục có cách phát hiện đo được.

### Bằng chứng

- [Bảng lỗi và cách khắc phục](report/team/bang_loi.md)
- [Báo cáo cá nhân](report/team/2A202603458_HoVanDung.md)
