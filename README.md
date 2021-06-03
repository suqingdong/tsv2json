# Convert TSV file to JSON

## Installation
```bash
pip install tsv2json
```

## Examples
```bash
tsv2json examples/demo.tsv

tsv2json examples/demo.tsv -i 2

tsv2json examples/demo.tsv -i 2 -o out.json

tsv2json examples/demo.tsv -i 2 -l 3

tsv2json examples/demo.tsv -c 'name' -H 0

tsv2json examples/demo.csv -s , 
```

## Use in Python
```python
from tsv2json.core import TSV

tsv = TSV('examples/demo.tsv')

print(tsv.data)

print(tsv.to_json(indent=2))

tsv.to_json('out.json')
```
