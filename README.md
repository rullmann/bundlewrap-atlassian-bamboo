# atlassian-bamboo

Atlassian Bamboo, a CI/CR tool, can be managed by bundlewrap with this bundle.
As the software is proprietary and repositories are not available the setup is a bit tricky. You've been warned!

## Requirements

* [Oracle JDK](https://gist.github.com/rullmann/e909ec68b66ac711bf441188dbea93c0) installed under `/opt/java/current`
* [Atlassian Bamboo] installed under `/opt/bamboo` with a systemd unit called `atlassian-bamboo.service`
  * This can be achived by building rpm files: https://github.com/rullmann/atlassian-rpm-specs

## Setup notes

* Install Oracle JDK
* Install Atlassian Bamboo by using an rpm file
* Assign this bundle to a node and add the required metadata

## Integrations

* Bundles:
  * [telegraf](https://github.com/rullmann/bundlewrap-telegraf)

## Metadata

    'metadata': {
        'atlassian-bamboo': {
            'proxyname': 'bamboo.example.org', # required
            'jvm_args': '-XX:+UseG1GC', # optional, add additional JVM parameter
            'enable_jmx': False, # optional, will open port 5002 for JMX
            'jvm_min_mamory': '1024m', # optional
            'jvm_max_mamory': '1024m', # optional
        },
    }
