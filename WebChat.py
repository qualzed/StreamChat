import webview

supported_links = ['youtube', 'twitch']

def check_link(chat_link):
    for links in supported_links:
        if(links in chat_link):
            webview.create_window("StreamChat", chat_link)
            webview.start()
        else:
            print("Link not supported")

chat_link = str(input("Link on chat: "))
check_link(chat_link)