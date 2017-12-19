openrc_maker is a simple cli tool to help generate an openrc file for use with
saml2 based providers so that you can use a v3token openrc file


Getting Started
===============
To get started you will need to install the project using pip

`pip install`

Usage
=====
.. code:: bash

    os_openrcgen --help

    Usage: os_openrcgen [OPTIONS]

    Options:
      --auth-url TEXT                 The URL of your keystone. For example:
                                      https://example.com:5000/v3  [required]
      --username TEXT                 The username to auth with.  [required]
      --password TEXT
      --protocol TEXT                 Auth protocol. Defaults to saml2
      --id-provider TEXT              The name of your identity provider. This is
                                      the name you gave your IdP in OpenStack.
                                      See: `openstack identity provider list` for
                                      a list of possibilities.  [required]
      --project-name TEXT             The name of the project your user will use
                                      once logged in.  [required]
      --project-domain-name TEXT      The name of the domain.  [required]
      --project-domain-id TEXT        The project domain id.  [required]
      --provider-type                 [okta|adfs|onelogin]
                                      The type of provider to use. Defaults to
                                      okta.
      --out-file FILENAME             Name of the file for your new openrc
      --in-file FILENAME              Name of the template file to use.
      --help                          Show this message and exit.


.. code::  bash

    os_openrcgen --username Os.admin@mysite.com --out-file example.rc \
    --in-file ~/programs/python/openrc_maker/templates/default-posix.txt \
    --auth-url https://aio.mysite.com:5000/v3 --id-provider okta \
    --project-name fedproject --project-domain-id default \
    --project-domain-name Default

