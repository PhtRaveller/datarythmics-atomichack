"""Various routines for dealing with the data."""

# Generic imports
from typing import Union
import pathlib

# DS imports
import numpy as np
import pandas as pd


def parse_cfg(f: Union[str, pathlib.Path]) -> pd.DataFrame:
    """Parse ground truth `.cfg` file into Pandas dataframe."""

    f = pathlib.Path(f)

    with open(f, "r") as fl:
        lines = [s.strip() for s in fl.readlines()]

    target = []

    fname = None
    defects = None

    for l in lines:
        tokens = l.split(", ")

        if len(tokens) == 1:

            if fname is not None:
                target.extend(defects)

            fname = l
            defects = []
        else:
            defects.append([fname] + [int(t) for t in tokens])

    if defects:
        target.extend(defects)

    return pd.DataFrame(target, columns=["frame", "x", "y", "label"])


def read_frame(fname: Union[str, pathlib.Path]) -> np.ndarray:
    """Read binary frame data."""

    fname = pathlib.Path(fname)

    with open(fname, "rb") as f:
        data = f.read()

    shape = np.frombuffer(data[:8], dtype=np.uint32)
    img = np.frombuffer(data, dtype=np.uint8, offset=8)

    return img.reshape(shape[::-1])
