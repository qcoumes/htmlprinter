#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# htmlprint.py
#

from html.entities import html5
import traceback



def encode(string):
    """Return the encoded string with corresponding hmtl5 entities."""
    
    string = string.replace('&', '&amp;')
    string = string.replace(';', '&semi;')
    for k, v in html5.items():
        if k[-1] == ';' and k[0].islower() and not 'amp' in k and  not 'semi' in k:
            string = string.replace(v, '&'+k)
    return string


def tag(tag, string, *args, **kwargs):
    """Return the surrounded string with tag, adding *args and **kwargs as tag's attributes.
    For the attribute 'class', use at least one uppercase."""
    
    string = encode(string)
    attributes = " ".join(
        [str(k).lower() + '="' + str(v) + '"' for k, v in kwargs.items()]
        + list(args)
    )
    return (
        "<" + tag
        + ("" if not attributes else " " + attributes)
        + ">" + string + '</' + tag + '>'
    )


def nltobr(string):
    """Replace and return string with newlines replaced by <br/>."""
    
    return string.replace("\r\n", "<br/>").replace("\r", "<br/>").replace("\n", "<br/>")


def code(string):
    """Return the surrounded string with a wrapping <pre> and <code> tag."""
    
    return (
        '<pre style="'
        + "white-space: pre-wrap;"
        + "white-space: -moz-pre-wrap;"
        + "white-space: -pre-wrap;"
        + "white-space: -o-pre-wrap;"
        + 'word-wrap: break-word;'
        + '"><code>' + string + "</code></pre>"
    )


def html_exc(limit=None, chain=True):
    """Return an html formatted string of the last exception."""
    
    return code(traceback.format_exc())
