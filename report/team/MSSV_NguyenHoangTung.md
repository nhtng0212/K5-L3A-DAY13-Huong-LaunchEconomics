# Báo cáo cá nhân — Nguyễn Hoàng Tùng

> **Lưu ý:** Đổi tên file này thành `<MSSV>_NguyenHoangTung.md` (ví dụ `20241234_NguyenHoangTung.md`) theo đúng cú pháp bài nộp khi điền MSSV chính thức.

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hoàng Tùng
- MSSV: [Điền MSSV của bạn vào đây]
- Email: nguyentungpcbv@gmail.com
- Vai trong nhóm: Nhóm trưởng (TV1), Kiến trúc sư Pilot (Pilot Architect), Chủ trì Duyệt chéo Gate 2a.

## 2. Phần việc phụ trách

- Phụ trách quản lý và điều phối tổng thể nhóm 5 thành viên; ban hành tài liệu tác chiến [PHAN_CONG_NHOM.md](../../PHAN_CONG_NHOM.md) với prompt mẫu chuẩn cho từng vai trò.
- Trực tiếp sở hữu và hoàn thiện toàn bộ **Nhiệm vụ D: Kế hoạch Pilot** trong file [pilot_plan.yaml](pilot_plan.yaml).
- Phụ trách tính toán lý thuyết cỡ mẫu thử nghiệm ngẫu nhiên theo cụm (Cluster RCT), phân tích hệ số thiết kế (Design Effect), và đề xuất đánh đổi MDE khả thi.
- Soạn thảo 3 luật dừng tự động (Stop Rules) và cơ chế hoàn tác khẩn cấp (Rollback) 30 phút.
- Chủ trì đại diện nhóm trình bày bảo vệ hồ sơ và phản biện trước nhóm đối tác tại phiên duyệt chéo Gate 2a.

## 3. Đóng góp cụ thể

1. **Kiến trúc Kế hoạch Pilot ([pilot_plan.yaml](pilot_plan.yaml)):**
   - Hoàn thiện 100% các trường dữ liệu theo chuẩn YAML, xóa sạch toàn bộ dấu `?` và kiểm tra xác thực bằng `yaml.safe_load`.
   - Thu hẹp phạm vi pilot thông minh: Chọn `noi_dia` (chi phí 2.696 đ = 0,22×) và `hang_nang` (8.221 đ = 0,69×, simulated). Loại bỏ `quoc_te` (22.515 đ = 1,88×, chạy lại không hiệu quả) và `doi_tac` (0,85×).
   - Thiết kế lộ trình rollout 3 bước `[0.10, 0.25, 0.50]` tương ứng 4 $\rightarrow$ 10 $\rightarrow$ 20 nhân viên.
2. **Chứng minh & Tính toán Thống kê Cỡ mẫu (Nhiệm vụ D1):**
   - Phân tích và chứng minh lý thuyết: Khi chia thử nghiệm theo nhân viên ($c = 20$ cụm mỗi nhóm, $\text{ICC} = 0,02$), cỡ mẫu hiệu dụng tối đa $n_{\text{effective}} < c/\text{ICC} = 1.000$. Do đó, không thể đạt được $n = 1.251$ để phát hiện mức chênh 5 điểm với power 0,80.
   - Đưa ra quyết định kinh doanh - kỹ thuật: Nâng MDE lên 6 điểm ($0,70 \rightarrow 0,76$), cỡ mẫu cần 859 đơn/nhóm, đòi hỏi $m \ge 299$ đơn/nhân viên ($\text{DE} = 6,96$). Đồng thời công khai đánh đổi: Nếu tác động thực tế chỉ là 5 điểm, power kiểm định thực tế là 0,64.
3. **Bảo đảm tính Tách tác động (Identifiability - D2):**
   - Thiết lập đối chứng song song (Concurrent Control) giữa 20 nhân viên can thiệp và 20 nhân viên đối chứng trong cùng 12 depot.
   - Giảm thiểu rủi ro lan tỏa (Spillover) bằng phân quyền tài khoản cá nhân `staff_id` và ghi log `trace_id`.
4. **Xây dựng 3 Luật dừng (Stop Rules):**
   - Dựa trên tỉ lệ mở lại thực tế 4,25% để đặt ngưỡng an toàn: chênh $\ge 2$ điểm phần trăm so với đối chứng hoặc trần tuyệt đối 6%, hoặc $\ge 1$ ca hoàn trùng.
   - Luật dừng chi phí: Chi phí mỗi việc thành công $> 8.000\text{ đ}$ trong 2 tuần liên tiếp.
   - Luật dừng mức độ sử dụng: Tỉ lệ bỏ qua gợi ý $> 40\%$ trong 1 tuần.

## 4. Bằng chứng

- [Kế hoạch pilot hoàn chỉnh (pilot_plan.yaml)](pilot_plan.yaml)
- [Bảng phân công nhóm tác chiến (PHAN_CONG_NHOM.md)](../../PHAN_CONG_NHOM.md)
- Bảng phân vai nhóm trong [TEAM.md](../../TEAM.md)
- Commit quản trị và phản biện tại phiên duyệt chéo Gate 2a.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity AI Agent (Gemini 3.8 Flash).
- **Mục đích:**
  - Hỗ trợ giải phương trình phi tuyến tính để tìm số đơn tối thiểu mỗi nhân viên $m \ge 299$ theo công thức $20m / (1 + (m-1) \times 0,02) \ge 859$.
  - Rà soát cú pháp YAML và tự động kiểm tra vi phạm quy tắc cấm (từ cấm vận hành chính thức và dấu "?").
  - Xây dựng cấu trúc ma trận phân công 5 người để loại bỏ xung đột git và nghẽn việc.
- **Tự kiểm tra:**
  - Tự tay bấm máy tính kiểm tra lại các giá trị $Z_{1-\alpha/2} = 1,96$ và $Z_{1-\beta} = 0,84$.
  - Chạy lệnh Python độc lập `yaml.safe_load` để xác nhận file không bị lỗi format.
  - Đối chiếu số liệu baseline 4,25% từ dữ liệu thực tế trước khi chốt ngưỡng an toàn trong luật dừng.

## 6. Tự đánh giá

- Hoàn thành xuất sắc vai trò Nhóm trưởng: Lập kế hoạch rõ ràng, phân công mạch lạc, không để thành viên bị tắc nghẽn công việc.
- Hoàn thiện phần việc kỹ thuật cá nhân (Nhiệm vụ D) sớm hơn mốc thời gian quy định với độ chuẩn xác tuyệt đối, sẵn sàng bảo vệ lý lẽ và số liệu trước hội đồng Gate 2a.
- Mức độ đóng góp: Đạt 100% mục tiêu đề ra.
