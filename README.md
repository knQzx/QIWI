# QIWI
Hello everyone! This is a script based on the QIWI API. It contains functions that reduce 
the work of a person. Also, this script can be used to help people who make payments in their, for example, Telegram Bot store.


# QIWI FROM STORE
There is a "QIWI FROM STORE" file here. This script provides you with clean functions for creating payments in your, for example, 
telegram store on python. You will only need your phone number, without the+, and a qiwi token, which you can register here - 
[QIWI API TOKEN](https://qiwi.com/api). For example, you can configure the payment so that in the bot you will give a special generated key, the 
person will send you money, the program reads the information about the payment and if the comment is the same, the program puts 
this money on the bot.


# QIWI API
# This script will help you find out all the details of the payment to your account. Let's go through the functions:
##### profile_information - gets all the information about your profile in the form of a dictionary
##### date_of_creation - gets the date of creation of your qiwi profile
##### banc - gets the bank name
##### level_iden - gets your profile information about your identification level
##### validity_period - checks whether the passport has expired, returns either true or false
##### number_person - get your number
##### name_person - get your nickname
##### last_transaction_status - get the status of the last payment on the account
##### last_transaction_number - get the number of the person who last transferred money to us 
##### last_transaction_sum - get the amount of the last receipt of money
##### last_transaction_info_end-get all the information about the payment, amount and currency
##### balance - get the current balance in rubles
##### nickname_user - get the username of the user balance
##### nickname_banc - get the bank's omnidonym
##### name_of_money - get the name of the corresponding wallet account
***
# Данный скрипт вам поможет узнать все данные платежа на ваш аккаунт. Пройдёмся по функциям:
##### profile_information - получает всю информацию о вашем профиле в виде словаря
##### date_of_creation - получает дату создания вашего qiwi профиля
##### banc - получает имя банка
##### level_iden - получает информация вашего профиля о вашем уровне идентификации
##### validity_period - проверяет не истёк ли срок действия паспорта, возвращает либо true либо false
##### number_person - получаем свой номер
##### name_person - получаем свой никнейм
##### last_transaction_status - получаем статус последнего платежа на аккаунте
##### last_transaction_number - получаем номер человека который последним нам перевёл деньги
##### last_transaction_sum - получаем сумму последнего получения денег
##### last_transaction_info_end - получаем всю информацию о платеже, amount and валюта
##### balance - получаем текущий баланс в рублях
##### nickname_user - получаем всевдоним пользовательского баланса
##### nickname_banc - получаем всевдоним банка
##### name_of_money - получаем название соответствующего счета кошелька
***
We can call the functions of the first file like this:
qiwi = Qiwi(input('enter your number here without +: '), input('enter your qiwi token here: '))
print(qiwi.<function name>)
***
In the second file, this happens like this:
qiwi = Store_QIWI(input('enter your number here without +: '), input('enter your qiwi token here:  '))
print(qiwi.<function name>)



