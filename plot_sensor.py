import pandas as pd
import matplotlib.pyplot as plt

# Read CSV (adjust columns to match yours)
df = pd.read_csv('ptat_output.csv', sep=r'\s+', comment='*', header=None)
df.columns = ['Index', 'Temp_C', 'V_PTAT', 'V_CTAT', 'V_OUT', 'Unused']
df = df.drop(columns=['Index', 'Unused'])

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
ptat_line, = ax.plot(df['Temp_C'], df['V_PTAT'], label='PTAT Voltage', linewidth=2)
ctat_line, = ax.plot(df['Temp_C'], df['V_CTAT'], label='CTAT Voltage', linewidth=2)
vout_line, = ax.plot(df['Temp_C'], df['V_OUT'], label='V_OUT (Bandgap)', linewidth=2)

ax.set_xlabel('Temperature (°C)')
ax.set_ylabel('Voltage (V)')
ax.set_title('PTAT + CTAT Temperature Sensor Output')
ax.grid(True)
ax.legend()

# Add interactive hover
annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

lines = [ptat_line, ctat_line, vout_line]
labels = ['PTAT', 'CTAT', 'V_OUT']
data_keys = ['V_PTAT', 'V_CTAT', 'V_OUT']

def update_annot(line, ind, label):
    x, y = line.get_data()
    annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
    text = f"{label}\nTemp: {x[ind['ind'][0]]:.1f}°C\nVolt: {y[ind['ind'][0]]:.4f} V"
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor("lightyellow")
    annot.get_bbox_patch().set_alpha(0.9)

def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        for i, line in enumerate(lines):
            cont, ind = line.contains(event)
            if cont:
                update_annot(line, ind, labels[i])
                annot.set_visible(True)
                fig.canvas.draw_idle()
                return
    if vis:
        annot.set_visible(False)
        fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.tight_layout()
plt.show()