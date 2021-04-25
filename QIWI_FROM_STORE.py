import requests
import json


def connect(number, token):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + token
    parameters = {'rows': '50'}
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + number + '/payments', params=parameters)
    req = json.loads(h.text)
    return req


class Store_QIWI:
    def __init__(self, number, token):
        self.number = number
        self.token = token
        self.gg = connect(self.number, self.token)

    def last_pay_status(self):
        '''данная функция возвращает статус платежа проведенного последним,
        так вы можете узнать совершён он или нет'''
        return self.gg['data'][0]['status']

    def last_pay_number(self):
        '''так вы можете увидеть номер с которого отправили деньги'''
        return self.gg['data'][0]['account']

    def last_pay_sum(self):
        '''так вы можете узнать сумму последнего платежа'''
        return self.gg['data'][0]['sum']['amount']

    def last_pay_info(self):
        '''так вы узнаете окончательные данные платежа, его сумму и валюту'''
        return self.gg['data'][0]['total']

    def info_about_provider(self):
        '''так вы получите все данные об провайдере'''
        return self.gg['data'][0]['provider']
    
    def last_pay_comment(self):
        '''так вы получаете комментарий который был к платежу'''
        return self.gg['data'][0]['comment']


qiwi = Store_QIWI(input('введи сюда свой номер без +: '), input('введи сюда свой qiwi token - '))
