def parse_graph(input_text: str) -> dict[str, list[str]]:
    """
    Create an internal representation of a graph from the given text input.

    Supported edge formats:
        - `node1 node2`
        - `node1 - node2`
        - `node1 -> node2`

    Lines starting with `#` are ignored.

    ------

    Arguments:
        input_text: String containing graph edges in different lines.

    ------

    Returns:
        A directed graph in dictionary form where each key is a node and each value is a list of neighbors.
    """
    graph = {}

    for idx, line in enumerate(input_text.strip().split('\n'), start = 1):
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        nodes = line.split(' ')
        if not nodes or len(nodes) != 2:
            raise Exception(f'Invalid edge format at line {idx}: {line}')

        node1, node2 = nodes

        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []

        graph[node1].append(node2)

    if not graph:
        raise Exception(f'Invalid graph input.')

    return graph


def compute_prime_paths(graph: dict[str, list[str]]) -> dict[str, str | list[list[str]]]:
    """
    Compute prime paths for the given directed graph.

    ------

    Arguments:
        graph: A dictionary representing a directed graph
               where each key is a node and each value is a list of neighbors.

    ------

    Returns:
        A dictionary containing the prime paths and debug information.
    """

    debug, counter = '', 0
    paths = [[node] for node in graph]

    while True:
        counter += 1
        debug += f'Iteration {counter}:\n'
        made_changes = False

        for idx in range(len(paths)):
            path = paths[idx]
            if not path:
                continue

            pstr = path.copy()
            node = path[-1]

            has_one_neighbor = len(graph[node]) == 1
            remove_path = False
            for neighbor in graph[node]:
                if max([path.count(n) for n in set(path)]) > 1:
                    debug += f'[Path Ended - A] | {pstr} --> {path}\n'
                    continue

                if neighbor in path and neighbor != path[0]:
                    debug += f'[Path Ended - B] | {pstr} --> {path}\n'
                    continue

                if has_one_neighbor:
                    path.append(neighbor)
                    debug += f'[Path Updated  ] | {pstr} --> {path}\n'

                else:
                    paths.append(path + [neighbor])
                    debug += f'[Path Split    ] | {pstr} --> {paths[-1]}\n'
                    remove_path = True

                made_changes = True

            if remove_path:
                path.clear()
                debug += f'[Path Removed  ] | {pstr} --> {path}\n'

        debug += '\n'
        if not made_changes:
            debug += 'Done.\n'
            debug += '-' * 100 + '\n\n'
            break

    debug += 'Removing sub-paths...\n'
    for i in range(len(paths)):
        if not paths[i]:
            continue

        path = str(paths[i])[1 : -1]

        for j in range(len(paths)):
            if i == j:
                continue

            if path in str(paths[j]):
                debug += f'[Found Sub-path] | {paths[i]} --> {paths[j]}\n'
                paths[i].clear()
                break
    debug += 'Done.'

    paths = [path for path in paths if path]
    paths.sort(key = lambda x: (len(x), x))
    return {'paths' : paths, 'debug' : debug}


def format_output(paths: list[list[str]]) -> str:
    """
    Format the given prime paths for display on the site.

    ------

    Arguments:
         paths: A list of prime paths.

    ------

    Returns:
        A formatted string of the same prime paths.
    """

    if not paths:
        return 'No prime paths found.'

    output = f'Found {len(paths)} prime path(s):\n' \
             f'Num\tLen\tPath\n'
    for idx, path in enumerate(paths, start = 1):
        pstr = ' → '.join(map(str, path))
        output += f'{idx:3}\t{len(path):3}\t{pstr}\n'

    return output
