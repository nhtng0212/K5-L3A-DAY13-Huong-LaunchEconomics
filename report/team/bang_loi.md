# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Bảng nhãn TV4 và TV5

TV4 đã chốt 20 nhãn có đối chiếu [hướng dẫn Lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhãn-tham-khảo-cho-20-ca). Dấu — là ô chưa có dữ liệu. Rubric CP3 yêu cầu hai bộ nhãn độc lập để tính đồng thuận.

|  Ca | Nhãn TV4 đã chốt  | Nhãn TV5 | Trùng? | Nhãn thống nhất |
| --: | ----------------- | -------- | ------ | --------------- |
|   1 | Do người dùng     | —        | —      | —               |
|   2 | Hệ thống          | —        | —      | —               |
|   3 | Ngữ cảnh          | —        | —      | —               |
|   4 | Giới hạn hệ thống | —        | —      | —               |
|   5 | Ngầm              | —        | —      | —               |
|   6 | Do người dùng     | —        | —      | —               |
|   7 | Hệ thống          | —        | —      | —               |
|   8 | Hệ thống          | —        | —      | —               |
|   9 | Do người dùng     | —        | —      | —               |
|  10 | Ngữ cảnh          | —        | —      | —               |
|  11 | Giới hạn hệ thống | —        | —      | —               |
|  12 | Ngầm              | —        | —      | —               |
|  13 | Giới hạn hệ thống | —        | —      | —               |
|  14 | Do người dùng     | —        | —      | —               |
|  15 | Hệ thống          | —        | —      | —               |
|  16 | Ngữ cảnh          | —        | —      | —               |
|  17 | Ngầm              | —        | —      | —               |
|  18 | Ngữ cảnh          | —        | —      | —               |
|  19 | Giới hạn hệ thống | —        | —      | —               |
|  20 | Hệ thống          | —        | —      | —               |

**Tỷ lệ đồng thuận:** Chưa tính. Công thức là số ca trùng chia cho 20 rồi nhân 100%. Mục tiêu CP3 là ít nhất 16/20 (80%).

**Quy tắc cho ca lệch:** Sau khi đối chiếu, mỗi ca lệch ghi một câu giải thích căn cứ chọn nhãn thống nhất. Nếu dưới 80%, nhóm ghi lại định nghĩa đã làm rõ trước khi tiếp tục.

## Căn cứ phân loại của TV4

|  Ca | Nhãn chốt         | Căn cứ                                                                                                                       |
| --: | ----------------- | ---------------------------------------------------------------------------------------------------------------------------- |
|   1 | Do người dùng     | Số tài khoản khách nhập thiếu 2 chữ số, khiến ngân hàng từ chối lệnh hoàn.                                                   |
|   2 | Hệ thống          | Kiện 28 kg bị tra theo bảng giá hàng thường, khiến khách nhận thiếu 45.000 đ.                                                |
|   3 | Ngữ cảnh          | Tiền về ví LogiX đúng thiết kế. Khách kỳ vọng tiền về tài khoản ngân hàng.                                                   |
|   4 | Giới hạn hệ thống | LogiX thiếu dữ liệu chặng do hãng nước ngoài giao, nên trợ lý không xác định được trạng thái.                                |
|   5 | Ngầm              | Kiểm tra mẫu cuối tuần mới phát hiện 14 đơn được hoàn theo giá trước giảm.                                                   |
|   6 | Do người dùng     | Khách chọn luồng giao trễ cho một kiện hàng bị vỡ.                                                                           |
|   7 | Hệ thống          | Trợ lý báo hoàn thành công dù sổ cái trả lỗi 503 và chưa xác nhận giao dịch.                                                 |
|   8 | Hệ thống          | Trợ lý viện dẫn điều 7.2 trong câu trả lời dù chính sách hiện hành không có điều này.                                        |
|   9 | Do người dùng     | Khách nhập mã đơn của sàn vào ô yêu cầu mã vận đơn.                                                                          |
|  10 | Ngữ cảnh          | Trợ lý áp dụng đúng điều khoản bất khả kháng khi có bão. Cam kết giao trong 24 giờ trên ứng dụng tạo kỳ vọng khác cho khách. |
|  11 | Giới hạn hệ thống | Trợ lý chưa hỗ trợ tin nhắn thoại, nên yêu cầu khách nhập bằng chữ.                                                          |
|  12 | Ngầm              | Kết quả vẫn đúng, che khuất việc gọi tool nhiều lần và tiền token ở D05 gấp 3 trong 3 tuần.                                  |
|  13 | Giới hạn hệ thống | Hoàn phí bảo hiểm của đối tác nằm ngoài phạm vi trợ lý.                                                                      |
|  14 | Do người dùng     | Khách bấm nhầm xác nhận đã nhận tiền, khiến yêu cầu bị đóng.                                                                 |
|  15 | Hệ thống          | Trợ lý tính hoàn 100% thay cho 50%. Nhân viên phát hiện trước khi gửi.                                                       |
|  16 | Ngữ cảnh          | Trợ lý gửi thông báo ngay khi xử lý xong theo thiết kế. Giờ gửi 2:14 sáng gây phiền cho khách.                               |
|  17 | Ngầm              | Bảng giá cũ gây chênh 1.000–2.000 đ trên 212 đơn trong 9 ngày, không có yêu cầu nào được mở lại.                             |
|  18 | Ngữ cảnh          | Mức hoàn 15.000 đ đúng chính sách. Khách tưởng hoàn thiếu vì tin nhắn thiếu phép tính.                                       |
|  19 | Giới hạn hệ thống | Đơn từ 14 tháng trước vượt phạm vi dữ liệu 12 tháng của trợ lý.                                                              |
|  20 | Hệ thống          | Lệnh thứ hai thiếu khóa chống trùng, khiến cùng một khoản được hoàn hai lần.                                                 |

Phân bố 20 ca gồm 4 lỗi do người dùng, 5 lỗi hệ thống, 4 lỗi ngữ cảnh, 4 lỗi giới hạn hệ thống và 3 lỗi ngầm.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Các ngưỡng dưới đây là đề xuất của TV4. Mỗi event cần có `trace_id` để truy vết yêu cầu.

|  Ca | Loại lỗi          | Phát hiện bằng gì                                                                                                                                                        | Khắc phục thế nào                                                                                                                     | Ai phụ trách                        |
| --: | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
|   1 | Do người dùng     | Kiểm tra định dạng tài khoản trước mỗi lệnh hoàn. Ghi `refund_account_validation_failed` và chặn lệnh ngay khi có 1 lỗi định dạng theo ngân hàng đã chọn.                | Hiển thị yêu cầu định dạng để khách sửa. Chỉ gửi lệnh khi thông tin hợp lệ.                                                           | Kỹ sư phụ trách tích hợp thanh toán |
|  20 | Hệ thống          | Theo dõi `refund_ledger_write` theo thời gian thực. Cảnh báo khi cùng một mã khoản hoàn có từ 2 giao dịch ghi thành công.                                                | Dùng khóa chống trùng cố định cho cùng khoản hoàn và áp dụng ràng buộc duy nhất tại sổ cái. Đối soát ngay khi có cảnh báo hoàn trùng. | Kỹ sư trưởng agent                  |
|   3 | Ngữ cảnh          | Trước mỗi lần xác nhận, so nơi khách muốn nhận với nơi trợ lý dự kiến hoàn. Ghi `refund_destination_mismatch` và hiện giải thích ngay khi có 1 lần lệch.                 | Hiển thị nơi nhận là ví LogiX, thời gian dự kiến và cách dùng số dư. Cho khách xác nhận trước khi gửi lệnh.                           | Trưởng nhóm CSKH                    |
|   4 | Giới hạn hệ thống | Kiểm tra dữ liệu từng chặng khi tiếp nhận yêu cầu. Nếu thiếu từ 1 chặng, ghi `handoff_to_staff` với lý do `missing_carrier_leg_data`. Thống kê số lượt chuyển hằng ngày. | Nêu rõ chặng chưa tra được. Chuyển yêu cầu cùng mã vận đơn, chặng thiếu và thông tin đã xác minh cho nhân viên.                       | Trưởng nhóm CSKH                    |
|   5 | Ngầm              | Hằng tuần kiểm tra mẫu đơn có mã giảm giá bằng `audit_sample_checked`. Mở điều tra nếu phát hiện ít nhất 1 đơn hoàn thừa.                                                | Tính tiền hoàn từ số thực trả sau giảm giá. Đối soát các khoản đã hoàn sai và kiểm tra cách tính trên đơn có mã giảm giá.             | Kế toán trưởng                      |
