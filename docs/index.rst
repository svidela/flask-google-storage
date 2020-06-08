Welcome to Flask-GoogleStorage
==============================

**Flask-GoogleStorage** is a Flask extension for adding storage capabilities using Google Cloud Storage.

Install
=======

Flask-GoogleStorage requires Python >= 3.6.

.. code-block:: bash

    $ pip install flask-googlestorage

   
Usage
=====

In order to authenticate with Google Cloud Storage, set the ``GOOGLE_APPLICATION_CREDENTIALS``
environment variable to the full path to your service account private key file (see `google-auth`_
documentation for more details). If the authentication fails, **Flask-GoogleStorage** will storage
and serve uploaded files locally and relative to the configuration variable
``GOOGLE_STORAGE_LOCAL_DEST``. Note that this configuration variable is required even in the case of
successfull authentication as **Flask-GoogleStorage** will use such destination as a temporary
storage.

First create your app as usual:

.. code-block:: python

    from datetime import timedelta

    from flask import Flask
    from flask_googlestorage import GoogleStorage, Bucket
    
    files = Bucket("files")
    storage = GoogleStorage(files)

    def create_app():
        app = Flask(__name__)
        app.config.update(
            GOOGLE_STORAGE_LOCAL_DEST = app.instance_path,
            GOOGLE_STORAGE_SIGNATURE = {"expiration": timedelta(minutes=5)},
            GOOGLE_STORAGE_FILES_BUCKET = "files-bucket-id"
        )
        storage.init_app(app)

        return app

Then you can save :py:class:`werkzeug.datastructures.FileStorage` objects using:

.. code-block:: python

    filename = files.save(file_storage)  # add public=True to make it publicly available

The URL for a given filename can be obtained using:

.. code-block:: python

    files.url(filename)  # returns the public url
    files.signed_url(filename)  # returns a signed url valid for 5 minutes


Configuration
=============

The following configuration values are available. **Flask-GoogleStorage** loads these values from
your main Flask config which can be populated in various ways.

Configuration Keys
------------------

A list of configuration keys currently understood by the extension:

.. tabularcolumns:: |p{6.5cm}|p{8.5cm}|

====================================== =========================================
``GOOGLE_STORAGE_LOCAL_DEST``          Local path for either temporary or local storage.
``GOOGLE_STORAGE_SIGNATURE``           A dictionary specifying the keyword arguments
                                       for building the signed url.
``GOOGLE_STORAGE_TENACITY``            A dictionary specifying the keyword arguments
                                       for the :py:func:`tenacity.retry` decorator.
``GOOGLE_STORAGE_RESOLVE_CONFLICTS``   If set to `True`, **Flask-GoogleStorage** will
                                       resolve name conflicts. Otherwise, existing files will
                                       be overwritten.
``GOOGLE_STORAGE_DELETE_LOCAL``        If set to `True`, uploaded files are deleted after
                                       uploading to Google Cloud Storage (successfully or not).
``GOOGLE_STORAGE_X_SIGNATURE``         Overwrite ``GOOGLE_STORAGE_SIGNATURE`` for bucket ``X``.
``GOOGLE_STORAGE_X_TENACITY``          Overwrite ``GOOGLE_STORAGE_TENACITY`` for bucket ``X``.
``GOOGLE_STORAGE_X_RESOLVE_CONFLICTS`` Overwrite ``GOOGLE_STORAGE_RESOLVE_CONFLICTS`` for bucket ``X``.
``GOOGLE_STORAGE_X_DELETE_LOCAL``      Overwrite ``GOOGLE_STORAGE_DELETE_LOCAL`` for bucket ``X``.
``GOOGLE_STORAGE_X_BUCKET``            Bucket id for bucket ``X``. If the bucket is not found, files will be
                                       saved and served locally.
====================================== =========================================

To restrict uploaded files content length you should use the `Flask` configuration variable
``MAX_CONTENT_LENGTH``. See the `Configuration Handling`_ section in `Flask` documentation for more details.


API Reference
=============

.. toctree::
    :maxdepth: 2

    api_reference

Project Info
============

.. toctree::
    :maxdepth: 1

    changelog
    license
    authors

.. _Configuration Handling:
    https://flask.palletsprojects.com/en/1.1.x/config/#configuration-handling

.. _google-auth: 
    https://google-auth.readthedocs.io