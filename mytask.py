import ansover as ao ## Библиотека для равновесия (ansolver.py в папке со скриптом)
import sys
import plotly.graph_objects as go ## Библиотека для графиков
import numpy as np

def d(mass):
    a = 1
    ans = []
    for i in mass:
        if a == 0:
            ans.append(i - tmp)
        a = 0
        tmp = i

    return ans

acc = 0.1 # точность расчётов (шаг добавления NaOH)

ka1 = 10 ** (-2.7) # Константа кислотности 1
ka2 = 10 ** (-7.4) # Константа кислотности 2

eq = ao.Equ(ka1 = ka1, ka2 = ka2) # Создание объекта равновесие с указанием нужных констант (поддерживается 3х основная кислота + 3х основное основание + 2х основная кислота + сильное основание + сильная кислота)

ph = []
for i in np.arange(0, 300, acc): # Цикл добавления NaOH
    eq.calc(ca = (0.1 * 0.1) / (0.1 + i / 1000), cb = ((i / 1000) * 0.1) / (0.1 + i / 1000))

    ph.append(eq.get_pH())

print(ph)

# ph = d(ph) # Для первой производной
# ph = d(ph) # Для второй производной

## Построение графика

fig = go.Figure()
fig.add_trace(go.Scatter(x=list(np.arange((300/acc - len(ph))*acc, 300, acc)), y=ph,
                    mode='lines',
                    name='lines'))

fig.update_layout(
    font = dict(
        family = "Courier New, monospace",
        size = 20,
        color = "#7f7f7f"
    ),
    boxmode = "group",
    title=""
)

fig.update_xaxes(title_text="V NaOH")
fig.update_yaxes(title_text="pH")
fig.update_layout(title="")

fig.update_layout(
    xaxis=dict(
        showgrid=True,
        gridcolor='rgb(215, 215, 215)',
        linecolor='rgb(215, 215, 215)',
        linewidth=1.5,
        gridwidth=1.5,
        zerolinecolor='rgb(215, 215, 215)',
        # ticks='outside',
        # tickfont=dict(
        #     family = "Courier New, monospace",
        #     size = 20,
        #     color = "#7f7f7f"
        # ),
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='rgb(215, 215, 215)',
        linecolor='rgb(215, 215, 215)',
        linewidth=1.5,
        gridwidth=1.5,
        zerolinecolor='rgb(215, 215, 215)',
        # showline=True,
        # showticklabels=False,
    ),
    plot_bgcolor='white',
    boxmode = "group",
)

fig.show()