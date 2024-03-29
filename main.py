import requests

canvas = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 2, 2, 2, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
]

url = "http://pixel.samuraism.com/api/highlight"

for i, x in enumerate(canvas):
    for j, y in enumerate(x):
        if y == 0:
            continue
        match y:
            case 1:
                requests.get(url, params={'x': j, 'y': i, 'color': 'black'})
            case 2:
                requests.get(url, params={'x': j, 'y': i, 'color': 'red'})
