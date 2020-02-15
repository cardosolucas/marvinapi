import requests
import json

class MarvinAPI:
    def __init__(self, url):
        self.url = url

    def acquisitor(self, action, parameters={}):
        alowed_action = [
            'reload',
            'health',
            'status'
        ]
        if action not in alowed_action:
            return {'error': True}
        elif action == alowed_action[1]:
            resp = requests.get(self.url + '/acquisitor/' + action)
        else:
            resp = requests.push(self.url + '/acquisitor/' + action, json = parameters)

        if resp.status_code != 200:
            return {'error': True}
        else:
            to_return_dict = resp.json()
            to_return_dict['error'] = False
            return to_return_dict

    def tpreparator(self, action, parameters={}):
        alowed_action = [
            'reload',
            'health',
            'status'
        ]
        if action not in alowed_action:
            return {'error': True}
        elif action == alowed_action[1]:
            resp = requests.get(self.url + '/tpreparator/' + action)
        else:
            resp = requests.push(self.url + '/tpreparator/' + action, json = parameters)

        if resp.status_code != 200:
            print(resp.status_code)
            return {'error': True}
        else:
            to_return_dict = resp.json()
            to_return_dict['error'] = False
            return to_return_dict

    def trainer(self, action, parameters={}):
        alowed_action = [
            'reload',
            'health',
            'status'
        ]
        if action not in alowed_action:
            return {'error': True}
        elif action == alowed_action[1]:
            resp = requests.get(self.url + '/trainer/' + action)
        else:
            resp = requests.push(self.url + '/trainer/' + action, json = parameters)

        if resp.status_code != 200:
            print(resp.status_code)
            return {'error': True}
        else:
            to_return_dict = resp.json()
            to_return_dict['error'] = False
            return to_return_dict

    def evaluator(self, action, parameters={}):
        alowed_action = [
            'reload',
            'health',
            'status',
            'metrics'
        ]
        if action not in alowed_action:
            return {'error': True}
        elif action == alowed_action[1]:
            resp = requests.get(self.url + '/evaluator/' + action)
        else:
            resp = requests.push(self.url + '/evaluator/' + action, json = parameters)

        if resp.status_code != 200:
            print(resp.status_code)
            return {'error': True}
        else:
            to_return_dict = resp.json()
            to_return_dict['error'] = False
            return to_return_dict

    def feedback(self, action, parameters={}):
        alowed_action = [
            'reload',
            'health',
            'status'
        ]
        if action not in alowed_action:
            return {'error': True}
        elif action == alowed_action[1]:
            resp = requests.get(self.url + '/feedback/' + action)
        else:
            resp = requests.push(self.url + '/feedback/' + action, json = parameters)

        if resp.status_code != 200:
            print(resp.status_code)
            return {'error': True}
        else:
            to_return_dict = resp.json()
            to_return_dict['error'] = False
            return to_return_dict

    def predictor(self, action, parameters={}):
        alowed_action = [
            'reload',
            'health',
            'status'
        ]
        if action not in alowed_action:
            return {'error': True}
        elif action == alowed_action[1]:
            resp = requests.get(self.url + '/predictor/' + action)
        else:
            resp = requests.push(self.url + '/predictor/' + action, json = parameters)

        if resp.status_code != 200:
            print(resp.status_code)
            return {'error': True}
        else:
            to_return_dict = resp.json()
            to_return_dict['error'] = False
            return to_return_dict

    def predict(self, message):
        parameters = {
            'message': [message]
        }
        resp = requests.post(self.url + '/predictor', json=parameters)
        if resp.status_code != 200:
            return {'error': True}
        else:
            to_return_dict = resp.json()
            to_return_dict['error'] = False
            return to_return_dict

    def send_feedback(self, message):
        parameters = {
            'message': [message]
        }
        resp = requests.post(self.url + '/feedback', json=parameters)
        if resp.status_code != 200:
            return {'error': True}
        else:
            to_return_dict = resp.json()
            to_return_dict['error'] = False
            return to_return_dict

    def get_metrics(self, protocol):
        parameters = {
            'protocol': protocol,
        }
        resp = requests.post(self.url + '/evaluator/metrics', json=parameters)
        if resp.status_code != 200:
            return {'error': True}
        else:
            to_return_dict = resp.json()
            to_return_dict['error'] = False
            return to_return_dict