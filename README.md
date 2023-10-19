# hello plumber

This package provides an API implemented in `R` with `plumber` which then can be consumed with `python`.

>The R package structure in this case might be a little over-kill but is convenient when the API gets more complexe and has R dependencies. Further, it is easy to develop an R package and then simply wrap its functionality in `inst/api/api.R` to provide the entry point for `plumber` as well as provide a wrapper for the `plumber` (see the `run()` function).

## Setup

```
pip install git+https://github.com/dheimgartner/hello_plumber
```

The package provides the console script `install_rapi` which installes the R API (the R package) first. Similarly, there is a `uninstall_rapi` helper.

## Usage

After having called the `install_rapi` setup command, you can consume the API like so:

```python
url = "http://localhost:8000"
with RApiConsumer(port=8000):
    try:
        response = requests.get(f"{url}/echo?msg=hello")
        
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
```

The API server can be started from the cli `start_rapi`: Navigate to the `http://127.0.0.1:8000/__docs__/` to check out the documentation and test it in a GUI environment.