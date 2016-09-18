# Rinobot-plugin

## Installation

`pip install rinobot_plugin`

## Example

```python
import rinobot_plugin as bot
import numpy as np

def main():
  # lets get our parameters and data
  filepath = bot.filepath()
  data = bot.loadfile(filepath)

  # now comes the custom plugin logic
  shift = bot.get_arg('shift', type=float)
  index = bot.index_from_args(data)
  data[index] = data[index] + shift
  outname = bot.no_extension() + '-shift-%s.txt' % shift

  # then we set up the output
  outpath = bot.output_filepath(outname)
  np.savetxt(outpath, data, fmt="%d")

if __name__ == "__main__":
  main()
```

## Documentation

### `loadfile(fpath, skiprows=0, **args)`

Loads a file with numpy.loadtxt and will recursively skips headers.

Parameters:

- `fpath` : string, Path to file to load
- `skiprows` : int, Number of rows to skip
- `**args` : Extra arguments for numpy.loadtxt

Returns

- `data` : array or None, Returns and array is possible and None if no data was found

### `reset_parser()`

Only used for testing to reset the parser to call it again.

### `add_argument('--argument', type=str, [is_required=True])`

Adds an argument that rinobot will parse from the command line.

### `get_args()`

Returns the arguments parsed from the command line, `filepath` is available
by default, along with any other specified arguments.

### `get_arg(arg, type=None, *args, **kwargs)`

Example usage: `param = bot.get_arg('param', type=float)` Fills the value param
if '--param=3.4' is specified on the command line, and its bound to a  float. It
can also take an argument `required=True` if you want an error to be raised  if
the parameter doesnt exist.

### `is_plugin()`

Returns True if the code is running as a rinobot plugin.

### `filepath()`

Gets the filepath of the input file

### `filename()`

Gets the input filename

### `no_extension()`

Returns the input filename with no extension

### `output_filepath(filename)`

If you pass a new filenae for the ouput; this function will resolve the path for it
relative to the input filename.

**this is the required way to save a file if the code is being used with rinobot**.
If you save the output file in another way, then Rinobot cannot track it and plugin
pipelines will break down.

### `index_from_args(data)`

Returns the index of the data passed in by the user.

So if the program is called like

`python plugin.py /filepath.txt --cols=1:4 --rows=3`

Then after loading the data from the filepath calling

```
index = index_from_args(data)
```

Will give the indices of the data to be operated on.

Examples:
- `--cols=2` operates on column 2
- `--cols=1:` operates on columns from 1 on, so skipping the zeroth column.
- `--cols=1:3` operates on columns from 1 to 3
- `--cols=1:10:2` operates on columns from 1 to 10 skipping every second column
- `--cols=:10` operates on columns up to column 10
- `--cols=1::2` operates on columns from 1 on, skipping every second column

Same goes for rows:
- `--row=2` operates on row 2
- `--rows=1:` operates on rows from 1 on, so skipping the zeroth row.
- `--rows=1:3` operates on rows from 1 to 3
- `--rows=1:10:2` operates on rows from 1 to 10 skipping every second row
- `--rows=:10` operates on rows up to row 10
- `--rows=1::2` operates on rows from 1 on, skipping every second row


### `build_index(data, cols_string, rows_string)`

Same as `index_from_args` but the cols_string and rows_string can be specified
and not read from the program arguments.

## Development

Clone the repo and type:

`python setup.py develop`

This will install the package into a directory for development.

## Testing

To run the tests in either interpreter just use

```python
python setup.py test
```

or, if python 3 is named `python3`

python3 setup.py test

## publishing to pypi
