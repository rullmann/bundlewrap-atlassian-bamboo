svc_systemd = {
    'atlassian-bamboo': {},
}

files = {
    '/etc/systemd/system/atlassian-bamboo.service.d/environment.conf': {
        'content_type': 'mako',
        'mode': '0644',
        'source': 'systemd-environment.conf',
        'triggers': ['svc_systemd:atlassian-bamboo:restart', 'action:systemd-daemon-reload'],
    },
    '/opt/bamboo/bin/setenv.sh': {
        'content_type': 'mako',
        'mode': '0755',
        'source': 'setenv.sh',
        'triggers': ['svc_systemd:atlassian-bamboo:restart'],
    },
    '/opt/bamboo/conf/server.xml': {
        'content_type': 'mako',
        'mode': '0644',
        'source': 'server.xml',
        'triggers': ['svc_systemd:atlassian-bamboo:restart'],
    },
    '/opt/bamboo/webapps/jolokia.war': {
        'owner': 'bamboo',
        'content_type': 'binary',
        'mode': '0644',
        'triggers': ['svc_systemd:atlassian-bamboo:restart'],
    },
}

directories = {
    '/opt/bamboo/webapps': {
        'mode': '0755',
        'owner': 'bamboo',
    },
}
