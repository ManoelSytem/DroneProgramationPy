import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))

def getkey(KeyName):
    ans = False
    
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'k_{}'.format(KeyName))

    if keyInput[myKey]:
       ans = True
    pygame.display.update()
   
    return ans

def main():
    print(getkey("a"))


if __name__== '__main__':
    init()
    while True:
        main()




