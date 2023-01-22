config = {
     'bootstrap.servers': '<bootstrap_server>',     
     'security.protocol': 'SASL_SSL',
     'sasl.mechanisms': 'PLAIN',
     'sasl.username': '<api_key>', 
     'sasl.password': '<api_val>'}

sr_config = {
    'url': '<schema_registry_url>',
    'basic.auth.user.info':'<schema_registry_api_key>:<schema_registry_api_val>'
}