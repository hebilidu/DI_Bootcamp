# Week05 Day1 - OOP - XP Ninja
# Created on  : 210502 by : lidu
# Modified on : 210503 by : lidu

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
    def send_message(self, msg_txt, msg_rcvr):
        self.messages.append({'rcvr': msg_rcvr, 'sndr': self, 'content': msg_txt})
        msg_rcvr.messages.append({'rcvr': msg_rcvr , 'sndr': self, 'content': msg_txt})
    def show_outgoing_messages(self):
        list_outgoing = [msg['content'] for msg in self.messages if msg['sndr'] == self]
        print(f'Outgoing messages for {self}:')
        if len(list_outgoing) == 0:
            print('None')
        else:
            print('\n'.join(list_outgoing))
    def show_incoming_messages(self):
        list_incoming = [msg['content'] for msg in self.messages if msg['rcvr'] == self]
        print(f'Incoming messages for {self}:')
        if len(list_incoming) == 0:
            print('None')
        else:
            print('\n'.join(list_incoming))
    def show_messages_from(self, number):
        list_msg_from = [msg['content'] for msg in self.messages if msg['sndr'].phone_number == number]
        print(f'Messages from {number}:')
        if len(list_msg_from) == 0:
            print('None')
        else:
            print('\n'.join(list_msg_from))

john = Phone('555-111111')
tom = Phone('555-222222')
john.call(tom, True)
john.call(tom, False)
john.show_call_history()
john.send_message('Coucou', tom)
tom.send_message('Salut', john)
john.show_outgoing_messages()
john.show_incoming_messages()
john.show_messages_from(tom.phone_number)
tom.show_outgoing_messages()
tom.show_incoming_messages()
tom.show_messages_from(john.phone_number)
john.show_messages_from(john.phone_number)