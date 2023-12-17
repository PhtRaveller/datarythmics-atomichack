"""Plotting routines for AtomicHack."""

# DS imports
import numpy as np
import pandas as pd

# Plotting imports
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

PATCH_S = 80


def plot_frame(frame: np.ndarray,
               frame_metadata: pd.Series,
               frame_defects: pd.Series,
               figsize: tuple = (6,6),
               dpi: int = 150,
               fontsize: int = 10):
    """Plot single frame with defects outlined."""

    fig = plt.figure(figsize=figsize, dpi=dpi)

    # Frame
    plt.imshow(frame, cmap=plt.cm.gray, vmin=0, vmax=255)

    # Defects
    for _, defect in frame_defects.iterrows():
        plt.plot([defect.x], [defect.y], "x",
                 color=f"#{defect.colorcode.lower()}",
                 markersize=12)
        defect_outline = Rectangle((defect.x - PATCH_S, defect.y - PATCH_S),
                                   2 * PATCH_S, 2 * PATCH_S,
                                   linewidth=0.5,
                                   linestyle=("-" if defect.source=="train" else "--"),
                                   edgecolor=f"#{defect.colorcode.lower()}",
                                   facecolor='none')
        plt.gca().add_patch(defect_outline)
        plt.text(defect.x - PATCH_S, defect.y - PATCH_S,
                 defect.classname,
                 verticalalignment="top",
                 horizontalalignment="left",
                 fontsize=5,
                 color="white" if defect.colorcode!="FFFFFFFF" else "black",
                 bbox={
                     "pad": 0,
                     "facecolor": f"#{defect.colorcode.lower()}",
                     "edgecolor": f"#{defect.colorcode.lower()}",
                     
                 })

    # Clean-up
    plt.xlim(0, 960)
    plt.ylim(600, 0)
    plt.xticks([])
    plt.yticks([])
    plt.grid(None)

    # Title
    plt.title((f"Frame: {frame_metadata.frame}, "
               f"defects: {len(frame_defects[frame_defects.label!=0])}"),
              fontsize=fontsize)
    plt.tight_layout()
    plt.show()
    return fig
