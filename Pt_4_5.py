graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'
way = []


def find_all_paths(trackmap, start_point, end_point, path):
    path = path + [start_point]
    paths = []
    if start_point == end_point:
        return [path]
    if not trackmap.get(start_point):
        return []
    for connected in trackmap[start_point]:
        new_paths = find_all_paths(trackmap, connected, end_point, path)
        paths.extend(new_paths)
    return paths


tracks = find_all_paths(graph, start, end, way)
print("Все возможные пути из A в F: ", *tracks)
