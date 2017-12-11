import requests
import time
from time import sleep

token = '465665994:AAExqJJ9Gl6hJfE1U4371zerf2n1rPFf-WE'

URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0

#Добавить кнопки
#Добавить остальные API
#Допилить cftime

def ctftime():
    
    now = int(time.time())
    nxmounth = now + 31536000
    #print(now)
    #print(nxmounth)
    
    #url = 'https://ctftime.org/api/v1/events/?limit=1&start={}&finish={}'.format(str(now),str(nxmounth))   
    #print(url)
    
    #response = requests.get(url).json()
    #print(response)
    
    #date = response['organizers']['start']
    #print (date)
    
    #name = response['organizers']['name']
    #print(str(name))
    
    #calendar = name + date
    #return str(response)

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()

def get_message():
    
    data = get_updates()

    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        
        chat_id = data['result'][-1]['message']['chat']['id']
        message_text = last_object['message']['text']

        message = {'chat_id': chat_id, 'text': message_text}

        return message
    return None

def send_message(chat_id, text='Wait, please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id,text)
    requests.get(url)

def main():

    while True:
        answer = get_message()
        
        if answer != None:   
            chat_id = answer['chat_id']
            text = answer['text']
        
            if text == '/soon':
                send_message(chat_id,'Dont work! Please wait.')
                print('/soon')
                print(chat_id)
                
            if text == '/rasp':
                send_message(chat_id, 'https://ctftime.org/calendar/')
                print('/rasp')
                print(chat_id)

            if (text != '/rasp' and text != '/soon'):
                send_message(chat_id, 'Invalid command!')

        #else:
                #continue
        #sleep (2)
        
if __name__ == '__main__':
    main()

