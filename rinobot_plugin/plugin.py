import os
import warnings
import argparse
import numpy as np


def loadfile(fpath, skiprows=0, **args):
    """
        load(fpath, skiprows=0, **args)

        Loads a file with numpy.loadtxt and will recursively skips headers.

        Parameters
        ----------
        fpath : string
            Path to file to load
        skiprows : int
            Number of rows to skip
        **args
            Extra arguments for numpy.loadtxt

        Returns
        -------
        data : array or None
            Returns and array is possible
            and None if no data was found
    """
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            return np.loadtxt(fpath, skiprows=skiprows, **args)
        except ValueError:
            return load(fpath, skiprows+1)
        except StopIteration:
            return None


parser = argparse.ArgumentParser()
parser.add_argument('filepath', type=str)
parser.add_argument('--prefix', type=str)


def reset_parser():
    global parser
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str)
    parser.add_argument('--prefix', type=str)


class Args(object):
    prefix=None
    filepath=None


def get_args():
    args, unknown = parser.parse_known_args(namespace=Args())
    return args


def get_arg(arg, type=None, *args, **kwargs):
    if type:
        add_argument('--%s' % arg, type=type, *args, **kwargs)
    args, unknown = parser.parse_known_args(namespace=Args())
    return getattr(args, arg)


def add_argument(*args, **kwargs):
    parser.add_argument(*args, **kwargs)


def is_plugin():
    args = get_args()
    if args.prefix:
        return True
    else:
        return False


def filepath():
    args = get_args()
    return args.filepath


def filename():
    args = get_args()
    return os.path.basename(args.filepath)


def no_extension():
    return os.path.splitext(filename())[0]


def output_filepath(fname):
    args = get_args()

    prefix = ''
    if args.prefix:
        prefix = args.prefix

    return os.path.join(
        os.path.dirname(filepath()),
        prefix + fname
    )
