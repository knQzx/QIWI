# QIWI
Hello everyone! This is a script based on the QIWI API. It contains functions that reduce 
the work of a person. Also, this script can be used to help people who make payments in their, for example, Telegram Bot store.
You can use this to track transactions to your QIWI account. You can attach this to a separate database and check every second whether a payment has been received or not. If you have entered, then just fill in the data in this database.


# QIWI FROM STORE
There is a "QIWI FROM STORE" file here. This script provides you with clean functions for creating payments in your, for example, 
telegram store on python. You will only need your phone number, without the+, and a qiwi token, which you can register here - 
[QIWI API TOKEN](https://qiwi.com/api). For example, you can configure the payment so that in the bot you will give a special generated key, the 
person will send you money, the program reads the information about the payment and if the comment is the same, the program puts 
this money on the bot.


# QIWI API
# This script will help you find out all the details of the payment to your account. Let's go through the functions:
##### <code>profile_information</code> - gets all the information about your profile in the form of a dictionary
##### <code>date_of_creation</code> - gets the date of creation of your qiwi profile
##### <code>banc</code> - gets the bank name
##### <code>level_iden</code> - gets your profile information about your identification level
##### <code>validity_period</code> - checks whether the passport has expired, returns either true or false
##### <code>number_person</code> - get your number
##### <code><code>name_person</code> - get your nickname
##### <code>last_transaction_status</code> - get the status of the last payment on the account
##### <code>last_transaction_number</code> - get the number of the person who last transferred money to us 
##### <code>last_transaction_sum</code> - get the amount of the last receipt of money
##### <code>last_transaction_info_end</code> - get all the information about the payment, amount and currency
##### <code>balance</code> - get the current balance in rubles
##### <code>nickname_user</code> - get the username of the user balance
##### <code>nickname_banc</code> - get the bank's omnidonym
##### <code>name_of_money</code> - get the name of the corresponding wallet account
***
# Данный скрипт вам поможет узнать все данные платежа на ваш аккаунт. Пройдёмся по функциям:
##### <code>profile_information</code> - получает всю информацию о вашем профиле в виде словаря
##### <code>date_of_creation</code> - получает дату создания вашего qiwi профиля
##### <code>banc</code> - получает имя банка
##### <code>level_iden</code> - получает информация вашего профиля о вашем уровне идентификации
##### <code>validity_period</code> - проверяет не истёк ли срок действия паспорта, возвращает либо true либо false
##### <code>number_person</code> - получаем свой номер
##### <code>name_person</code> - получаем свой никнейм
##### <code>last_transaction_status</code> - получаем статус последнего платежа на аккаунте
##### <code>last_transaction_number</code> - получаем номер человека который последним нам перевёл деньги
##### <code>last_transaction_sum</code> - получаем сумму последнего получения денег
##### <code>last_transaction_info_end</code> - получаем всю информацию о платеже, amount and валюта
##### <code>balance</code> - получаем текущий баланс в рублях
##### <code>nickname_user</code> - получаем всевдоним пользовательского баланса
##### <code>nickname_banc</code> - получаем всевдоним банка
##### <code>name_of_money</code> - получаем название соответствующего счета кошелька
***
We can call the functions of the first file like this:<br/>
qiwi = Qiwi(input('enter your number here without +: '), input('enter your qiwi token here: '))<br/>
print(qiwi.<function name>)
***
In the second file, this happens like this:<br/>
qiwi = Store_QIWI(input('enter your number here without +: '), input('enter your qiwi token here:  '))<br/>
print(qiwi.<function name>)
