# Week05 Day1 - OOP - XP Ninja
# Created on  : 210502 by : lidu
# Modified on : 210502 by : lidu

class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []
    def __str__(self):
        return (self.phone_number)
    def __repr__(self):
        return (self.phone_number)
    def call(self, other_phone, is_incoming):
        out_str = self.phone_number + ' was called by '*is_incoming + ' has called '*(not is_incoming) + other_phone.phone_number 
        self.call_history.append(out_str)
        print(out_str)
    def show_call_history(self):
        for line in self.call_history:
            print(line)
    def send_message(self, msgTxt, msgRcvr):
        self.messages.append({'rcvr': msgRcvr, 'sndr': self, 'content': msgTxt})
        msgRcvr.messages.append({'rcvr': self , 'sndr': msgRcvr, 'content': msgTxt})
        print(self.messages)
    def show_outgoing_messages(self):
        list_outgoing = [msg['content'] for msg in self.messages if msg['sndr'] == self]
        print(f'Outgoing messages for {self}')
        if len(list_outgoing) == 0:
            print('None')
        else:
            print('\n'.join(list_outgoing))
    def show_incoming_messages(self):
        pass
    def show_messages_from(self, number):
        pass

john = Phone('555-111111')
tom = Phone('555-222222')
john.call(tom, True)
john.call(tom, False)
john.show_call_history()
john.send_message('Coucou', tom)
tom.send_message('Salut', john)
john.show_outgoing_messages()
# tom.show_outgoing_messages()
