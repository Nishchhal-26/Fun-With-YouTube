import webbrowser
while True:
    ch=input('Enter choice from below-\n1)Extract Thumbnails of a youtube video\n2)Download a youtube video\n3)Exit\nChoice - ')
    if ch=='1':
        url=input('Enter the link of the youtube video (Note-youtu.be or youtube.com format supported - ')
        #https://i.ytimg.com/vi/Code-of video/0.jpg
        if url.find('watch?v=') >0:
            a=url.split('watch?v=')
        else:
            a=url.split('/')
        b=a[-1]
        link='https://i.ytimg.com/vi/'+b+'/0.jpg'
        webbrowser.open(link)
    elif ch=='2':
        url=input('Enter the link of the youtube video (Note-youtu.be or youtube.com format supported - ')
        webbrowser.open('https://yt1s.com/en5?q='+url)
    elif ch=='3':
        break
    else:
        print('Invalid Choice')
