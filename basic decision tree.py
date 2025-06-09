
while True:

    browser = input("What browser do you use? ")

    browserOptions = ['firefox', 'chrome', 'edge', 'internet explorer', 'TOR', 'opera', 'opera gx', 'zen', 'chromium','netscape']

    if browser in browserOptions:
        break
    else:
        print(f"Choices = {', '.join(browserOptions)}")