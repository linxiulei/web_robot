#!/usr/bin/env python

import logging
from pyxmpp2.jid import JID
from pyxmpp2.message import Message
from pyxmpp2.client import Client
from pyxmpp2.simple import send_message
from pyxmpp2 import streamtls
from pyxmpp2.interfaces import EventHandler, event_handler

class MyHandler(EventHandler):
    def __init__(self, target_jid, message):
        self.target_jid = target_jid
        self.message = message

    @event_handler(AuthorizedEvent)
    def handle_authorized(self, event):
        message = Message(to_jid = self.target_jid, body = self.message)
        event.stream.send(message)
        event.stream.disconnect()

    @event_handler(DisconnectedEvent)
    def handle_disconnected(self, event):
        return QUIT
    
    @event_handler()
    def handle_all(self, event):
        logging.info(u"-- {0}".format(event))

class Gtalk():
    def __init__(self, sid, spwd):
        self.sid = JID(sid)
	self.spwd = spwd

    def send_msg(self, rid, msg):
        self.rid = JID(rid)
	if not self.sid.resource:
	    self.sid = JID(self.sid.local, self.sid.domain,'send_message')

	msg = Message(to_jid=self.rid, body=msg)
	def send(stream):
	    stream.send(msg)
	   
	self.xmpp_do(send)

    def xmpp_do(self, function):
        class GtalkClient(Client):
	    def session_started(self):
	        function(self.stream)
		self.disconnect()

	#tls = streamtls.TLSSetings(require=True, verify_peer=False)
	tls = streamtls.XMPPSettings({
	                                  u'passord':'64227072'
	                             })
        auth = ['sasl:PLAIN']
        handler = MyHandler(JID(target_jid), message)
	gtalkClient = GtalkClient(self.sid, EventHandler(), settings=tls)
	gtalkClient.connect()
	try:
	    gtalkClient.loop(1)
	except KeyboardInterrupt:
	    print u'disconnection...'
	    gtalkClient.disconnect()


if __name__ == '__main__':
    g = Gtalk('linshoulei@gmail.com',u'64227072')
    g.send_msg('linxiulei@gmail.com','hello world')
