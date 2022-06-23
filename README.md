## About the connector
host.io helps to get comprehensive domain name data, uncover new domains and the relationships between them, get DNS details, scraped website content, outbound links, backlinks, and other hosting details for any domain. This connector facilitates automated operation related to various domains.
<p>This document provides information about the host.io Connector, which facilitates automated interactions, with a host.io server using FortiSOAR&trade; playbooks. Add the host.io Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with host.io.</p>

### Version information

Connector Version: 1.0.0


Authored By: spryIQ.co

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-host_io`

## Prerequisites to configuring the connector
- You must have the URL of host.io server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the host.io server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>host.io</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>API Token<br></td><td>Provide API token, used for user authentication.<br>
<tr><td>Server URL<br></td><td>URL of the host.io connector to access the connector website.<br>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Web Domain Details<br></td><td>Get metadata scraped from a domain homepage.<br></td><td>web_domain_details <br/>Utilities<br></td></tr>
<tr><td>Get DNS Domain Details<br></td><td>Get all the DNS records stored for a domain.<br></td><td>dns_domain_details <br/>Utilities<br></td></tr>
<tr><td>Get Related Domains<br></td><td>Get a count of the number of related domains for all supported lookups offered by host.io.<br></td><td>get_related_domains <br/>Utilities<br></td></tr>
<tr><td>Get Full Domains Data<br></td><td>A single endpoint that includes the data from WEB DOMAIN, DNS DOMAIN, RELATED DOMAIN and IPinfo.<br></td><td>full_domains_data <br/>Utilities<br></td></tr>
<tr><td>Get All Domains<br></td><td>Get all domains associated with :field, and a count of the total. The :value should be according to the :field and not necessarily a domain.<br></td><td>get_all_domains <br/>Utilities<br></td></tr>
</tbody></table>

### operation: Get Web Domain Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Web Domain<br></td><td>The domain name for which you want to retrieve a host.io list of metadata.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "domain": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "rank": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "url": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ip": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "date": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "length": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "encoding": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "copyright": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "title": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "links": []
</code><code><br>}</code>
### operation: Get DNS Domain Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>DNS Domain<br></td><td>Domain name for which you want to retrieve a host.io list of dns records.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "domain": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "a": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "aaaa": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "mx": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ns": []
</code><code><br>}</code>
### operation: Get Related Domains
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Domain Name<br></td><td>Domain name for which you want to retrieve related domains count for all lookups offered by host.io.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ip": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "redirects": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "backlinks": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "asn": []
</code><code><br>}</code>
### operation: Get Full Domains Data
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Domain Name<br></td><td>Domain name for which you want to retrieve a host.io list of full data.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "domain": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "dns": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ipinfo": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "web": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "related": {}
</code><code><br>}</code>
### operation: Get All Domains
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Field<br></td><td>Provide field name to get associated domains.<br>
</td></tr><tr><td>Value<br></td><td>The value should be according to the field and not necessarily a domain.<br>
</td></tr><tr><td>Limit<br></td><td>Must be one of 0, 1, 5, 10, 25, 100, 250, or 1000. Default is 25.<br>
</td></tr><tr><td>Page<br></td><td>The page of data to view, 0-indexed. Default is 0. Pagination takes into account the limit.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "domains": []
</code><code><br>}</code>
## Included playbooks
The `Sample - host_io - 1.0.0` playbook collection comes bundled with the host.io connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the host.io connector.

- Get All Domains
- Get DNS Domain Details
- Get Full Domains Data
- Get Related Domains
- Get Web Domain Details

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
