import numpy as np


class Equ:
    def __init__(self, ka1 = 0, ka2 = 0, ka3 = 0, kd1 = 0, kd2 = 0, kg1 = 0, kg2 = 0, kg3 = 0):
        self.ka1 = ka1
        self.ka2 = ka2
        self.ka3 = ka3
        self.kd1 = kd1
        self.kd2 = kd2
        self.kg1 = kg1
        self.kg2 = kg2
        self.kg3 = kg3


    def set_c(self):
        ka1 = self.ka1
        ka2 = self.ka2
        ka3 = self.ka3
        kd1 = self.kd1
        kd2 = self.kd2
        kg1 = self.kg1
        kg2 = self.kg2
        kg3 = self.kg3

        ca = self.ca
        cd = self.cd
        cg = self.cg
        cb = self.cb
        cz = self.cz

        r = cz - cb
        kw = 10 ** -14

        t1 = kg1 + ka1
        t2 = kg1 * kg2 + ka1 * kg1 + ka1 * ka2
        t3 = kg1 * kg2 * kg3 + ka1 * kg1 * kg2 + ka1 * ka2 * kg1 + ka1 * ka2 * ka3
        t4 = ka1 * kg1 * kg2 * kg3 + ka1 * ka2 * kg1 * kg2 + ka1 * ka2 * ka3 * kg1
        t5 = ka1 * ka2 * kg1 * kg2 * kg3 + ka1 * ka2 * ka3 * kg1 * kg2
        t6 = ka1 * ka2 * ka3 * kg1 * kg2 * kg3

        h1 = kd1 + ka1
        h2 = kd1 * kd2 + ka1 * kd1 + ka1 * ka2
        h3 = ka1 * kd1 * kd2 + ka1 * ka2 * kd1 + ka1 * ka2 * ka3
        h4 = ka1 * ka2 * kd1 * kd2 + ka1 * ka2 * ka3 * kd1
        h5 = ka1 * ka2 * ka3 * kd1 * kd2

        m1 = kd1 + kg1
        m2 = kd1 * kd2 + kg1 * kd1 + kg1 * kg2
        m3 = kg1 * kd1 * kd2 + kg1 * kg2 * kd1 + kg1 * kg2 * kg3
        m4 = kg1 * kg2 * kd1 * kd2 + kg1 * kg2 * kg3 * kd1
        m5 = kg1 * kg2 * kg3 * kd1 * kd2

        t11 = kd1 * cd
        t22 = 2 * kd1 * kd2 * cd + kd1 * t1 * cd
        t33 = 2 * kd1 * kd2 * t1 * cd + kd1 * t2 * cd
        t44 = 2 * kd1 * kd2 * t2 * cd + kd1 * t3 * cd
        t55 = 2 * kd1 * kd2 * t3 * cd + kd1 * t4 * cd
        t66 = 2 * kd1 * kd2 * t4 * cd + kd1 * t5 * cd
        t77 = 2 * kd1 * kd2 * t5 * cd + kd1 * t6 * cd
        t88 = 2 * kd1 * kd2 * t6 * cd

        h11 = 3 * cg
        h22 = 2 * kg1 * cg + 3 * h1 * cg
        h33 = kg1 * kg2 * cg + 2 * kg1 * h1 *cg + 3 * h2 * cg
        h44 = kg1 * kg2 * h1 * cg + 2 * kg1 * h2 *cg + 3 * h3 * cg
        h55 = kg1 * kg2 * h2 * cg + 2 * kg1 * h3 *cg + 3 * h4 * cg
        h66 = kg1 * kg2 * h3 * cg + 2 * kg1 * h4 *cg + 3 * h5 * cg
        h77 = kg1 * kg2 * h4 * cg + 2 * kg1 * h5 *cg
        h88 = kg1 * kg2 * h5 * cg

        m11 = ka1 * ca
        m22 = ka1 * m1 * ca + 2 * ka1 * ka2 * ca
        m33 = ka1 * m2 * ca + 2 * ka1 * ka2 * m1 * ca + 3 * ka1 * ka2 * ka3 * ca
        m44 = ka1 * m3 * ca + 2 * ka1 * ka2 * m2 * ca + 3 * ka1 * ka2 * ka3 * m1 * ca
        m55 = ka1 * m4 * ca + 2 * ka1 * ka2 * m3 * ca + 3 * ka1 * ka2 * ka3 * m2 * ca
        m66 = ka1 * m5 * ca + 2 * ka1 * ka2 * m4 * ca + 3 * ka1 * ka2 * ka3 * m3 * ca
        m77 = 2 * ka1 * ka2 * m5 * ca + 3 * ka1 * ka2 * ka3 * m4 * ca
        m88 = 3 * ka1 * ka2 * ka3 * m5 * ca

        c1 = t1 + kd1
        c2 = t2 + kd1 * t1 + kd1 * kd2
        c3 = t3 + kd1 * t2 + kd1 * kd2 * t1
        c4 = t4 + kd1 * t3 + kd1 * kd2 * t2
        c5 = t5 + kd1 * t4 + kd1 * kd2 * t3
        c6 = t6 + kd1 * t5 + kd1 * kd2 * t4
        c7 = kd1 * t6 + kd1 * kd2 * t5
        c8 = kd1 * kd2 * t6

        self.j0 = -1
        self.j1 = r - h11 - c1
        self.j2 = m11 + t11 - h22 + kw + r * c1 - c2
        self.j3 = m22 + t22 - h33 + kw * c1 + r * c2 - c3
        self.j4 = m33 + t33 - h44 + kw * c2 + r * c3 - c4
        self.j5 = m44 + t44 - h55 + kw * c3 + r * c4 - c5
        self.j6 = m55 + t55 - h66 + kw * c4 + r * c5 - c6
        self.j7 = m66 + t66 - h77 + kw * c5 + r * c6 - c7
        self.j8 = m77 + t77 - h88 + kw * c6 + r * c7 - c8
        self.j9 = m88 + t88 + kw * c7 + r * c8
        self.j10 = kw * c8


    def f(self, x):
        return (x ** 10) * self.j0 + (x ** 9) * self.j1 + (x ** 8) * self.j2 + (x ** 7) * self.j3 + (x ** 6) * self.j4 + (x ** 5) * self.j5 + (
                x ** 4) * self.j6 + (x ** 3) * self.j7 + (x ** 2) * self.j8 + x * self.j9 + self.j10


    def df(self, x):
        return 10 * (x ** 9) * self.j0 + 9 * (x ** 8) * self.j1 + 8 * (x ** 7) * self.j2 + 7 * (x ** 6) * self.j3 + 6 * (x ** 5) * self.j4 + 5 * (
                x ** 4) * self.j5 + 4 * (x ** 3) * self.j6 + 3 * (x ** 2) * self.j7 + 2 * x * self.j8 + self.j9


    def calc(self, ca = 0, cd = 0, cg = 0, cb = 0, cz = 0):
        self.ca = ca
        self.cd = cd
        self.cg = cg
        self.cb = cb
        self.cz = cz
        ka1 = self.ka1
        ka2 = self.ka2
        ka3 = self.ka3
        kd1 = self.kd1
        kd2 = self.kd2
        kg1 = self.kg1
        kg2 = self.kg2
        kg3 = self.kg3

        self.set_c()

        x0 = float(0.1)
        e = 1e-20
        i = 0
        while True:
            i += 1
            x1 = x0 - (self.f(x0) / self.df(x0))
            if abs(x1 - x0) < e: 
                self.x = x1
                break
            if i > 1e+3:
                print("WARNING")
                self.x = x1
                break
            x0 = x1

        ans = self.x

        self.a = (ca * (ans ** 3)) / (ans ** 3 + (ans ** 2) * ka1 + ans * ka1 * ka2 + ka1 * ka2 * ka3)
        self.a1 = (ka1 * self.a) / ans
        self.a2 = (ka1 * ka2 * self.a) / (ans ** 2)
        self.a3 = (ka1 * ka2 * ka3 * self.a) / (ans ** 3)
        self.d = (cd * (ans ** 2)) / (ans ** 2 + ans * kd1 + kd1 * kd2)
        self.d1 = (kd1 * self.d) / ans
        self.d2 = (kd1 * kd2 * self.d) / (ans ** 2)
        self.g = (cg * (ans ** 3)) / (ans ** 3 + (ans ** 2) * kg1 + ans * kg1 * kg2 + kg1 * kg2 * kg3)
        self.g1 = (kg1 * self.g) / ans
        self.g2 = (kg1 * kg2 * self.g) / (ans ** 2)
        self.g3 = (kg1 * kg2 * kg3 * self.g) / (ans ** 3)


    def get_pH(self):
        return -np.log10(self.x)


    def get_cH(self):
        return self.x


    def get_cA(self):
        return self.a


    def get_cA1(self):
        return self.a1


    def get_cA2(self):
        return self.a2


    def get_cA3(self):
        return self.a3


    def get_cD(self):
        return self.d


    def get_cD1(self):
        return self.d1


    def get_cD2(self):
        return self.d2


    def get_cG(self):
        return self.g


    def get_cG1(self):
        return self.g1


    def get_cG2(self):
        return self.g2


    def get_cG3(self):
        return self.g3