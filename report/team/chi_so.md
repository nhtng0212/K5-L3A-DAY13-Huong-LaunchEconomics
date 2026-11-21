# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Chỉ số trong đợt chạy thử 2 tuần trên mẫu 1.200 yêu cầu (không viết "trợ lý đã nâng chỉ số" vì đợt chạy thử chưa có nhóm đối chứng):

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200 yêu cầu) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177 yêu cầu được xem lại) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200 yêu cầu; trong phạm vi noi_dia + hang_nang là 3,97%) |
| Dùng (tự đề xuất) | Tỉ lệ yêu cầu trong nhóm can thiệp được mở bằng trợ lý | Số yêu cầu nhóm pilot có `agent_suggestion_shown`, chia tổng yêu cầu nhóm pilot tiếp nhận | Không cần tính (đo trong pilot) |
| An toàn (tự đề xuất) | Tỉ lệ đơn hoàn sai tiền phát hiện qua kiểm toán mẫu hằng tuần | Số đơn kiểm toán có `so_tien_da_hoan != so_tien_dung`, chia số đơn kiểm toán mẫu (`audit_sample_checked`) | Không cần tính (bắt lỗi ngầm như ca 5, 17) |

## Danh sách event

Hệ thống ghi nhận 10 event chuẩn, mỗi event bắt buộc có trường `trace_id` để liên kết thông suốt từ yêu cầu của khách đến trace thực thi của agent:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / Cổng tiếp nhận | `request_id`, `loai`, `so_tien_yeu_cau`, `arm`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent runtime | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status` (`ok`/`loi`), `trace_id` | Sau mỗi lần chạy agent, kể cả khi lỗi |
| `agent_suggestion_shown` | Giao diện CSKH | `staff_id`, `so_tien_de_xuat`, `phuong_an`, `trace_id` | Khi gợi ý của trợ lý hiện ra trên màn hình |
| `staff_review_decision` | Nhân viên CSKH | `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai` (đo thực tế), `trace_id` | Khi nhân viên bấm gửi, sửa hoặc bỏ qua gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `staff_id`, `phut_lam_lai` (đo thực tế), `ly_do_lam_lai`, `trace_id` | Khi nhân viên hoàn thành xử lý thủ công |
| `refund_ledger_write` | Dịch vụ sổ cái kế toán | `idempotency_key`, `so_tien_hoan`, `ket_qua` (`success`/`failed`), `trace_id` | Khi ghi lệnh hoàn tiền vào sổ cái giao dịch |
| `handoff_to_staff` | Agent runtime | `reason` (lý do chuyển), `tom_tat_ngu_canh`, `trace_id` | Khi agent gặp giới hạn hệ thống cần chuyển người |
| `ticket_closed` | Hệ thống Ticket | `closed_at`, `duration_hours`, `dong_trong_24h` (0/1), `trace_id` | Khi yêu cầu được xử lý xong và đóng lại |
| `ticket_reopened` | Khách hàng | `reopened_at`, `days_since_closed`, `reason`, `trace_id` | Khi khách mở lại khiếu nại trong vòng 7 ngày |
| `audit_sample_checked` | Kế toán nội bộ | `so_tien_da_hoan`, `so_tien_dung`, `lech_tien`, `trace_id` | Hằng tuần khi kiểm tra mẫu ngẫu nhiên hồ sơ |

**Kiểm tra chéo:** Liên kết giữa chỉ số ở bảng E1 và các event đo lường:

1. **Chỉ số chính (% đóng trong 24h & không mở lại trong 7 ngày):** Đo từ `ticket_closed` (lấy thuộc tính `dong_trong_24h` hoặc `duration_hours <= 24`) kết hợp kiểm tra không tồn tại event `ticket_reopened` có cùng `trace_id` với `days_since_closed <= 7`.
2. **Chỉ số dùng (Tỉ lệ bỏ qua gợi ý):** Đo từ `staff_review_decision` bằng cách đếm số event có `quyet_dinh` thuộc `['sua', 'bo']` chia cho tổng số event `staff_review_decision` ghi nhận.
3. **Chỉ số an toàn (Tỉ lệ mở lại trong 7 ngày):** Đo bằng cách đếm số `trace_id` có phát sinh event `ticket_reopened` với `days_since_closed <= 7`, chia cho tổng số `refund_request_created`.
4. **Chỉ số dùng đề xuất (% mở bằng trợ lý):** Tỷ lệ giữa số `trace_id` có event `agent_suggestion_shown` trên tổng số `refund_request_created` gán vào nhóm pilot can thiệp (`arm == 'assistant'`).
5. **Chỉ số an toàn đề xuất (% đơn hoàn sai tiền qua kiểm toán):** Đo trực tiếp từ tập event `audit_sample_checked`, đếm số event có `so_tien_da_hoan != so_tien_dung` chia cho tổng số event kiểm toán mẫu.

## E2 · Rủi ro kinh tế

Các rủi ro kinh tế được định lượng trực tiếp từ kết quả phân tích độ nhạy (bảng B1, B3, B4 và A4 trong `bang_chi_phi.md`):

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| **Số ca làm lại tăng gấp đôi** | Chi phí mỗi việc thành công tăng +51,8%, từ 4.472 đ lên 6.787 đ [simulated], triệt tiêu hơn nửa phần tiết kiệm. | Tỉ lệ yêu cầu cần làm lại theo dõi hằng tuần vượt ngưỡng 7% (đợt chạy thử ghi nhận 4,9% trong phạm vi `noi_dia` + `hang_nang`). | Thu hẹp phạm vi chỉ giữ lại `noi_dia`, tạm dừng `hang_nang`; đồng thời rà soát ngay 20 trace làm lại gần nhất để phân tích nguyên nhân gốc. | PM trợ lý hoàn phí |
| **Bắt buộc xem lại 100% kéo dài** | Chi phí mỗi việc thành công vọt lên 11.743 đ (0,98× baseline) với 9 phút làm lại, hoặc lên 12.414 đ (1,03× baseline) nếu làm lại 15,3 phút như thực tế [simulated] (trợ lý đắt hơn người). | Tỉ lệ yêu cầu được xem lại vẫn duy trì > 50% vào cuối tuần thứ 2 (bước rollout 0.25). | Ban hành quy trình giảm xem lại theo bậc: chuyển sang kiểm tra xác suất ngẫu nhiên 20% khi tỉ lệ nhân viên sửa/bỏ < 15%. | Trưởng nhóm CSKH |
| **Khối lượng thực tế thấp hơn dự kiến** | Chi phí cố định 40 triệu đ/tháng phân bổ tăng từ 1.185 đ/việc (ở 45.000 đơn) lên 2.370 đ/việc nếu khối lượng giảm còn một nửa [simulated], đẩy tổng chi phí lên 5.784 đ (0,48×). | Số yêu cầu thành công theo tuần thấp hơn 50% kế hoạch phân bổ liên tiếp trong 2 tuần. | Giữ nguyên quy mô pilot không mở rộng thêm nhân viên; đàm phán lại hợp đồng hạ tầng máy chủ và chi phí cố định cho phù hợp lưu lượng thực. | PM trợ lý hoàn phí |
