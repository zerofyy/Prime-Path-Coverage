<h1 align="center">
  Zerofy's Prime Path Coverage Tool
</h1>


## 📄 Overview
This is a freely available tool for computing prime path coverage in directed graphs used in path-based software testing.

## ⚙ Usage
The tool is available as a GitHub Page [here](https://zerofyy.github.io/Prime-Path-Coverage/) with instructions on the site.

Alternatively, the algorithm can be found in [this script](prime_path_coverage.py) which can be used like so:
```python
# ...code from the script...

graph = {
    1 : [2],    # 1 -> 2
    2 : [3, 4], # 2 -> 3, 2 -> 4
    3 : [2],    # 3 -> 2
    4 : []      # 4 -> /  this node has no neighbors
}

result = compute_prime_paths(graph)
paths = result['paths']

# Print paths formatted into a Num,Len,Path table.
print(format_output(paths))

# Print raw paths, as lists of nodes.
for path in paths:
    print(path)
```

## TODO
- Allow inputting graphs on the site in `node neighbor1 neighbor2 ...` format.
