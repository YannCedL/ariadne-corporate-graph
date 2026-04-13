# ariadne-corporate-graph

corporate ownership graph engine mapping parent companies and subsidiaries.

## install

```bash
pip install -e .
```

## run api

```bash
uvicorn ariadne_corporate_graph.api:app --port 8002
```

## usage

```python
from ariadne_corporate_graph import build_company_graph

result = build_company_graph("383474814")
print(result.result)
```
