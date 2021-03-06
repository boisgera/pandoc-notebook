#!/usr/bin/env python

# Python Standard Library
import copy
import os.path
import pathlib
import tempfile

# Pandoc
import pandoc
from pandoc.types import Div, CodeBlock

# Plumbum
from plumbum.cmd import jupyter


# 🧠 Food for thought
# ------------------------------------------------------------------------------

# 🚧 TODO
# ------------------------------------------------------------------------------
#
#   - Try a mkdocs material + mkdocsstrings setup to see how that flies


# 🪲 BUGS
# ------------------------------------------------------------------------------
#
#   - Jupyter nbconvert couldn't care less about image dpi, right?
#     Mmm not true; at least when figsize and shape are set at figure creation
#     time, the notebook cleared and then converted to HTML with nbconvert
#     --execute we end up with size-dependent images. So what's the deal in
#     our case ?
#     OTOH: width and depth means NOTHING per se, dpi WILL fuck up the apparent
#     size of the image. Getting a prescribed width and depth will need some
#     work.
#

# TODO :
#
#   - function with doc input and doc output ? Would be nice but there is
#     also an extra "media" directory that gets generated (or populated).
#     OK, why not? Mmm is this media file generated in the tmp directory
#     used by pandoc? MMm not obvious.
#
#   - mark code as .code UNLESS some (like "no-exec") flag is found?
#
#   - automate the svg backend stuff (?). Dunno, see later.
#     The code is:
#         import matplotlib_inline.backend_inline
#         matplotlib_inline.backend_inline.set_matplotlib_formats("svg")
#


def flag_code(doc):
    """
    Tag every CodeBlock in the doc with the class "code"
    """
    for elt in pandoc.iter(doc):
        if isinstance(elt, CodeBlock):
            id, classes, kv = elt[0]
            classes.append("code")
            elt[0] = id, classes, kv


def unflag_code(doc):
    """
    Remove the class "code" from every CodeBlock in the doc
    """
    for elt in pandoc.iter(doc):
        if isinstance(elt, CodeBlock):
            id, classes, kv = elt[0]
            classes = list(set(classes) - {"code"})
            elt[0] = id, classes, kv


def exec(doc, media="media"):
    tmp = pathlib.Path(tempfile.mkdtemp())
    pandoc.write(doc, file=(tmp / "notebook.ipynb"), format="ipynb")
    jupyter["nbconvert", "--to", "notebook", "--execute"](tmp / "notebook.ipynb")
    doc_ipynb = pandoc.read(
        file=(tmp / "notebook.nbconvert.ipynb"),
        format="ipynb",
        options=["--extract-media", media],
    )

    codeblocks_location = []
    for elt, path in pandoc.iter(doc, path=True):
        if isinstance(elt, CodeBlock) and "code" in elt[0][1]:
            codeblocks_location.append(path[-1])

    blocks = doc_ipynb[1]
    outputs = []
    for block in blocks:
        assert isinstance(block, Div)
        if "code" in block[0][1]:
            div = block
            outputs.append([])
            for _block in div[1]:
                if isinstance(_block, Div) and "output" in _block[0][1]:
                    outputs[-1].append(_block)

    assert len(codeblocks_location) == len(outputs)

    for (holder, index), output in reversed(list(zip(codeblocks_location, outputs))):
        holder[index + 1 : index + 1] = output


# Main Entry Point
# ------------------------------------------------------------------------------
doc = pandoc.read(file="notebook.md")
flag_code(doc)
exec(doc)
unflag_code(doc)
pandoc.write(doc, file="notebook-out.md", options=["--standalone"])


# # TODO: deal with execute_results, stream and display_data (should be good enough)
