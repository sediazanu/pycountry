from geopy.distance import vincenty

newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(round(vincenty(newport_ri, cleveland_oh).miles), 'miles')
