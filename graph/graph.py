import plotly.graph_objects as go

def render_graph(values, options = {}):
    filename = options['output_filename']
    print(values)
    timestamps = sorted(values['temperatures'].keys())
    temperatures = [values['temperatures'][t] for t in timestamps]
    print(timestamps)
    print(temperatures)

    fig = go.Figure(
        data = go.Scatter(
            x = timestamps,
            y = temperatures
        )
    )

    fig.write_html(filename)
