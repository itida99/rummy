import pygame as p
import random

p.init()

def swap(a,left_cards,ev,middle):
    k = left_cards.index(middle)
    temp = left_cards[left_cards.index(middle)]
    left_cards[left_cards.index(middle)] = a[f_key.index(ev)]
    a[f_key.index(ev)] = temp
    middle = left_cards[k]
    return a,left_cards,middle


def swap_not_inplace(a,left_cards,ev,middle):
    x = a[:]
    y = left_cards[:]
    temp = y[left_cards.index(middle)]
    y[left_cards.index(middle)] = x[f_key.index(ev)]
    x[f_key.index(ev)] = temp
    return x,y,middle

def disp(middle):
    background.fill((0,128,0))
    x=20
    y=5
    for i in range(len(b)):
        background.blit(back,(x,y))
        x+=90
    x=20
    y=350
    background.blit(back,(600,150))
    background.blit(font.render('v', True, (255,255,255)),(645,290))
    background.blit(deck[left_cards[left_cards.index(middle)]],(700,150))
    background.blit(font.render('x', True, (255,255,255)),(745,290))
    for i in a:
        background.blit(deck[i],(x,y))
        background.blit(d_key[f_key[a.index(i)]],(x+45,y+140))
        x+=90
    p.draw.rect(background,(255,0,0),(1200,230,140,70))
    background.blit(font.render('Rummy', True, (255,255,255)),(1210,240))
    background.blit(font.render('z', True, (255,255,255)),(1260,295))

def update_game():
    middle = random.choice(left_cards)
    return middle

    
def move_comp(b):
    ''' takes b and return either -1 or the least priority elements'''
    def sort_by_value(l): 
        n = len(l)  
        for i in range(n): 
            flag = 0
            for j in range(0, n-i-1): 
                if cards.index(l[j][0:-1]) > cards.index(l[j+1][0:-1]) : 
                    l[j], l[j+1] = l[j+1], l[j] 
                    flag = 1
            if flag == 0:
                break
        return l
    def check_sublist(b,a):
        return  b in [a[i:len(b)+i] for i in range(len(a))]
    def form_d(b):
        b =sorted(b, key = lambda t:t[-1])
        c=[]
        j=0
        for i in range(len(b)-1):
            if b[i][-1]!=b[i+1][-1]:
                c.append(b[j:i+1])
                j=i+1
        c.append(b[j:len(b)])
        for i in range(len(c)):
            c[i] = sort_by_value(c[i])
        d=[]
        for i in c:
            d.extend(i)
        return d
    def close_by(b):
        d = form_d(b)
        c=[]
        j=0
        for i in range(len(d)-1):
            if abs(sequenced_cards.index(d[i])-sequenced_cards.index(d[i+1]))>3 and d[i][-1]==d[i+1][-1]:
                c.append(d[j:i+1])
                j=i+1
            if d[i][-1]!=d[i+1][-1]:
                c.append(d[j:i+1])
                j=i+1
        c.append(d[j:len(d)])
        # print(c)
        return c
    def find_triad(l):
        k=[]
        for i in cards:
            if list(map(lambda t : t[0:-1],l)).count(i) == 3:
                k.append(i)
        return k
    def least_prior(c,b):
        m = min(list(map(lambda x:len(x),c)))
        lp=[i[0] for i in (list(filter(lambda t:len(t)==m , c)))]
        for i in list(map(lambda t:t[0:-1], lp)):
            if i in find_triad(b):
                if len(lp)==1:
                    lp.extend( min(list(filter(lambda x:len(x)>m,c))) )
                    lp.remove(lp[list(map(lambda t:t[0:-1], lp)).index(i)])
                else:
                    lp.remove(lp[list(map(lambda t:t[0:-1], lp)).index(i)])
        return lp
    def make_subsets(l,j):
        c=[]
        for i in range(len(l)-j+1):
            c.append(l[i:i+j])
        return c
    def check_if_win(b):
        c = close_by(b)
        winning_set=[]
        for i in c:
            if len(i)>2:
                c1 = make_subsets(i,3)
                for j in c1:
                    if check_sublist(j,sequenced_cards):
                        winning_set.append(j)
            if len(i)>3:
                c1 = make_subsets(i,4)
                for j in c1:
                    if check_sublist(j,sequenced_cards):
                        winning_set.append(j)
        k=find_triad(b)
        for i in k:
            d=[]
            for j in b:
                if j[0:-1] == i:
                    d.append(j)
            winning_set.append(d)
        check1=[]
        for i in winning_set:
            check1.extend(i)
        if len(least_prior(c,b))<2:
            check2 = b[0:b.index(least_prior(c,b)[0])]+b[b.index(least_prior(c,b)[0])+1:len(b)]
        else:
            check2 = b[:]
        # print(check1,check2)
        return len(winning_set)>4 and len(list(filter(lambda i:len(i)==4,winning_set)))>0 and len(list(filter(lambda i:len(i)==3,winning_set)))>2 and set(check1).intersection(set(check2))==set(check2) 

    sequenced_cards = []
    for i in cards:
        for j in suits:
            sequenced_cards.append(i+j)
    sequenced_cards = sorted(sequenced_cards, key = lambda t:t[-1])

    if check_if_win(b):
        return -1
    else:
        return least_prior(close_by(b),b)

#delete iske neeche ka
''' attenntionn '''
def make_a_easy(a):
    sequenced_cards = []
    for i in cards:
        for j in suits:
            sequenced_cards.append(i+j)
    sequenced_cards = sorted(sequenced_cards, key = lambda t:t[-1])
    def sort_by_value(l): 
            n = len(l)  
            for i in range(n): 
                flag = 0
                for j in range(0, n-i-1): 
                    if cards.index(l[j][0:-1]) > cards.index(l[j+1][0:-1]) : 
                        l[j], l[j+1] = l[j+1], l[j] 
                        flag = 1
                if flag == 0:
                    break
            return l
    def form_d(b):
        b =sorted(b, key = lambda t:t[-1])
        c=[]
        j=0
        for i in range(len(b)-1):
            if b[i][-1]!=b[i+1][-1]:
                c.append(b[j:i+1])
                j=i+1
        c.append(b[j:len(b)])
        for i in range(len(c)):
            c[i] = sort_by_value(c[i])
        d=[]
        for i in c:
            d.extend(i)
        return d
    def close_by(b):
        d = form_d(b)
        c=[]
        j=0
        for i in range(len(d)-1):
            if abs(sequenced_cards.index(d[i])-sequenced_cards.index(d[i+1]))>3 and d[i][-1]==d[i+1][-1]:
                c.append(d[j:i+1])
                j=i+1
            if d[i][-1]!=d[i+1][-1]:
                c.append(d[j:i+1])
                j=i+1
        c.append(d[j:len(d)])
        # print(c)
        return c
    y = close_by(a)
    a=[]
    # print(y)
    for i in y:
        a.extend(i)
    return a

def change_for_user(e,middle):
    global a
    global left_cards
    global b
    a,left_cards,middle = swap(a,left_cards,e,middle)
    print(a,left_cards,middle)
    a = make_a_easy(a)
    ls = move_comp(b)
    k,l,m = swap_not_inplace(b,left_cards,e,middle)
    print(b,left_cards,middle)
    print(k,l,m)
    n = move_comp(k)
    print(ls,n)
    if n == -1:
        x=20
        y=5
        b = make_a_easy(b)
        for i in b:
            background.blit(deck[i],(x,y))
            x+=90
        text = font.render('Computer Win', True, (255,255,255))
        background.blit(text,(700,600)) 
        p.display.update()
    else:
        if len(n)<len(ls):
            if n[0] == middle:
                b,left_cards,middle = swap(b,left_cards,f_key[b.index(ls[0])],middle)
            else:
                b,left_cards,middle = swap(b,left_cards,f_key[b.index(n[0])],middle)
                print(b,left_cards,middle,'*')
                background.blit(font.render('Computer choose the card thrown by you', True, (255,255,255)),(400,600))
                p.display.update() 
                p.time.delay(s)
                disp(middle)
        else:
            middle = update_game()
            b,left_cards,middle = swap(b,left_cards,f_key[b.index(ls[0])],middle) 
            print(a,left_cards,middle,'*')
            background.blit(font.render('Computer choose a new card', True, (255,255,255)),(500,600)) 
            p.display.update()
            p.time.delay(s)
            disp(middle)
    return middle

background=p.display.set_mode((1400,700))
p.display.set_caption('Rummy')
cards=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits=['D','C','S','H']
deck={}
for i in cards:
    for j in suits:
        deck[i+j] = p.image.load('PNG\\'+i+j+'.png')
        deck[i+j] = p.transform.scale(deck[i+j], (86, 132))

d_key = {}
f_key = [p.K_q, p.K_w, p.K_e, p.K_r, p.K_t, p.K_y, p.K_u, p.K_i, p.K_o, p.K_p, p.K_a, p.K_s, p.K_d,p.K_f]
font = p.font.Font('Montserrat-Regular.ttf', 30)
for i in f_key:
    d_key[i] = font.render(p.key.name(i), True, (255,255,255))
middle_card = p.K_x
side_mid = p.K_v
you_win = p.K_z

left_cards = []
for i in cards:
    for j in suits:
        left_cards.append(i+j)
a=[]
b=[]
for i in range(14):
    m = random.randint(0,len(left_cards)-1)
    k = left_cards[m]
    a.append(k)
    left_cards.remove(k)
for i in range(14):
    m=random.randint(0,len(left_cards)-1)
    k=left_cards[m]
    b.append(k)
    left_cards.remove(k)

back = p.image.load('PNG\\purple_back.png')
back = p.transform.scale(back, (86, 132))
ls = move_comp(b)
if ls == -1:
    x=20
    y=5
    b = make_a_easy(b)
    for i in b:
        background.blit(deck[i],(x,y))
        x+=90
    text = font.render('Computer Win', True, (255,255,255))
    background.blit(text,(700,600)) 
    p.display.update()  
 
s = 1500
count = 0
playing = True
middle = update_game()
a  = make_a_easy(a)
print(a)

if __name__ == '__main__':
    while playing :
        disp(middle)
        for event in p.event.get():
            if event.type == p.KEYUP:
                if event.key not in f_key and event.key!=middle_card and event.key != p.K_v and event.key != p.K_z:
                    background.blit(font.render('Invalid input', True, (255,255,255)),(600,600))
                    p.display.update()
                    p.time.delay(s)
                    disp(middle)
                else:
                    disp(middle)
                    count +=1
                    print(count) 
                    if count % 2 == 0:
                        if inkey == p.K_x:
                            middle = change_for_user(event.key,middle)
                        elif inkey == p.K_v:
                            middle = update_game()
                            middle = change_for_user(event.key,middle)
                        elif inkey == you_win:
                            n = move_comp(a)
                            if n == -1:
                                background.blit(font.render('You win, congratulations', True, (255,255,255)),(500,600))
                                p.display.update()
                                p.time.delay(5000)
                                quit()
                            else:
                                background.blit(font.render('Oops, looks like you have not made the right sequences', True, (255,255,255)),(300,600))
                                p.display.update()
                                p.time.delay(s)
                                disp(middle)
                        elif event.key in f_key:
                            a[f_key.index(event.key)],a[f_key.index(inkey)] = a[f_key.index(inkey)],a[f_key.index(event.key)]
                        else:
                            count-=2
                            text = font.render('Invalid input', True, (255,255,255))
                            background.blit(text,(600,600))
                            p.display.update()
                            p.time.delay(s)
                    else:
                        if event.key in f_key or event.key == p.K_x or event.key == p.K_v or event.key == p.K_z:
                            inkey = event.key
                # update_game()
                p.display.update()
            
            else:
                if event.type == p.QUIT:
                    p.quit()
                    quit()