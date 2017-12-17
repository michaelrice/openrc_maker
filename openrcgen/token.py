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

import pf9_saml_auth
from keystoneauth1 import session


def okta(*args, **kwargs):
    auth = pf9_saml_auth.V3Pf9SamlOkta(
        auth_url=kwargs.get("auth_url"),
        username=kwargs.get("username"),
        password=kwargs.get("password"),
        protocol='saml2',
        identity_provider=kwargs.get("id_provider"),
        project_name=kwargs.get("project_name"),
        project_domain_name=kwargs.get("project_domain_id"),
    )

    # Create Keystone authentication session
    sess = session.Session(auth=auth)
    return sess.get_token()


def adfs(*args, **kwargs):
    raise NotImplementedError("Currently only okta is supported!")
    # auth = pf9_saml_auth.V3Pf9ADFSPassword(
    #    auth_url=kwargs.get("auth_url"),
    #    identity_provider=kwargs.get("id_provider"),
    #    identity_provider_url=None,
    #    service_provider_endpoint=None,
    #    username=kwargs.get("username"),
    #    password=kwargs.get("password")
    # )


def onelongin(*args, **kwargs):
    raise NotImplementedError("Currently only okta is supported!")
    # auth = pf9_saml_auth.V3Pf9SamlOnelogin(
    #    auth_url=kwargs.get("auth_url"),
    #    identity_provider=kwargs.get("id_provider")
    # )
