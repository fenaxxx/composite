def yamada_sun(sigma_11, tau_12, mat):
    f1t = mat.f_1_t
    f1c = mat.f_1_c
    f12 = mat.f_12
    if sigma_11 >=0:
        rf = 1 / ((sigma_11/f1t)**2+(tau_12/f12)**2)**0.5
    else:
        rf = 1 / ((sigma_11/f1c)**2+(tau_12/f12)**2)**0.5
    return rf
def k_s(sigma_33, tau_13, mat):
    f3t = mat.f_3_t
    f3c = mat.f_3_c
    f13 = mat.f_13
    a = (sigma_33**2/f3t/f3c+tau_13**2/f13**2)
    b = sigma_33*(1/f3t-1/f3c)
    rf = (-b + (b**2 -4 * a * (-1))**0.5) / 2 / a
    return rf
def puck(simg11, sigma22, tau12, mat):
    f1t = mat.f_1_t
    f2t = mat.f_2_t
    f2c = mat.f_2_c
    f12 = mat.f_12
    aa = (simg11 / 2 / f1t)**2 + sigma22**2 / abs(f2t * f2c) + (tau12 / f12)**2
    bb = sigma22 * (1 / f2t + 1 / f2c)
    cc = -1
    rf = (-bb + (bb**2 - 4 * aa * cc)**0.5) / 2 / aa
    return rf
