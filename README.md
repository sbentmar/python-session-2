# Tempgraph

*Tempgraph* will let you add temperatures and draw graphs!

## Usage

To use tempgraph, first install all libraries:

```
python3 -m pip install requirements.txt
```

Then, add some temperatures! To add the a temperature for the current timestamp, use `-t`:
```
python3 tempgraph.py -t 12
```

To add historical temperatures, use `-v`:
```
python3 tempgraph.py -v1000=12
```

Then, generate a graph:
```
python3 tempgraph.py -g
```

You can also combine all of these commands on the same line:

```
python3 tempgraph -t 15 -g
```