import random
top = ['블라우스', '맨투맨', '셔츠', '크롭티', '목티', '후드티', '니트']
pants = ['청바지','슬랙스','트레이닝바지','롱스커트','미니스커트','반바지','레깅스']

def gola(select,tp):
    answer=input('저희가 고객님한테 어울리는 %s를 추천드릴까요?(yes or no) : '%(tp))
    if answer=='yes':
        print(random.choice(select)+'(을)를 추천해요.')
        respond=input('마음에 드시나요?(네 or 아니요): ')
        if respond == '네':
            print('어머~ 고객님 너어무 잘 어울리신다~~ 완전 고객님꺼!!')
        else:
            print(select)
            n=int(input('그럼 이 중에서 몇 번째 옷이 마음에 드시나요?:'))
            print('고객님께서 '+ select[n-1] +'(을)를 고르셨네요')
    else:
       print(select)
       m=input('여기서 원하시는 옷이 있으신가요? ')
       for i in range(len(select)):
           if select[i] == m:
               print('%s는 %d번째에 있어요.' % (m, i+1))
           
print('어서오세요, 상명스토어입니다!')           
gola(top,'상의')
gola(pants,'하의')

tops = {'블라우스':12000, '맨투맨':10000, '셔츠':13000, '크롭티':5000, '목티':7000, '후드티':15000, '니트':18000}
pantss = {'청바지':10000,'슬랙스':12000,'트레이닝바지': 8000,'롱스커트':10000,'미니스커트':5000,'반바지':7000,'레깅스':6000}
s1=input('새 상품 가져다 드리려구요~ 고르신 상의 한번 더 말씀해주시겠어요?:')
s2=input('새 상품 가져다 드리려구요~ 고르신 하의 한번 더 말씀해주시겠어요?:')    
print('고객님께서 결제하실 가격은 총 %d원 입니다'%(tops[s1]+pantss[s2]))

