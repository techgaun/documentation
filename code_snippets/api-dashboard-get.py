from datadog import initialize, api

options = {
    'api_key': 'api_key',
    'app_key': 'app_key'
}

initialize(**options)

api.Timeboard.get(4953)
