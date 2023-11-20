# Desc: Layout configuration for the line plot

layout_parameters = {
    "xaxis": {
        "showline": True,
        "showgrid": False,
        "zeroline": False,
        "showticklabels": True,
        "linecolor": 'rgb(204, 204, 204)',
        "linewidth": 2,
        "ticks": 'outside',
        "tickfont": {
            "family": 'Arial',
            "size": 12,
            "color": 'rgb(82, 82, 82)',
        },
    },
    "yaxis": {
        "showline": True,
        "showgrid": False,
        "showticklabels": True,
        "zeroline": False,
        "linecolor": 'rgb(204, 204, 204)',
    },
}

update_parameters = {
    "xaxis": {
        "title_text": "Measurement",
        "title_font": {"size": 15},
        "tickfont": {"size": 10},
        "dtick": 2.5,
        "tickformat": ".2f",
    },
    "yaxis": {
        "title_text": "Time (min)",
        "title_font": {"size": 15},
        "tickfont": {"size": 10},
        "dtick": 25000,
    },
}