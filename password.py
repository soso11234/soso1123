

import pygame

class OTP():
    def __init__(self):
        
        pass
    def password_drawing(self):
        pygame.init()
        size = (500,500)
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        passcode = []
        screen = pygame.display.set_mode(size)
        running = True
        for x in range (4):
            for y in range(4):
                pygame.draw.rect(screen,white,(100*x,100*y,100,100))
                pygame.draw.rect(screen,black,(100*x,100*y,101,101),1)
                pygame.draw.circle(screen,black,(50+100*x,50+100*y),10)     
        while running:
            if len(passcode) == 4: #the length of pattern 
                running = False
            else:
                pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if len(passcode) <= 4:   #The pattern has to be 4, and a user has to know how many box the user pick, and how many box left               
                        if x < 100 and y < 100:
                            pygame.draw.circle(screen,red,(50,50),10)
                            passcode.append(1)
                        elif x < 100 and y < 200:
                            pygame.draw.circle(screen,red,(50,150),10)
                            passcode.append(2)
                        elif x < 100 and y < 300:
                            pygame.draw.circle(screen,red,(50,250),10)
                            passcode.append(3)
                        elif x < 100 and y < 400:
                            pygame.draw.circle(screen,red,(50,350),10)
                            passcode.append(4)
                        elif 100 < x < 200 and y < 100:
                            pygame.draw.circle(screen,red,(150,50),10)
                            passcode.append(5)
                        elif 100 < x < 200 and y < 200:
                            pygame.draw.circle(screen,red,(150,150),10)
                            passcode.append(6)
                        elif 100 < x < 200 and y < 300:
                            pygame.draw.circle(screen,red,(150,250),10)
                            passcode.append(7)
                        elif 100 < x < 200 and y < 400:
                            pygame.draw.circle(screen,red,(150,350),10)
                            passcode.append(8)
                        elif 200 < x < 300 and y < 100:
                            pygame.draw.circle(screen,red,(250,50),10)
                            passcode.append(9)
                        elif 200 < x < 300 and y < 200:
                            pygame.draw.circle(screen,red,(250,150),10)
                            passcode.append(10)
                        elif 200 < x < 300 and y < 300:
                            pygame.draw.circle(screen,red,(250,250),10)
                            passcode.append(11)
                        elif 200 < x < 300 and y < 400:
                            pygame.draw.circle(screen,red,(250,350),10)
                            passcode.append(12)
                        elif 300 < x < 400 and y < 100:
                            pygame.draw.circle(screen,red,(350,50),10)
                            passcode.append(13)
                        elif 300 < x < 400 and y < 200:
                            pygame.draw.circle(screen,red,(350,150),10)
                            passcode.append(14)
                        elif 300 < x < 400 and y < 300:
                            pygame.draw.circle(screen,red,(350,250),10)
                            passcode.append(15)
                        elif 300 < x < 400 and y < 400:
                            pygame.draw.circle(screen,red,(350,350),10)
                            passcode.append(16)
                        else:
                            break
                    else:
                        print('click 5, close it ')
                        running = False
                    
            pygame.display.update()
        passcode.sort() # Password has to be same, even though a user start from any points ex)1,2,3,4 = 4,3,2,1
        return passcode

    def id(self):
        username = input('Write your username >> ')
        f = open('database','r') #log in ! 
        searching = f.read()
        if username in searching:
            f.close()
            return username
        else:
            print("Your username doesn't exist, please try again.") 
            id(self)
    def create_id(self):
        username = input('Create your username >> ')
        f = open('database','a')
        f.write('id\n')
        f.write(username+'\n')
        f.close()
        return username
    
    def check(self):     
        begin = input("Do you have user name? if you have, type Y, if you don't have, type N >> ").lower()
        if begin == 'y':
            OTP.id(self)
            passcode = OTP.password_drawing(self)
            f = open('database','r')
            line = f.read().strip("[,]\n").strip().split('\n')
            vertix = []
            for i in line:
                vertix.append(i)
            f.close()
            if str(passcode) == (vertix[2]):
                print('login success!')
                return True
            else:
                print('wrong password')
                OTP.check(self)
        elif begin == 'n':
            OTP.create_id(self)
            create_passocde = OTP.password_drawing(self)
            f = open('database','a')
            f.write(str(create_passocde)+'\n')
            f.close()
            print('Register success!')
            return True
        else:
            print('Type wrong word')

class Register():
    def __init__(self):
        pass
    def site(self):
        address = input('Enter the website or program what you want to register >>')
        f = open('database','a')
        f.write(address+'\n')
        f.close()
        print('Register success!')
        return address
    def site_id(self):
        site = Register.site(self)
        id_site = input("Enter the id of the webiste or program what you want to register >>")
        f = open('database','a')
        f.write(site+','+id_site+'\n')
        f.close()
        print('Register success!')
        return id_site
    def site_password(self):
        password_site = input("Enter the password >>")
        f = open('database','a')
        f.write(password_site+'\n')
        f.close()
        print('Register success!')
        return password_site




def main():
    otp = OTP()
    register = Register()
    checking = otp.check()
    start = True
    while start:
        if checking == True:
            choice = input('Type R for register your account and password of any sites or program. Type D for displaying what you register in here, and Type Q to exit.').lower()
            if choice == 'r':
                repeat = int(input('How many site or prgram would you like to add in here? >> '))
                n = 0
                while n < repeat:
                    register.site_id()
                    register.site_password()
                    n +=1
            elif choice == 'd':
                double_check = otp.id()
                print(dictionary2(double_check))

            elif choice == 'q':
                start = False
            else:
                print("You type wrong word, please try again.")   
        else:
            otp.check()


def dictionary(username): # to display every information
    f = open('database','r')
    line = f.read().strip("[,]\n").strip().split('\n')
    vertix = ['id','password','site','site_id','site_password']
    contents= [] # read file, and make it in a list
    id_address=[] # what index of 'id' in the contents list, it's to distinguish between differnet username in the file
    diction = {}
    for i in line:
        contents.append(i)
    begin = contents.index(username) # find username in contents list
    for index, value in enumerate(contents): 
        if value == 'id':
            id_address.append(index) # find 'id' index in the list
    for value in id_address: #every index of 'id' in contents list
        if value == begin-1: #being = username, and also the 'id' has to be before the username, because the 'id' is the milstone of each username
            a = value #find the 'id' for start make a dictionary of the username information
        else:
            pass
    b = id_address.index(a) #the 'id' right before the username(which is typed by user)
    if len(id_address) > 1: #if more than 1 username was registered
        slicing = contents[a+1:id_address[b+1]] # 'id'befor the username to next 'id'
        if len(slicing)>6: # if a user input more than 1 site/program
            repeat = (len(slicing)-len(vertix))//3 #the length always 3 more (site, site_id and site_password) from 5
            for i in vertix:
                diction[i] = [] #site, site_id and site_password can be more than 1, that's why empty list is added to each key
                for num in range(0,repeat+1):
                    if vertix.index(i) >=2:
                        diction[i].append(slicing[vertix.index(i)+3*num]) #for site, site_id and site_password key, add each value into the keys
                    else:
                        diction[i]=[slicing[vertix.index(i)]] # if a user add only one site or program
    else:
        slicing_solo = contents[1:]
        repeat_solo = (len(slicing_solo)-len(vertix))//3 #the length always 3 more (site, site_id and site_password) from 5
        for i in vertix:
            diction[i] = []
            for num in range(0,repeat_solo+1):
                if vertix.index(i)>=2:
                    diction[i].append(slicing_solo[vertix.index(i)+3*num])
                else:
                    diction[i] = [slicing_solo[vertix.index(i)]]    
    return diction

def dictionary2(username):
    f = open('database','r')
    line = f.read().strip("[,]\n").strip().split('\n')
    vertix = ['site','site_id','site_password']
    contents= [] # read file, and make it in a list
    id_address=[] # what index of 'id' in the contents list, it's to distinguish between differnet username in the file
    diction = {}
    for i in line:
        contents.append(i)
    begin = contents.index(username) # find username in contents list
    for index, value in enumerate(contents): 
        if value == 'id':
            id_address.append(index) # find 'id' index in the list
    for value in id_address: #every index of 'id' in contents list
        if value == begin-1: #being = username, and also the 'id' has to be before the username, because the 'id' is the milstone of each username
            a = value #find the 'id' for start make a dictionary of the username information
        else:
            pass
    b = id_address.index(a) #the 'id' right before the username(which is typed by user)
    if len(id_address) > 1: #if more than 1 username was registered
        slicing = contents[begin+2:id_address[b+1]] # site to next 'id'
        if len(slicing)>6: # if a user input more than 1 site/program
            repeat = (len(slicing))//3 #the length always 3 more (site, site_id and site_password) from 5
            for i in vertix:
                diction[i] = [] #site, site_id and site_password can be more than 1, that's why empty list is added to each key
                for num in range(0,repeat):
                    if vertix.index(i) >=2:
                        diction[i].append(slicing[vertix.index(i)+3*num]) #for site, site_id and site_password key, add each value into the keys
                    else:
                        diction[i]=[slicing[vertix.index(i)]] # if a user add only one site or program
    else:
        slicing_solo = contents[3:]
        repeat_solo = (len(slicing_solo))//3 #the length always 3 more (site, site_id and site_password) from 3
        for i in vertix:
            diction[i] = []
            for num in range(0,repeat_solo):
                if len(slicing_solo) > 3:
                    diction[i].append(slicing_solo[vertix.index(i)+3*num])
                else:
                    diction[i] = [slicing_solo[vertix.index(i)]]    
    return diction

main()
