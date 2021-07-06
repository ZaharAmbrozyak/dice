from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Створити D.
die_1 = Die()
die_2 = Die()

# Зробити декілька кидків та зберегти результати у список.
results = []

rolls = range(1_000_000 + 1)

[results.append(die_1.roll() + die_2.roll()) for roll_num in rolls]


# Проаналізувати результати.
frequencies = []

max_result = die_1.num_sides + die_2.num_sides

[frequencies.append(results.count(value)) for value in range(1, max_result+1)]

# Візуалізувати результати.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of rolling a {die_1.get_name()} and a {die_2.get_name()} {rolls[-1]} times',
     xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename=f'{die_1.get_name()}_{die_2.get_name()}_{rolls[-1]}_times.html')
