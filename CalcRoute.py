# Paste your optimal route after the equal sign (=) here
optimal_route = ('Lake Texoma', 'Lavon Lake, TX', 'Lake Ray Hubbard, TX', 'Lake Tawakoni, TX', 'Lake Fork, TX', 'Jim Chapman Lake, TX', 'Lake Bob Sandlin, TX', "Lake O' the Pines, Texas", 'Wright Patman Lake, TX', 'Caddo Lake', 'Toledo Bend Reservoir', 'Sam Rayburn Reservoir, Angelina National Forest, TX', 'Lake Livingston, TX', 'Conroe Lake, TX', 'Lake Limestone, TX', 'Richland Chambers Reservoir, TX', 'Lake Palestine, TX', 'Cedar Creek Reservoir, TX', 'Lake Whitney, TX', 'Belton Lake, Bell County, TX', 'Buchanan Lake, TX', 'Lake Travis, TX', 'Canyon Lake, TX', 'Falcon Reservoir', 'Amistad National Recreation Area, Del Rio, TX', 'Possum Kingdom Lake, TX', 'Lewisville Lake, TX', 'Lake Ray Roberts, TX')


optimal_route = list(optimal_route)
optimal_route += [optimal_route[0]]
subset = 0
    
while subset < len(optimal_route):
    
    waypoint_subset = optimal_route[subset:subset + 10]
    output = "calcRoute(\"%s\", \"%s\", [" % (waypoint_subset[0], waypoint_subset[-1])
    for waypoint in waypoint_subset[1:-1]:
        output += "\"%s\", " % (waypoint)
        
    if len(waypoint_subset[1:-1]) > 0:
        output = output[:-2]
        
    output += "]);"
    print(output)
    print("")
    subset += 9