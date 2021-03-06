import requests
import json


def get_profile(self, token):
    s7 = requests.Session()
    s7.headers['Accept'] = 'application/json'
    s7.headers['authorization'] = 'Bearer ' + token
    p = s7.get('https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled=true&contractInfoEnabled=true&userInfoEnabled=true')
    return p.json()


def gg(login, api_access_token):
    balances = balance(login, api_access_token)['accounts']
    # рублевый баланс
    rubAlias = [x for x in balances if x['alias'] == 'qw_wallet_rub']
    return rubAlias


def balance(login, api_access_token):
    s = requests.Session()
    s.headers['Accept'] = 'application/json'
    s.headers['authorization'] = 'Bearer ' + api_access_token
    b = s.get('https://edge.qiwi.com/funding-sources/v2/persons/' + login + '/accounts')
    return b.json()
    # все балансы


class Qiwi:
    def __init__(self, number, token):
        self.number = number
        self.token = token
        self.profile = get_profile(self.token)

    def profile_information(self):
        '''получаем информацию о профиле'''
        return self.profile['contractInfo']

    def date_of_creation(self):
        '''получаем дату создания'''
        return self.profile['contractInfo']['creationDate']

    def banc(self):
        '''получаем имя банка'''
        return self.profile['contractInfo']['identificationInfo'][0]['bankAlias']

    def level_iden(self):
        '''получаем левел идентефикации пользователя'''
        return self.profile['contractInfo']['identificationInfo'][0]['identificationLevel']

    def validity_period(self):
        '''истек ли срок действия паспорт, возвращает true или false'''
        return self.profile['contractInfo']['identificationInfo'][0]['passportExpired']

    def number_person(self):
        '''получаем номер человека'''
        return self.profile['contractInfo']['contractId']

    def name_person(self):
        '''получаем никнейм пользователя'''
        return self.profile['contractInfo']['nickname']['nickname']

    def last_transaction_status(self):
        '''получаем статус последнего платежа на наш аккаунт'''
        s = requests.Session()
        s.headers['authorization'] = 'Bearer ' + self.token
        parameters = {'rows': '50'}
        h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + self.number + '/payments', params=parameters)
        req = json.loads(h.text)
        return req['data'][0]['status']

    def last_transaction_number(self):
        '''получаем телефон человека который последним отправил нам деньги '''
        s = requests.Session()
        s.headers['authorization'] = 'Bearer ' + self.token
        parameters = {'rows': '50'}
        h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + self.number + '/payments', params=parameters)
        req = json.loads(h.text)
        return req['data'][0]['account']

    def last_transaction_sum(self):
        '''получаем сумму последнего платежа отправленного нам'''
        s = requests.Session()
        s.headers['authorization'] = 'Bearer ' + self.token
        parameters = {'rows': '50'}
        h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + self.number + '/payments', params=parameters)
        req = json.loads(h.text)
        return req['data'][0]['sum']['amount']

    def last_transaction_info_end(self):
        '''получаем конечную инфу о платеже, amout это сумма, а currency это валюта'''
        s = requests.Session()
        s.headers['authorization'] = 'Bearer ' + self.token
        parameters = {'rows': '50'}
        h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + self.number + '/payments', params=parameters)
        req = json.loads(h.text)
        return req['data'][0]['total']

    def balance(self):
        '''текущий баланс в рублях'''
        return gg(self.number, self.token)[0]['balance']['amount']

    def nickname_user(self):
        '''Псевдоним пользовательского баланса'''
        return gg(self.number, self.token)[0]['alias']

    def nickname_banc(self):
        '''Псевдоним банка'''
        return gg(self.number, self.token)[0]['bankAlias']

    def name_of_money(self):
        '''Название соответствующего счета кошелька'''
        return gg(self.number, self.token)[0]['title']


qiwi = Qiwi(input('введи сюда свой номер без +: '), input('введи сюда свой qiwi token - '))

