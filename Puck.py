import mechanize
import facebook
import time
 
# Browser
br = mechanize.Browser()
 
 
 
# Browser settings
br.set_handle_equiv( True )
br.set_handle_gzip( True )
br.set_handle_redirect( True )
br.set_handle_referer( True )
br.set_handle_robots( False )
 
 
br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 )
 
br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]
br.open("https://www.facebook.com/messages/t/")
br.geturl()
 
print ("[+] UNKNOWN [+]")
print ("[+] by UNKNOWN [+]")
msg=str(input("Enter your Token : "))
poct=str(input("Enter your post Link : "))
npl=str(input(" Enter your np last line :  "))
aa= "[[SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 ______________ [[ .. :|] <3 .. DushMano  :|] <3 ko ..  :|] <3 Saja  :|] <3 Dene ..  :|] <3 Kii  :|] <3 Ek ..  :|] <3 Tehjeeb  :|] <3 Haii ..  :|] <3 Merii  :|] <3 Maiin ..  :|] <3 Hath  :|] <3 Nhii ..  :|] <3 Uthata  :|] <3 bs ..  :|] <3 Najro  :|] <3 Se ..  :|] <3 Giira  :|] <3 Deta ..  :|] <3 Hu  :|] <3 ____________[[(^^^)  :|] :O ..  :|] :3 ..  :|] <3 .. (Y)"
 
 
ss= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 ______________ [[ .. :|] <3 .. Aksar  :|] <3 Wohii ..  :|] <3 Log  :|] <3 .. Uthhate  :|] <3 Haiin ..  :|] <3 hum  :|] <3 Par ..  :|] <3 UngliiYan  :|] <3 Jiinkii ..  :|] <3 humeiin  :|] <3 Chhune ..  :|] <3 Kii  :|] <3 Aukat ..  :|] <3 Nahii  :|] <3 Hotii ..  :|] <3 _______________ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
dd="SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 ______________ [[ .. :|] <3 Toofan  :|] <3 Bhii ..  :|] <3 Aana  :|] <3 Jrurii ..  :|] <3 Haii  :|] <3 JiindGii ..  :|] <3 Me  :|] <3 Tab ..  :|] <3 Jaakr  :|] <3 Pata ..  :|] <3 Chlta  :|] <3 Haii ..  :|] <3 Kii  :|] <3 Kon .. Haath ..  :|] <3 Chudakar  :|] <3 Bhagta ..  :|] <3 Haii  :|] <3 Aur ..  :|] <3 Kon  :|] <3 .. Haath  :|] <3 Pakadkar  :|] <3 .. Bhagta  :|] <3 Haii  :|] <3_____________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
ff= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3______________ [[ .. :|] <3 .. Abhii  :|] <3 To  :|] <3 .. Hum  :|] <3 Maiidan ..  :|] <3 Me  :|] <3 Utare ..  :|] <3 Bhii  :|] <3 Nhii ..  :|] <3 Aur  :|] <3 Logo  :|] <3 .. Ne  :|] <3 Hamare  :|] <3 Charche ..  :|] <3 Suru  :|] <3 Kar ..  :|] <3 Diiye  :|] <3 .. _____________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
gg= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 ______________ [[ .. :|] <3 .. Peene  :|] <3 piilane ..  :|] <3 Kii  :|] <3Kya ..  :|] <3 Bat  :|] <3 Karte ..  :|] <3 Ho  :|] <3 Kabhii ..  :|] <3 Hum  :|] <3 Bhii ..  :|] <3 Piiya  :|] <3 Karte ..  :|] <3 The  :|] <3 Jiitnii ..  :|] <3 Tum  :|] <3 Jam ..  :|] <3 Me  :|] <3 Liiye ..  :|] <3 baiithe  :|] <3 Ho ..  :|] <3 Utnii  :|] <3Hum ..  :|] <3 paiimaane :|] <3 Me ..  :|] <3 chhodh  :|] <3 Diiya ..  :|] <3 karte  :|] <3 The ..  :|] <3 _______________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
hh= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 ______________ [[ .. :|] <3 .. DushMano :|] <3 ko .. :|] <3 Saja :|] <3 Dene .. :|] <3 Kii :|] <3 Ek .. :|] <3 Tehjeeb :|] <3 Haii .. :|] <3 Merii :|] <3 Maiin .. :|] <3 Hath :|] <3 Nhii .. :|] <3 Uthata :|] <3 bs .. :|] <3 Najro :|] <3 Se .. :|] <3 Giira :|] <3 Deta .. :|] <3 Hu :|] <3 ____________ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
jj= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 ______________ [[ .. :|] <3 Na :|] <3 Peshii :|] <3 .. Hogii :|] <3 Na :|] <3 .. Gwaah :|] <3 hoga :|] <3 .. Ab :|] <3 Jo :|] <3 .. Hum :|] <3 Se .. :|] <3 Uljega :|] <3 Bs .. :|] <3 Siidha :|] <3 Tbaah .. :|] <3 Hoga :|] <3 .. ___________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
kk= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 ______________ [[ .. :|] <3 Jeet :|] <3 Aur .. :|] <3 Haar :|] <3 Aapkii .. :|] <3 Soch :|] <3 Par .. :|] <3 Hi :|] <3 Niirbhr .. :|] <3 Krtii :|] <3 haii .. :|] <3 Maan :|] <3 Lo .. :|] <3 To :|] <3 Haar .. :|] <3 Gye :|] <3 Aur .. :|] <3 Than :|] <3 Lo .. :|] <3 To :|] <3 Jeet .. :|] <3 Gye :|] <3 _________________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
ll= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 ______________ [[ .. :|] <3 Badshah :|] <3 kii .. :|] <3 Galii :|] <3 Maiin .. :|] <3 Aake :|] <3 .. Uska :|] <3 Pata .. :|] <3 Nhii :|] <3 .. Poochte :|] <3 Ghulamo .. :|] <3 Ke :|] <3 Jhuke .. :|] <3 Huye :|] <3 sarr .. :|] <3 Khud :|] <3 ba .. :|] <3 khud :|] <3 Raasta .. :|] <3 Bata :|] <3 .. Dete :|] <3 Haii .. :|] <3 _________________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
zz= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 ______________ [[ ..  :|] <3 Agar :|] <3 .. Lagta :|] <3 Haii :|] <3 .. Tumhe :|] <3 Galat .. :|] <3 Hoon :|] <3 Maiin .. :|] <3 To :|] <3 Sahii :|] <3 .. Ho :|] <3 Tum :|] <3 .. Thoda :|] <3 Alag .. :|] <3 Hoon :|] <3 .. Maiin :|] <3 .. _______________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
xx= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 _______________ [[ .. :|] <3 .. Lahro :|] <3 Ko :|] <3 .. khamosh :|] <3 Dekhkar .. :|] <3 YE :|] <3 Na :|] <3 .. Smjana :|] <3 Kii  :|] <3 .. Smundar :|] <3 Me .. :|] <3 Lehre :|] <3 Nhii .. :|] <3 Haii :|] <3 Hum .. :|] <3 Jab :|] <3 Bhii .. :|] <3 Uthege :|] <3 Toofan .. :|] <3 Bnkar :|] <3 Uthege :|] <3 .. Bs :|] <3 Uthne :|] <3 Kii :|] <3 .. Abhii :|] <3 Thanii :|] <3 .. Nhii :|] <3 Haii :|] <3 .. ____________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
cc= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 ________________ [[ .. :|] <3 .. Attiitude :|] <3 ka .. :|] <3 Andaza :|] <3 Yahii .. :|] <3 Se :|] <3 laga .. :|] <3 Lo :|] <3 Tum .. :|] <3 Player :|] <3 Banna .. :|] <3 chahte :|] <3 .. Ho :|] <3 Aur .. :|] <3 Maiin  :|] <3 Game .. :|] <3 Changer :|] <3 ______________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
vv= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 _______________ [[  .. :|] <3 Toofan  :|] <3 Bhii ..  :|] <3 Aana  :|] <3 Jarurii ..  :|] <3 Haii  :|] <3 JiindGii ..  :|] <3 Me  :|] <3 Tab ..  :|] <3Jaakr  :|] <3 Pata ..  :|] <3 Chlta  :|] <3 Haii ..  :|] <3 Kii  :|] <3 Kon .. Haath ..  :|] <3 Chudakar  :|] <3 Bhagta ..  :|] <3 Haii  :|] <3 Aur ..  :|] <3Kon  :|] <3 .. Haath  :|] <3 Pakadkar  :|] <3 .. Bhagta  :|] <3 Haii  :|] <3_____________ [[ #[[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
bb= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 _______________ [[ .. :|] <3 DushMAn :|] <3 Bola .. :|] <3 Mahangii :|] <3 .. Padegii :|] <3 Tujhe .. :|] <3 Ye :|] <3 DushManii .. :|] <3 Maiine :|] <3 .. Bola :|] <3 SasTii .. :|] <3 To :|] <3 Maiin .. :|] <3 Shraab :|] <3 Bhii .. :|] <3 Nhii :|] <3 Peeta .. :|] <3 ______________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
nn= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 _______________ [[ .. :|] <3 .. Peene :|] <3 Piilane .. :|] <3 Kii :|] <3 Kya .. :|] <3 Bat :|] <3 Karte .. :|] <3 Ho :|] <3 Kabhii .. :|] <3 Hum :|] <3 Bhii .. :|] <3 Piiya :|] <3 Karte .. :|] <3 The :|] <3 Jiitnii .. :|] <3 Tum :|] <3 Jam .. :|] <3 Me :|] <3 Liiye .. :|] <3 baiithe :|] <3 Ho .. :|] <3 Utnii :|] <3 Hum .. :|] <3 Paiimaane :|] <3 Me .. :|] <3 Chhodh :|] <3 Diiya .. :|] <3 Karte :|] <3 The .. :|] <3 _______________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
mm= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 _______________ [[  .. :|] <3 Hum ..  :|] <3  to ..  :|] <3 Diil ..  :|] <3 Ke ..  :|] <3 Badshah ..  :|] <3  Haiin ..  :|] <3 Jo ..  :|] <3 Sunte ..  :|] <3 bhii ..  :|] <3 Diil ..  :|] <3 Kii ..  :|] <3 Haiin ..  :|] <3 Or ..  :|] <3 Krte ..  :|] <3 Bhii ..  :|] <3 Diil ..  :|] <3 Kii ..  :|] <3 Haii :|] <3_____________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
ww= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 _______________ [[  .. :|] <3 Humse ..  :|] <3 Ladne ..  :|] <3 Wale ..  :|] <3  Bhii ..  :|] <3 Kamaal ..  :|] <3 Ke ..  :|] <3 Hote ..  :|] <3 Haiin ..  :|] <3 Post ..  :|] <3 To ..  :|] <3 Khud ..  :|] <3 Kii ..  :|] <3 Hotii ..  :|] <3 Haiin ..  :|] <3 Par ..  :|] <3 Charche ..  :|] <3 Hamare ..  :|] <3 Hote ..  :|] <3 Haiin :|] <3_____________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
ee= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 _______________ [[  .. :|] <3 IInsaan ..  :|] <3 Siirf ..  :|] <3 Aag ..  :|] <3 Se ..  :|] <3 Nhii Jalta ..  :|] <3 kuch ..  :|] <3 log ..  :|] <3 to ..  :|] <3 RaaWaan ..  :|] <3 Andaaj ..  :|] <3 Se ..  :|] <3 Jal ..  :|] <3 Jaate ..  :|] <3 Haiin :|] <3_____________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
tt= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 _______________ [[  .. :|] <3 Jiindagii ..  :|] <3 Jeete ..  :|] <3 Haii ..  :|] <3 Hum ..  :|] <3 Shaan ..  :|] <3 Se ..  :|] <3 Tabhii ..  :|] <3 To ..  :|] <3 Dushman ..  :|] <3 Jalte ..  :|] <3 Haiin ..  :|] <3 RaaWaaN ..  :|] <3 Ke ..  :|] <3 Naam ..  :|] <3 Se :|] <3_____________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
yy= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 _______________ [[ .. :|] <3 RaaWaaN :|] <3  ..  :|] <3 Jaanta ..  :|] <3 Haii ..  :|] <3 Khaan ..  :|] <3 Tak ..  :|] <3 Udaan ..  :|] <3 Haii ..  :|] <3 Unkii ..  :|] <3 Mere ..  :|] <3 Hii ..  :|] <3 Haath ..  :|] <3 Se ..  :|] <3 Niikle ..  :|] <3 Huye ..  :|] <3 Pariinde ..  :|] <3 Haiin :|] <3_____________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
op= "SR:) <([[) :P __ :D :|] <3 ___ SR:) :|] <3 _______________ [[  .. :|] <3 Sear ..  :|] <3 Ko ..  :|] <3 Jaagnaa ..  :|] <3 Or ..  :|] <3 Hume ..  :|] <3 Sulanaa ..  :|] <3 Kiisii ..  :|] <3 Ke ..  :|] <3 Bas ..  :|] <3 Kii ..  :|] <3 Baat ..  :|] <3 Nhii :|] <3_____________ [[ [[ (^^^) (Y) ..  SR:) (^^^) :3 ..  : <3 .. (Y)"
 
 
 
 
 
 
token=msg
def auto_messages():
 
 while True:
    graph = facebook.GraphAPI(access_token=token,version='2.8')
    
    graph.put_object(parent_object= poct, connection_name='messages',message=aa+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    
    graph.put_object(parent_object=poct, connection_name='messages',message=ss+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    graph.put_object(parent_object=poct, connection_name='messages',message=dd+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    graph.put_object(parent_object=poct, connection_name='messages',message=ff+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    graph.put_object(parent_object= poct, connection_name='messages',message=gg+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    
    graph.put_object(parent_object=poct, connection_name='messages',message=hh+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    graph.put_object(parent_object=poct, connection_name='messages',message=jj+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    graph.put_object(parent_object=poct, connection_name='messages',message=kk+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    graph.put_object(parent_object= poct, connection_name='messages',message=ll+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    
    graph.put_object(parent_object=poct, connection_name='messages',message=zz+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    graph.put_object(parent_object=poct, connection_name='messages',message=xx+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    graph.put_object(parent_object=poct, connection_name='messages',message=cc+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    graph.put_object(parent_object= poct, connection_name='messages',message=vv+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    
    graph.put_object(parent_object=poct, connection_name='messages',message=bb+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    graph.put_object(parent_object=poct, connection_name='messages',message=nn+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    graph.put_object(parent_object=poct, connection_name='messages',message=mm+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    graph.put_object(parent_object= poct, connection_name='messages',message=ww+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    
    graph.put_object(parent_object=poct, connection_name='messages',message=ee+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    graph.put_object(parent_object=poct, connection_name='messages',message=tt+npl)
    print ("message send done =d!\n")
    time.sleep(200)
    graph.put_object(parent_object=poct, connection_name='messages',message=yy+npl)
    print ("message send done =d!\n")
    time.sleep(200)
 
    
if __name__ == '__main__':
    auto_messages()
    print ("message send done =d!\n")
#Code agar copy krte ho to nam mt htana made by sachin
 
