# add temperature with specified timestamp
python3 tempgraph.py -v 1643365409=32

# add multiple temperatures with specified timestamp
python3 tempgraph.py -v 1643365400=32 -v 1643365410=33

# add temperature for current time
python3 tempgraph.py -t 36

# render graph
python3 tempgraph.py -g

# list values
python3 tempgraph.py -l

# open graph in browser
python3 tempgraph.py -w
