# -*- coding: utf-8 -*-
from base64 import b64encode
from hashlib import sha1
from io import BytesIO
from os import urandom

import qrcode


def generate_token():
    # Generate the nonce
    # TODO: Work on the entropy and size of the nonce
    return sha1(urandom(128)).hexdigest()


def make_qrcode_base64(text):
    # Create a temporary placeholder to the image
    with BytesIO() as stream:
        # Generate the qrcode and save to the stream
        qrcode.make(text).save(stream)

        # Get the image bytes, then encode to base64
        image_data = b64encode(stream.getvalue())

    return image_data