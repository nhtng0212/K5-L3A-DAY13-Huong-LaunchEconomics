"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python lab13.py
Toàn bộ dữ liệu trong hai file CSV là giả lập.
"""
import math
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai

    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong > 0 else 0,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs)
    )


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    print("=" * 60)
    print("NHIỆM VỤ A1: KIỂM TRA ĐÁP ÁN BIẾT TRƯỚC")
    print("=" * 60)
    kiem_tra_dap_an_biet_truoc()

    print("\n" + "=" * 60)
    print("NHIỆM VỤ A2: MÔ HÌNH CHI PHÍ TRACE (CẢ 1.200 YÊU CẦU)")
    print("=" * 60)
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:16s} {gia_tri:>14,.1f}')
    print(f"-> Tỷ số Chi phí mỗi việc thành công / Hoá đơn: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần")
    print(f"-> Tỷ trọng làm lại [simulated]: {ket_qua['lam_lai'] / ket_qua['tong'] * 100:.1f}%")
    print(f"-> Tỷ trọng xem lại [simulated]: {ket_qua['xem_lai'] / ket_qua['tong'] * 100:.1f}%")
    print(f"-> Tỷ trọng giờ nhân viên [simulated]: {(ket_qua['xem_lai'] + ket_qua['lam_lai']) / ket_qua['tong'] * 100:.1f}%")

    print("\n" + "=" * 60)
    print("NHIỆM VỤ A3: PHÂN TÍCH THEO TỪNG LOẠI YÊU CẦU")
    print("=" * 60)
    print(f"{'Loai':12s} | {'Số YC':>6s} | {'Thành công':>10s} | {'Runs/YC':>8s} | {'CPS [sim]':>12s} | {'So Baseline':>11s}")
    print("-" * 70)
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub_reqs = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub_reqs)
        so_yc = len(sub_reqs)
        ti_le_tc = kq['thanh_cong'] / so_yc
        sub_runs = runs[runs['request_id'].isin(sub_reqs['request_id'])]
        lan_chay_tb = len(sub_runs) / so_yc
        boi_so = kq['cps'] / BASELINE
        print(f"{loai:12s} | {so_yc:6d} | {ti_le_tc*100:9.1f}% | {lan_chay_tb:8.2f} | {kq['cps']:10,.0f} đ | {boi_so:10.2f}x")

    print("\nTỉ lệ lần chạy status == 'ok' theo từng lần thử (attempt):")
    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['is_ok'] = (merged['status'] == 'ok').astype(float)
    pvt = merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean')
    print((pvt * 100).round(1).to_string())

    print("\n" + "=" * 60)
    print("NHIỆM VỤ A4: CHI PHÍ CỐ ĐỊNH (noi_dia + hang_nang)")
    print("=" * 60)
    sub_nd_hn = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_nd_hn = mo_hinh(runs, sub_nd_hn)
    so_tc_sample = kq_nd_hn['thanh_cong']
    tong_yc_sample = len(reqs)
    tc_thang_full = 45000 * so_tc_sample / tong_yc_sample
    cp_co_dinh_moi_yc_full = 40_000_000 / tc_thang_full
    cps_full = kq_nd_hn['cps'] + cp_co_dinh_moi_yc_full

    tc_thang_half = tc_thang_full / 2
    cp_co_dinh_moi_yc_half = 40_000_000 / tc_thang_half
    cps_half = kq_nd_hn['cps'] + cp_co_dinh_moi_yc_half

    print(f"Biến phí mỗi việc thành công [simulated]: {kq_nd_hn['cps']:,.0f} đ")
    print(f"Quy mô đầy đủ (45k đơn/tháng): Cố định = {cp_co_dinh_moi_yc_full:,.0f} đ/yc -> Tổng CPS = {cps_full:,.0f} đ ({cps_full/BASELINE:.2f}x) [simulated]")
    print(f"Quy mô giảm một nửa (pilot):     Cố định = {cp_co_dinh_moi_yc_half:,.0f} đ/yc -> Tổng CPS = {cps_half:,.0f} đ ({cps_half/BASELINE:.2f}x) [simulated]")

    print("\n" + "=" * 60)
    print("NHIỆM VỤ B1 & B2: BẢNG ĐỘ NHẠY (9 KỊCH BẢN & ĐỔI MỘT CẶP)")
    print("=" * 60)
    kich_ban = {
        'Gốc (A2)':                 dict(),
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2.0),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2.0),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    for ten, kw in kich_ban.items():
        res = mo_hinh(runs, reqs, **kw)
        cps = res['cps']
        pct = (cps / goc - 1) * 100
        print(f"{ten:28s}: {cps:8,.0f} đ [sim] ({pct:+6.1f}%)")

    # B2: Đổi một cặp (token x2 và xem lại x2)
    res_b2 = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)
    pct_b2 = (res_b2['cps'] / goc - 1) * 100
    print(f"{'B2: Token x2 & Xem lại x2':28s}: {res_b2['cps']:8,.0f} đ [sim] ({pct_b2:+6.1f}%)")

    print("\n" + "=" * 60)
    print("NHIỆM VỤ B3: GIỚI HẠN CHẠY LẠI & CHI PHÍ TOÀN HỆ THỐNG")
    print("=" * 60)
    print(f"{'Giới hạn':10s} | {'Tổng trợ lý [sim]':>18s} | {'Không TC':>8s} | {'Cả hệ thống [sim]':>18s} | {'CPS trợ lý [sim]':>16s}")
    print("-" * 80)
    for k in [1, 2, 3]:
        res_k = mo_hinh(runs, reqs, max_lan_chay=k if k < 3 else None)
        khong_tc = len(reqs) - res_k['thanh_cong']
        tong_he_thong = res_k['tong'] + khong_tc * BASELINE
        print(f"Max {k} lần  | {res_k['tong']:16,.0f} đ | {khong_tc:8d} | {tong_he_thong:16,.0f} đ | {res_k['cps']:14,.0f} đ")

    print("\n" + "=" * 60)
    print("NHIỆM VỤ B4: XEM LẠI 100% (noi_dia + hang_nang: 982 YÊU CẦU)")
    print("=" * 60)
    # 982 yêu cầu noi_dia + hang_nang
    runs_nd_hn = runs[runs['request_id'].isin(sub_nd_hn['request_id'])]
    tien_token_tool = (runs_nd_hn['tokens_in'] / 1000 * 26 + runs_nd_hn['tokens_out'] / 1000 * 130 + runs_nd_hn['tool_calls'] * 15).sum()
    runs_ok_req_ids = runs_nd_hn[runs_nd_hn['status'] == 'ok']['request_id'].unique()
    so_yc_co_ok = len(set(runs_ok_req_ids).intersection(set(sub_nd_hn['request_id'])))
    tien_xem_lai_100 = so_yc_co_ok * 5 * 2000  # 5 phút mỗi yc
    so_ca_lam_lai = (sub_nd_hn['ket_qua'] == 'lam_lai').sum()
    tc_nd_hn = (sub_nd_hn['ket_qua'] == 'thanh_cong').sum()

    # Kịch bản 1: 9 phút làm lại
    tien_lam_lai_9m = so_ca_lam_lai * 9 * 2000
    tong_b4_9m = tien_token_tool + tien_xem_lai_100 + tien_lam_lai_9m
    cps_b4_9m = tong_b4_9m / tc_nd_hn

    # Kịch bản 2: 15.3 phút làm lại (trung bình thực tế)
    tien_lam_lai_15m = so_ca_lam_lai * 15.3 * 2000
    tong_b4_15m = tien_token_tool + tien_xem_lai_100 + tien_lam_lai_15m
    cps_b4_15m = tong_b4_15m / tc_nd_hn

    print(f"Số yc có ít nhất 1 lần ok (xem lại 5p): {so_yc_co_ok} -> Tiền xem lại: {tien_xem_lai_100:,.0f} đ")
    print(f"Token + Tool: {tien_token_tool:,.0f} đ | Số việc thành công: {tc_nd_hn} | Số ca làm lại: {so_ca_lam_lai}")
    print(f"1) Với 9,0 phút làm lại/ca:  Tổng = {tong_b4_9m:11,.0f} đ -> CPS = {cps_b4_9m:6,.0f} đ ({cps_b4_9m/BASELINE:.2f}x) [simulated]")
    print(f"2) Với 15,3 phút làm lại/ca: Tổng = {tong_b4_15m:11,.0f} đ -> CPS = {cps_b4_15m:6,.0f} đ ({cps_b4_15m/BASELINE:.2f}x) [simulated]")

    print("\n" + "=" * 60)
    print("NHIỆM VỤ D1: CỠ MẪU CHO PILOT (HỖ TRỢ THÀNH VIÊN 1)")
    print("=" * 60)
    n_yc = co_mau(0.70, 0.75)
    print(f"a) Chia theo yêu cầu (co_mau 0.70 -> 0.75): {n_yc} yêu cầu mỗi nhóm")
    m_staff = 75
    icc = 0.02
    de_staff = 1 + (m_staff - 1) * icc
    n_staff_req = math.ceil(n_yc * de_staff)
    staff_needed = math.ceil(n_staff_req / m_staff)
    print(f"b) Theo nhân viên m=75: DE = {de_staff:.2f}, n = {n_staff_req} -> cần {staff_needed} người/nhóm (tổng {staff_needed*2} > 40: KHÔNG ĐỦ)")
    n_eff_20_staff = 20 / icc
    print(f"c) Giới hạn 20 nhân viên mỗi nhóm: n_hiệu_dụng tối đa c/ICC = {n_eff_20_staff:,.0f} < {n_yc} (KHÔNG ĐẠT)")
    n_eff_6_depot = 6 / icc
    print(f"d) 6 depot mỗi nhóm: c/ICC = {n_eff_6_depot:,.0f} (KHÔNG ĐẠT)")
    n_6pt = co_mau(0.70, 0.76)
    # 20m / (1 + (m-1)*0.02) >= n_6pt
    # 20m >= n_6pt * 0.98 + n_6pt * 0.02 * m
    # m * (20 - 0.02 * n_6pt) >= n_6pt * 0.98
    m_req = (n_6pt * 0.98) / (20 - 0.02 * n_6pt)
    de_6pt = 1 + (math.ceil(m_req) - 1) * icc
    print(f"e) Mức chênh 6 điểm ({n_6pt} đơn/nhóm), 20 người/nhóm: m >= {math.ceil(m_req)} đơn/người (DE = {de_6pt:.2f})")

    print("\n" + "=" * 60)
    print("NHIỆM VỤ E1: TÍNH THỬ CHỈ SỐ (HỖ TRỢ THÀNH VIÊN 5)")
    print("=" * 60)
    chinh = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).mean()
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).mean()
    an_toan = (reqs['mo_lai_trong_7_ngay'] == 1).mean()
    print(f"1. Chỉ số chính (% đóng 24h & không mở lại 7 ngày): {chinh*100:.2f}% ({(chinh*len(reqs)):.0f}/{len(reqs)})")
    print(f"2. Chỉ số dùng (Tỉ lệ bỏ qua sửa + bỏ / xem lại):   {bo_qua*100:.2f}% ({(bo_qua*len(xem)):.0f}/{len(xem)})")
    print(f"3. Chỉ số an toàn (% mở lại trong 7 ngày):         {an_toan*100:.2f}% ({(an_toan*len(reqs)):.0f}/{len(reqs)})")
    print("=" * 60)
