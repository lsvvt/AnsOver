import ansover as ao ## Библиотека для равновесия (ansolver.py в папке со скриптом)
import sys
import plotly.graph_objects as go ## Библиотека для графиков

ka1 = 10 ** (-2.7) # Константа кислотности 1
ka2 = 10 ** (-7.4) # Константа кислотности 2

eq = ao.Equ(ka1 = ka1, ka2 = ka2) # Создание объекта равновесие с указанием нужных констант (поддерживается 3х основная кислота + 3х основное основание + 2х основная кислота + сильное основание + сильная кислота)

ph = []
for i in range(0, 300): # Цикл добавления NaOH
    eq.calc(ca = (0.1 * 0.1) / (0.1 + i / 1000), cb = ((i / 1000) * 0.1) / (0.1 + i / 1000))
    ph.append(eq.get_pH())

print(ph)

## Построение графика

fig = go.Figure()
fig.add_trace(go.Scatter(x=list(range(0, 300)), y=ph,
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