# AnsOver
Chemistry Equilibrium

* mytask.py - sample with plotly

# Guide
```
import ansover as ao 
eq = ao.Equ(ka1 = ..., ka2 = ..., kd1 = ...) - Create object
eq.calc(ca = ..., cb = ...) - Set concentrations and calculate
eq.get_pH() - Calc pH
eq.get_cXY() - Cacl concentration of XY, where X - substance, Y - abs(charge) (for examphe get_cG2() returns [G2+])
```

* Params for H3A (for H2A set ka3 = 0)
```
ca - common concentration
ka1 = [A-][H+]/[A]
ka2 = [A2-][H+]/[A-]
ka3 = [A3-][H+]/[A2-]
```

* Params for H2D (for HD set kd2 = 0)
```
cd - common concentration
kd1 = [D-][H+]/[D]
kd2 = [D2-][H+]/[D-]
```

* Params for G(OH)3 (for G(OH)2 set kg1 = 1e+100)
```
cg - common concentration
kg1 = [G2+][H+]/[G3+]
kg2 = [G+][H+]/[G2+]
kg3 = [G][H+]/[G+]
```

* cb - common concentration of strong base

* cz - common concentration of strong acid
