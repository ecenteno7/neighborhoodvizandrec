from shapely.geometry import Polygon, MultiPolygon

def get_center_and_radius(poly):
    if isinstance(poly, Polygon):
        center = poly.centroid
        radius = poly.distance(center)
        return center, radius
    elif isinstance(poly, MultiPolygon):
        centers = []
        radii = []
        for p in poly:
            c, r = get_center_and_radius(p)
            centers.append(c)
            radii.append(r)
        weights = [p.area for p in poly]
        total_weight = sum(weights)
        center = weighted_centroid(centers, weights)
        radius = weighted_radius(centers, radii, weights)
        return center, radius
    else:
        raise TypeError("Expected a Polygon or MultiPolygon, but got %s" % type(poly))

def weighted_centroid(points, weights):
    x_total = sum([p.x * w for p, w in zip(points, weights)])
    y_total = sum([p.y * w for p, w in zip(points, weights)])
    total_weight = sum(weights)
    return Point(x_total/total_weight, y_total/total_weight)

def weighted_radius(points, radii, weights):
    center = weighted_centroid(points, weights)
    distances = [center.distance(p) + r for p, r in zip(points, radii)]
    max_distance = max(distances)
    return max_distance
