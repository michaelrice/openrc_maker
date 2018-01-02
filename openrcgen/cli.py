# Copyright 2017 Michael Rice
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import click

import token
import openrcgen


@click.command()
@click.option(
    '--auth-url',
    help='The URL of your keystone. '
         'For example: https://example.com:5000/v3',
    required=True
)
@click.option(
    '--username',
    help="The username to auth with.",
    required=True
)
@click.password_option()
@click.option(
    '--protocol',
    default="saml2",
    help="Auth protocol. Defaults to saml2"
)
@click.option(
    '--id-provider',
    help="The name of your identity provider. This is the name "
         "you gave your IdP in OpenStack. See: "
         "`openstack identity provider list` for a list of "
         "possibilities.",
    required=True
)
@click.option(
    "--project-name",
    help="The name of the project your user "
         "will use once logged in.",
    required=True
)
@click.option(
    "--project-domain-name",
    help="The name of the domain.",
    required=True
)
@click.option(
    "--project-domain-id",
    help="The project domain id.",
    required=True
)
@click.option(
    "--provider-type",
    default="okta",
    help="The type of provider to use. Defaults to okta.",
    type=click.Choice(['okta', 'adfs', 'onelogin'])
)
@click.option(
    '--out-file',
    type=click.File('wb'),
    help="Name of the file for your new openrc"
)
@click.option(
    "--in-file",
    type=click.File('rb'),
    help="Name of the template file to use."
)
def make_openrc(**kwargs):
    ks_token = getattr(token, kwargs.get("provider_type"))(**kwargs)
    openrcgen.make_file(token=ks_token, **kwargs)
    click.echo("Complete. Next source the file and use the OpenStack clients.")
