# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- **Nhóm chấm (hội đồng):** Nhóm 4
- **Nhóm được chấm:** Nhóm 5

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| **Đề xuất khớp bằng chứng** | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **10** | Đề xuất "Go có điều kiện" nêu rõ ràng con số bất lợi: chi phí khi xem lại 100% vọt lên 11.743 đ (0,98× baseline) [simulated], và đưa ra giải pháp giảm xem lại theo bậc kèm điều kiện tiên quyết sửa lỗi hoàn trùng (ca 7, 20) trước khi chạy. |
| **Số giả lập và phạm vi** | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **10** | Tất cả các con số bắt nguồn từ cột `_simulated` (chi phí 4.472 đ, thời gian làm lại, xem lại) đều được gắn nhãn `[simulated]` đầy đủ; phạm vi pilot được thu hẹp về `noi_dia` (2.696 đ, 0,22×) và `hang_nang` (8.221 đ, 0,69×), loại trừ `quoc_te` (22.515 đ, 1,88×). |
| **Pilot ra được quyết định** | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **10** | Thiết kế phân ngẫu nhiên 20 nhân viên/nhóm có đối chứng đồng thời; cỡ mẫu MDE 6 điểm đạt 859 đơn/nhóm (DE = 6,96); 3 luật dừng đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ với ngưỡng đo thực tế (ngưỡng an toàn chênh 2 điểm so với đối chứng, trần 6%), có vai trò cụ thể có thẩm quyền dừng (Giám đốc vận hành). |
| **Tổng** | | | | **30 / 30** | **Xuất sắc: Bằng chứng định lượng chặt chẽ, không giấu số liệu bất lợi.** |

**Quyết định của hội đồng:** **Go có điều kiện**

**Lý do:** Hồ sơ của Nhóm 5 thể hiện sự trung thực cao trong đánh giá kinh tế của Agent, không chỉ nhìn vào hóa đơn token mà tính đầy đủ chi phí nhân viên can thiệp (chiếm 92,5% tổng chi phí [simulated]). Nhóm thẳng thắn loại bỏ luồng quốc tế không hiệu quả và đưa ra thiết kế pilot chuẩn mực với quy tắc an toàn có cơ sở khoa học.

**Một câu hỏi cho đội trình:**  
*"Trong bảng độ nhạy B4, nếu tuần đầu tiên đội ngũ CSKH bắt buộc phải duyệt xem lại 100% các yêu cầu của nhóm can thiệp thì chi phí mỗi việc thành công là bao nhiêu so với mốc 12.000 đ của nhân viên tự làm, và nhóm có phương án xử lý rủi ro này như thế nào để không bị lỗ ngân sách?"*

**Câu trả lời của đội trình (ghi lại tại buổi):**  
*"Đội trình trả lời rất chính xác: Theo tính toán tại bảng B4, khi xem lại 100% thì chi phí mỗi việc thành công là 11.743 đ (0,98× so với 12.000 đ) nếu thời gian làm lại là 9 phút, hoặc lên đến 12.414 đ (1,03× so với 12.000 đ - đắt hơn người tự làm) nếu thời gian làm lại thực tế là 15,3 phút. Để xử lý rủi ro này, nhóm đã cài đặt ngay điều kiện tiên quyết số 4: Giám đốc CSKH ban hành quy trình giảm xem lại theo bậc (rollout 10% → 25% → 50%), chỉ duy trì kiểm tra 100% trong 3 ngày đầu của bước 10%; khi tỷ lệ nhân viên sửa/bỏ < 15% sẽ lập tức chuyển sang kiểm tra xác suất ngẫu nhiên 20%, giúp chi phí bình quân ổn định ở mức dưới 5.000 đ."*
