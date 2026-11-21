# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- **Nhóm chấm (hội đồng):** Huong (Nhóm 4 — K5-L3A)
- **Nhóm được chấm:** botusieudang (Nhóm của Dương Văn Công — dcongdev · K5-L3A)
- **Repo nhóm được chấm:** `https://github.com/dcongdev/K5-L3A-DAY13-botusieudang-LaunchEconomics` (commit: `cf3c40c` / `55ddd16`)

---

## Bảng điểm thẩm định Gate 2a (Thang điểm 30)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do đánh giá (có số liệu chứng minh) |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **C6 — Đề xuất khớp bằng chứng** | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **10 / 10** | **Rất xuất sắc:** Nhóm đề xuất **"Go có điều kiện"** rất chặt chẽ. Nhóm không hề né tránh mà liệt kê đầy đủ 5 con số bất lợi lớn: (1) Xem lại 100% vọt lên 11.743 đ (0,98×) đến 12.414 đ (1,03× - đắt hơn người làm) [simulated]; (2) Chi phí so với 12.000 đ phải tính cả hệ thống là 0,49× [simulated] chứ không lấy 0,37×; (3) 40 nhân viên không đủ phát hiện mức chênh 5 điểm, chấp nhận MDE 6 điểm với power chỉ 0,64; (4) Đơn hàng nặng có tỉ lệ mở lại 8,23% cao hơn trần 6%; (5) Tỉ lệ mở lại hiện tại 3,97% nên không dùng trần tuyệt đối 3%. Đi kèm 4 điều kiện ràng buộc có vai trò và ngày kiểm tra cụ thể. |
| **C7 — Số giả lập và phạm vi** | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **10 / 10** | **Chuẩn mực:** Toàn bộ các con số bắt nguồn từ phút giả lập (`phut_xem_lai_simulated`, `phut_lam_lai_simulated`, CPS 4.472 đ, kịch bản B1-B4, chi phí hệ thống 5.865 đ) đều có nhãn `[simulated]` nghiêm túc. Phạm vi pilot thu hẹp thông minh về `noi_dia` (0,22×) và `hang_nang` (0,69×), loại bỏ `quoc_te` (1,88×, thành công 27,3%, attempt 3 chỉ đúng 2,2%) và `doi_tac` (0,85× có điều khoản riêng). Có tính đủ chi phí cố định 40tr/tháng ở quy mô 45k đơn (0,38×) và một nửa (0,48×). |
| **C8 — Pilot ra được quyết định** | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **10 / 10** | **Khoa học & Thực tế:** Thiết kế chia theo nhân viên (20 trợ lý vs 20 đối chứng) đạt chuẩn 20 cụm/nhóm, phân tầng theo 12 depot có bốc thăm seed `20261207` ghi trước; cỡ mẫu MDE 6 điểm đạt $n = 859$, yêu cầu $m \ge 299$ đơn/người ($\text{DE} = 6,96$); 4 luật dừng tự động chuẩn cú pháp NẾU – TRONG – THÌ – KHÔNG THÌ với ngưỡng an toàn động (+2 điểm so với đối chứng kèm trần 6%); cơ chế rollback 30 phút do Giám đốc vận hành quyết định. |
| **TỔNG ĐIỂM HỘI ĐỒNG** | | | | **30 / 30** | **Hồ sơ chuẩn mực, bảo vệ xuất sắc, tính liêm chính dữ liệu cao.** |

---

## Quyết định của Hội đồng Gate 2a
* **Phán quyết:** **GO CÓ ĐIỀU KIỆN** (Đồng thuận 100% với đề xuất của nhóm botusieudang).
* **Lý do:** Hồ sơ của nhóm botusieudang (dcongdev) đáp ứng hoàn hảo các yêu cầu khắt khe của Gate 2a. Nhóm thể hiện tư duy kinh tế AI sắc bén khi nhìn thấu tảng băng chìm giờ nhân viên (chiếm 92,5% chi phí), dũng cảm loại bỏ luồng đơn quốc tế không hiệu quả, và giải quyết bài toán cỡ mẫu cụm với tinh thần khoa học minh bạch.

---

## Câu hỏi chất vấn tại phiên bảo vệ & Câu trả lời của đội trình

### Câu hỏi chất vấn của Hội đồng (Nhóm Huong đặt ra):
> *"Tại mục 6 và phần chú thích D1 trong `pilot_plan.yaml`, nhóm bạn tính ra $m \ge 299$ yêu cầu trong phạm vi cho mỗi nhân viên trong suốt đợt pilot để đạt MDE 6 điểm. Với tiến độ rollout 3 bước `[0.10, 0.25, 0.50]` (mỗi bước 1 tuần) và nhóm tuyên bố chỉ bắt đầu đo chỉ số chính từ bước 0.50 (tức khi có đủ 20 nhân viên dùng trợ lý), thì 20 nhân viên này có kịp đạt đủ 299 đơn/người trước ngày ra quyết định 2027-01-14 không?"*

### Câu trả lời của đội trình (Nhóm botusieudang phản biện):
> *"Đội trình trả lời rất thuyết phục: Khối lượng đơn toàn công ty là 1.500 đơn/ngày, trong đó phạm vi noi_dia + hang_nang chiếm 982/1.200 = 81,8% (tương đương khoảng 1.227 đơn/ngày). Chia cho 40 nhân viên thì mỗi nhân viên xử lý trung bình ~30,7 đơn trong phạm vi mỗi ngày làm việc. Tại bước 0.50 (bắt đầu từ 2026-12-21 đến ngày nghiệm thu 2027-01-14, tức có khoảng 3 tuần làm việc ~15-18 ngày làm việc thực tế), mỗi nhân viên nhóm trợ lý sẽ tiếp nhận từ 460 đến 550 đơn, hoàn toàn vượt mức tối thiểu 299 đơn/người. Do đó, kế hoạch pilot bảo đảm thu thập thừa cỡ mẫu hiệu dụng để kết luận kiểm định."*

---

## Nhận xét chi tiết & Đóng góp hoàn thiện (Feedback chuyên môn gửi nhóm bạn)

1. **Điểm mạnh nổi bật:**
   - Cấu trúc hồ sơ và code chạy rất chuẩn mực, các phép thử A1, bảng A2, A3, B1-B4 đều khớp số 100%.
   - Việc kèm theo file `output_kiem_so.txt` và ghi rõ phép tính tay của thành viên Lê Quang Huy là bằng chứng đối chiếu độc lập rất giá trị.
   - Các điều kiện tiên quyết tại `ho_so_launch_v0.md` có phân công người phụ trách và ngày kiểm tra rất cụ thể, logic thời gian khớp hoàn hảo với ngày khởi động pilot.
2. **Góp ý hoàn thiện nhỏ (Improvement Suggestions):**
   - Trong `pilot_plan.yaml`, nhóm có thể làm rõ thêm cơ chế kiểm soát chất lượng dữ liệu: sau tuần rollout 10% đầu tiên, ai sẽ là người ký biên bản xác nhận thời gian xem lại/làm lại đo thực tế trước khi cập nhật vào bảng chi phí.
   - Tại `bang_loi.md`, việc 2 thành viên đạt tỉ lệ đồng thuận 100% (20/20 ca) là rất ấn tượng; tuy nhiên nếu có thêm 1-2 ca thảo luận về các góc nhìn dễ gây hiểu nhầm (như Ca 6 giữa Do người dùng và Ngữ cảnh) thì tính phản biện nhóm sẽ càng thêm thuyết phục.
