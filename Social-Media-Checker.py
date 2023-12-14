import requests

class ChecK():

    def __init__(self):
        self.email = str(input("Enter Email: "))
        self.twitter()

    def PrintT(self):
        print(f"{self.email} = Linked" + "\n")

    def PrintF(self):
        print(f"{self.email} = Unlinked" + "\n")

    def twitter(self):
        print("==================")
        print("[+] Twitter [+]")
        print("")
        r = requests.Session()
        url = "https://api.twitter.com/i/users/email_available.json?email=" + self.email
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
        Host = "api.twitter.com"
        Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        r.headers = {'User-Agent': user_agent, 'Host': Host, 'Accept': Accept}
        req = r.get(url).json()
        text = str(req)
        print(text)
        print('')
        if text.find("'valid': False") == True:
            self.PrintT()
        else:
            self.PrintF()
        self.instagram()

    def instagram(self):
        print("==================")
        print("[+] Instagram [+]")
        print("")
        r = requests.Session()
        url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        r.headers = {'user-agent': user_agent}
        r.headers.update({'X-CSRFToken': "missing"})
        data = {"email_or_username": self.email}
        req = r.post(url, data=data)
        print(req.text)
        print('')
        if req.text.find("We sent an self.email to") >= 0:
            self.PrintT()
        elif req.text.find("password") >= 0:
            self.PrintT()
        elif req.text.find("sent") >= 0:
            self.PrintT()
        else:
            self.PrintF()
        self.snapchat()

    def snapchat(self):
        print("==================")
        print("[+] Snapchat [+]")
        print("")
        url = "https://bitmoji.api.snapchat.com/api/user/find"
        r = requests.Session()
        r.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        req = r.post(url, headers=r.headers, json={"email": self.email})
        status = req.status_code
        print(status)
        print('')
        if status == 200:
            print(f"{self.email} = is linked to an account" + "\n")
            file = open("snapchat-linked.txt", "a")
            file.write(self.email + "\n")
            file.close()
        else:
            print(f"{self.email} = is not linked to an account" + "\n")


if __name__ == "__main__":
    print("""
             [-] SocialMediaChecker [-]
              [ Twitter - Instagram - Snapchat ]
        ======================================= 
        [+] Run by : DigiHub            |
        =======================================
        """)
    ChecK()

print('')
print('Press enter to exit .')
input('')
