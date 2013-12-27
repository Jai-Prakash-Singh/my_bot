import imaplib, sys
import email
from bs4 import BeautifulSoup
import proxy_module


def show_header(msg_data):
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1])
            for header in [ 'subject', 'to', 'from' ]:
                print '%-8s: %s' % (header.upper(), msg[header])

def activate_link(l):
    page = proxy_module.main(l)
    print page.url
    page.close()

def get_verify_url(mesginfo):
    soup = BeautifulSoup(mesginfo)
    data = soup.select('a[href*="verify"]')
    #print data
    try:
        for l in data:
            l = l.get("href").encode("ascii","ignore")
            activate_link(l)
    except:
        pass



def email_read(username,password): 
    conn = imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        (retcode, capabilities) = conn.login(username, password)
    except:
        print sys.exc_info()[1]
        sys.exit(1)

    conn.select(readonly=1) # Select inbox or default namespace
    (retcode, messages) = conn.search(None, '(UNSEEN)')

    if retcode == 'OK':
        messages = messages[0].split(' ')
        messages = messages[-3:]
        for message in messages:
            print 'Processing :', message

            typ, msg_data = conn.fetch(message, '(RFC822)')
            if typ =="OK":
                pass
                #show_header(msg_data)

            ret, mesginfo = conn.fetch(message, '(BODY.PEEK[TEXT])')  
            if ret =="OK":
                #print >>f1,'Message %s\n%s\n' % (ret, mesginfo[0][1])    
                #print >>f1, mesginfo,'\n',30*'-'
                mesginfo = 'Message %s\n%s\n' % (ret, mesginfo[0][1])
                get_verify_url(mesginfo)
    else:     
        pass
    
    print "connection closed"
    conn.close()
    


if __name__=="__main__":
    username = "xxxxxxxxxxx"
    password = "xxxxxxxxxxx" 
    email_read(username,password)              


