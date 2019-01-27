import json

dct1 = {'reverse0': [(609, 4.585), (615, 4.285), (966, 3.585)]}
dct2 = {'reverse1': [(619, 3.185), (625, 4.655), (936, 1.585)]}
print(dict(dct1, **dct2))