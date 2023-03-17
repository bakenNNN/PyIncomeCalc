'''made by rola'''
'''@ Po.Po.Hiv.'''
from asyncio.windows_events import NULL
from multiprocessing.connection import wait
import os
import pandas as pd
import PySimpleGUI as sg
import datetime
import psutil
import pickle
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase



working_directory_DBJSONdir = os.path.join(os.getcwd(), "FIREBASE_JSON.json") #dir a jsonhoz
cred = credentials.Certificate('./FIREBASE_JSON.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
firebase = firebase.FirebaseApplication('FIREBASE_URL', None)



vegeprogi=False
GRAPH_WIDTH = 120       # each individual graph size in pixels
GRAPH_HEIGHT = 40
TRANSPARENCY = 1      # how transparent the window looks. 0 = invisible, 1 = normal window
NUM_COLS = 4
POLL_FREQUENCY = 500    # how often to update graphs in milliseconds
txtwhile=0
verziovekt=[]
working_directory_versiondir = os.path.join(os.getcwd(), "Version.txt")

verzioszam=pd.read_csv(working_directory_versiondir, header=None)
while txtwhile<verzioszam[verzioszam.columns[0]].count():
    verziovekt.append(verzioszam.iloc[txtwhile,0])
    txtwhile+=1 
                 
txtwhile=0




colors = ('#23a0a0', '#56d856', '#be45be', '#5681d8', '#d34545', '#BE7C29')
working_directory_loadingdir = os.path.join(os.getcwd(), "data.pickle")

# DashGraph does the drawing of each graph
class ToltEsMent():
   def __init__(self, param):
        self.param = param
   def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("HIBA CURRENT STATE MENTESKOR (Possibly unsupported):", ex)
   def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("HIBA MEGLEVO MENTES TOLTESEKOR (Possibly unsupported):", ex)

class DashGraph(object):
    def __init__(self, graph_elem, text_elem, starting_count, color):
        self.graph_current_item = 0
        self.graph_elem = graph_elem        # type: sg.Graph
        self.text_elem = text_elem
        self.prev_value = starting_count
        self.max_sent = 1
        self.color = color
        # list of currently visible lines. Used to delete oild figures
        self.line_list = []

    def graph_percentage_abs(self, value):
        self.line_list.append(self.graph_elem.draw_line(            # draw a line and add to list of lines
                (self.graph_current_item, 0),
                (self.graph_current_item, value),
                color=self.color))
        if self.graph_current_item >= GRAPH_WIDTH:
            self.graph_elem.move(-1, 0)
            # delete the oldest line
            self.graph_elem.delete_figure(self.line_list[0])
            # remove line id from list of lines
            self.line_list = self.line_list[1:]
        else:
            self.graph_current_item += 1

    def text_display(self, text):
        self.text_elem.update(text)





savanyito=[]

def main():
    # A couple of "User defined elements" that combine several elements and enable bulk edits
    def Txt(text, **kwargs):
        return (sg.Text(text, font=('Helvetica 8'), **kwargs))

    def GraphColumn(name, key):
        return sg.Column([[Txt(name, size=(10, 1), key=key+'_TXT_'), ],
                    [sg.Graph((GRAPH_WIDTH, GRAPH_HEIGHT), (0, 0), (GRAPH_WIDTH, 100), background_color='black', key=key+'_GRAPH_')]], pad=(2, 2))

    num_cores = len(psutil.cpu_percent(percpu=True))
    verziotext='V.'+str(verziovekt[0])+' @PPH '+str(verziovekt[1])
    col_layout = [
     [sg.Text(size=(100, 0), font=('Helvetica', 10), key='-text2-')],
     [sg.Text(size=(100, 0), text='Jelenleg:')],
     [sg.Text(size=(100, 50), font=('Helvetica', 10), key='-text3-')]
     



  ]
   
    firstenter=True  
    layout = [[sg.T("")],
        [sg.Text("Táblázat: "), sg.Input(), sg.FileBrowse(
            button_text="Tallózás", key="-IN-")],
        [sg.Button("OK")],
        [sg.ProgressBar(609, orientation='h', size=(60, 40), border_width=4,
                        key='-PROGRESS_BAR-', bar_color=("Green", "Yellow"), pad=(20, 0))],
        [sg.Text(size=(15, 0), font=('Helvetica', 15),
                 justification='center', key='-text-', pad=(250, 0))],
        [sg.Column(col_layout, size=(200, 100),
                   element_justification='right', expand_x=True)],
        [sg.ProgressBar(35, orientation='h', size=(20, 5), border_width=4,
                        key='-PROGRESS_BAR2-', bar_color=("Green", "Yellow"), pad=(20, 50))],
        [sg.Text(pad=(0,150),text=verziotext)]                
 ]
    layout2=[]
   
    for rows in range(num_cores//NUM_COLS+1):
       layout2 += [[GraphColumn('CPU '+str(rows*NUM_COLS+cols), '_CPU_'+str(rows*NUM_COLS+cols)) for cols in range(min(num_cores-rows*NUM_COLS, NUM_COLS))]]
   












 




































    working_directory = os.getcwd()
    working_directory_txtdir = os.path.join(os.getcwd(), "Valtozok\\nullhetketto.txt")
    placeholdersuly=0
    placeholderosszeg=0
    txtwhile=0
    nullhetkettoelemek=[]
    nullharminckettoelemek=[]
    nullotelemek=[]
    kgelemek=[]
    befottelemek=[]
    lekvarelemek=[]
    voltteteljan=False
    volttetelfeb=False
    volttetelmar=False
    volttetelapr=False
    voltteteljun=False
    voltteteljul=False
    volttetelaug=False
    volttetelszep=False
    volttetelokt=False
    volttetelnov=False
    volttetelmaj=False
    voltteteldec=False
    paprikakremelemek=[]
    savanyukaposztaelemek=[]
    savanyusagelemek=[]
    szorpelemek=[]
    datumelemek=[]
    savanyito=[]
    kilenc=[]
    nullkettokettoelemek=[]
    kilencprint=''
    savanyitoprint=''
    excelfile_path= NULL














    februboolean=True
    marcboolean=True
    aprboolean=True
    majboolean=True
    junboolean=True
    julboolean=True
    augboolean=True
    szeptboolean=True
    jelenhonap=''
    oktboolean=True
    novboolean=True
    decboolean=True
    loading=True
    def liststring(savaoszlop):
        string =" "
        return(string.join(savaoszlop))

    sg.theme("DarkTeal2")

    classvektor=[]

    '''
    class termekekszamolasa(object):
        def __init__(self, valtozosuly):
        self.valtozosuly = valtozosuly


        def nullahetvenkettosuly(self):
        self.valtozosuly=self.valtozosuly*0.72
        
        return self.valtozosuly
    '''
    def nullahetvenkettosuly(valtozosuly):
        return valtozosuly*0.72
    def nullaharminchetsuly(valtozosuly):
        return valtozosuly*0.37
    def nullaotvensuly(valtozosuly):
        return valtozosuly*0.5
    def kgsuly(valtozosuly):
        return valtozosuly*1
    def nullkettoketsuly(valtozosuly):
        return valtozosuly*0.22

    placeholdersuly2=0
    placeholderosszeg2=0

    if os.path.exists(working_directory_loadingdir):
      toltottobj=ToltEsMent.load_object("data.pickle")
    
      layout4=toltottobj.param
      window3 = sg.Window('Időszaki Számoló', layout4, size=(1000,1500),resizable=True)
      graphs = [DashGraph(window3['_CPU_'+str(i)+'_GRAPH_'],
                                window3['_CPU_'+str(i) + '_TXT_'],
                                0, colors[i % 6]) for i in range(num_cores)]
      while True:
        events3,values3 = window3.read(timeout=POLL_FREQUENCY)
        stats = psutil.cpu_percent(percpu=True)
        if firstenter== True:
                    window3['__MINDENMAS'].update(visible=False) 
                    window3['__MINDENMASFeb'].update(visible=False)
                    window3['__MINDENMASMar'].update(visible=False)
                    window3['__MINDENMASApr'].update(visible=False)
                    window3['__MINDENMASMaj'].update(visible=False)
                    window3['__MINDENMASJun'].update(visible=False)
                    window3['__MINDENMASJul'].update(visible=False)
                    window3['__MINDENMASAug'].update(visible=False)
                    window3['__MINDENMASSzep'].update(visible=False)
                    window3['__MINDENMASOkt'].update(visible=False)
                    window3['__MINDENMASNov'].update(visible=False)
                    window3['__MINDENMASDec'].update(visible=False) 
                    window3['__SAVA'].update(visible=True)
                    window3['__SAVAFeb'].update(visible=True)
                    window3['__SAVAMar'].update(visible=True)
                    window3['__SAVAApr'].update(visible=True)
                    window3['__SAVAMaj'].update(visible=True)
                    window3['__SAVAJun'].update(visible=True)
                    window3['__SAVAJul'].update(visible=True)
                    window3['__SAVAAug'].update(visible=True)
                    window3['__SAVASzep'].update(visible=True)
                    window3['__SAVAOkt'].update(visible=True)
                    window3['__SAVANov'].update(visible=True)
                    window3['__SAVADec'].update(visible=True)
                    firstenter=False
        for i, util in enumerate(stats):
                    graphs[i].graph_percentage_abs(util)
                    graphs[i].text_display('{} CPU {:2.0f}'.format(i, util))
        if events3 == 'Savanyitó':
                    window3['__MINDENMAS'].update(visible=False) 
                    window3['__MINDENMASFeb'].update(visible=False)
                    window3['__MINDENMASMar'].update(visible=False)
                    window3['__MINDENMASApr'].update(visible=False)
                    window3['__MINDENMASMaj'].update(visible=False)
                    window3['__MINDENMASJun'].update(visible=False)
                    window3['__MINDENMASJul'].update(visible=False)
                    window3['__MINDENMASAug'].update(visible=False)
                    window3['__MINDENMASSzep'].update(visible=False)
                    window3['__MINDENMASOkt'].update(visible=False)
                    window3['__MINDENMASNov'].update(visible=False)
                    window3['__MINDENMASDec'].update(visible=False) 
                    window3['__SAVA'].update(visible=True)
                    window3['__SAVAFeb'].update(visible=True)
                    window3['__SAVAMar'].update(visible=True)
                    window3['__SAVAApr'].update(visible=True)
                    window3['__SAVAMaj'].update(visible=True)
                    window3['__SAVAJun'].update(visible=True)
                    window3['__SAVAJul'].update(visible=True)
                    window3['__SAVAAug'].update(visible=True)
                    window3['__SAVASzep'].update(visible=True)
                    window3['__SAVAOkt'].update(visible=True)
                    window3['__SAVANov'].update(visible=True)
                    window3['__SAVADec'].update(visible=True)
        if events3 == 'Egyéb':
                    window3['__SAVA'].update(visible=False)
                    window3['__SAVAFeb'].update(visible=False)
                    window3['__SAVAMar'].update(visible=False)
                    window3['__SAVAApr'].update(visible=False)
                    window3['__SAVAMaj'].update(visible=False)
                    window3['__SAVAJun'].update(visible=False)
                    window3['__SAVAJul'].update(visible=False)
                    window3['__SAVAAug'].update(visible=False)
                    window3['__SAVASzep'].update(visible=False)
                    window3['__SAVAOkt'].update(visible=False)
                    window3['__SAVANov'].update(visible=False)
                    window3['__SAVADec'].update(visible=False)
                    window3['__MINDENMAS'].update(visible=True) 
                    window3['__MINDENMASFeb'].update(visible=True)
                    window3['__MINDENMASMar'].update(visible=True)
                    window3['__MINDENMASApr'].update(visible=True)
                    window3['__MINDENMASMaj'].update(visible=True)
                    window3['__MINDENMASJun'].update(visible=True)
                    window3['__MINDENMASJul'].update(visible=True)
                    window3['__MINDENMASAug'].update(visible=True)
                    window3['__MINDENMASSzep'].update(visible=True)
                    window3['__MINDENMASOkt'].update(visible=True)
                    window3['__MINDENMASNov'].update(visible=True)
                    window3['__MINDENMASDec'].update(visible=True) 
        if events3 == sg.WIN_CLOSED or events3=="Exit":
                    
             
            quit()







    while True:
        window = sg.Window('Időszaki Számoló', layout, size=(1100,800),resizable=True)
        event, values = window.read()
        
        while loading==True:
            window['-PROGRESS_BAR2-'].update(visible=True)    
            nullhetketto = pd.read_csv(working_directory_txtdir, header=None)
            while txtwhile<nullhetketto[nullhetketto.columns[0]].count():
                nullhetkettoelemek.append(nullhetketto.iloc[txtwhile,0])
                txtwhile+=1
                window['-PROGRESS_BAR2-'].update(txtwhile+20)
            txtwhile=0
            working_directory_txtdir=''
            working_directory_txtdir = os.path.join(os.getcwd(), "Valtozok\\nullharmhet.txt")
            
            nullharmichet=pd.read_csv(working_directory_txtdir, header=None)
            while txtwhile<nullharmichet[nullharmichet.columns[0]].count():
                        nullharminckettoelemek.append(nullharmichet.iloc[txtwhile,0])
                        txtwhile+=1
                        window['-PROGRESS_BAR2-'].update(txtwhile+10)
            txtwhile=0
            working_directory_txtdir=''
            working_directory_txtdir = os.path.join(os.getcwd(), "Valtozok\\nullot.txt")
                        
            kg=pd.read_csv(working_directory_txtdir, header=None)
            while txtwhile<kg[kg.columns[0]].count():
                    kgelemek.append(kg.iloc[txtwhile,0])
                    txtwhile+=1
                    window['-PROGRESS_BAR2-'].update(txtwhile+20)
                    print(kgelemek)
            txtwhile=0
            working_directory_txtdir=''
            working_directory_txtdir = os.path.join(os.getcwd(), "Valtozok\\kg.txt")

            nullot=pd.read_csv(working_directory_txtdir, header=None)
            while txtwhile<nullot[kg.columns[0]].count():
                    nullotelemek.append(nullot.iloc[txtwhile,0])
                    txtwhile+=1
                    window['-PROGRESS_BAR2-'].update(txtwhile+10)
            txtwhile=0
            working_directory_txtdir=''
            working_directory_txtdir = os.path.join(os.getcwd(), "Valtozok\\befott.txt")

            befott=pd.read_csv(working_directory_txtdir, header=None)
            while txtwhile<befott[befott.columns[0]].count():
                    befottelemek.append(befott.iloc[txtwhile,0])
                    txtwhile+=1
                    window['-PROGRESS_BAR2-'].update(txtwhile+20)
            txtwhile=0
            working_directory_txtdir=''
            working_directory_txtdir = os.path.join(os.getcwd(), "Valtozok\\lekvar.txt")

            lekvar=pd.read_csv(working_directory_txtdir, header=None)
            while txtwhile<lekvar[lekvar.columns[0]].count():
                    lekvarelemek.append(lekvar.iloc[txtwhile,0])
                    txtwhile+=1
                    window['-PROGRESS_BAR2-'].update(txtwhile+10)
            txtwhile=0
            working_directory_txtdir=''
            working_directory_txtdir = os.path.join(os.getcwd(), "Valtozok\\paprikakrem.txt")

            paprikakrem=pd.read_csv(working_directory_txtdir, header=None)
            while txtwhile<paprikakrem[paprikakrem.columns[0]].count():
                    paprikakremelemek.append(paprikakrem.iloc[txtwhile,0])
                    txtwhile+=1
                    window['-PROGRESS_BAR2-'].update(txtwhile+20)
            txtwhile=0
            working_directory_txtdir=''
            working_directory_txtdir = os.path.join(os.getcwd(), "Valtozok\\savanyukap.txt")

            savanyukaposzta=pd.read_csv(working_directory_txtdir, header=None)
            while txtwhile<savanyukaposzta[savanyukaposzta.columns[0]].count():
                    savanyukaposztaelemek.append(savanyukaposzta.iloc[txtwhile,0])
                    txtwhile+=1
                    window['-PROGRESS_BAR2-'].update(txtwhile+10)
            txtwhile=0
            working_directory_txtdir=''
            working_directory_txtdir = os.path.join(os.getcwd(), "Valtozok\\savanyusag.txt")

            savanyusag=pd.read_csv(working_directory_txtdir, header=None)
            while txtwhile<savanyusag[savanyusag.columns[0]].count():
                    savanyusagelemek.append(savanyusag.iloc[txtwhile,0])
                    txtwhile+=1
                    window['-PROGRESS_BAR2-'].update(txtwhile+20)
            txtwhile=0
            working_directory_txtdir=''
            working_directory_txtdir = os.path.join(os.getcwd(), "Valtozok\\szorp.txt")
            
            szorp=pd.read_csv(working_directory_txtdir, header=None)
            while txtwhile<szorp[szorp.columns[0]].count():
                    szorpelemek.append(szorp.iloc[txtwhile,0])
                    txtwhile+=1 
                    window['-PROGRESS_BAR2-'].update(txtwhile+10)
            txtwhile=0
            working_directory_txtdir=''
            working_directory_txtdir = os.path.join(os.getcwd(), "Valtozok\\nullkettoketto.txt")
            
            nullketket=pd.read_csv(working_directory_txtdir, header=None)
            while txtwhile<nullketket[nullketket.columns[0]].count():
                    nullkettokettoelemek.append(nullketket.iloc[txtwhile,0])
                    txtwhile+=1 
                    window['-PROGRESS_BAR2-'].update(txtwhile+10)


            txtwhile=0
            working_directory_txtdir=''
            working_directory_txtdir = os.path.join(os.getcwd(), "Valtozok\\datum.txt")
            
            datumok=pd.read_csv(working_directory_txtdir, header=None)
            while txtwhile<datumok[datumok.columns[0]].count():
                        datumelemek.append(datumok.iloc[txtwhile,0])
                        txtwhile+=1
                        window['-PROGRESS_BAR2-'].update(txtwhile+10)   
            txtwhile=0
            working_directory_txtdir=''
            loading=False  
        window['-PROGRESS_BAR2-'].update(visible=False)                             
        SameDatumDifferentSzamla=False
        if event == sg.WIN_CLOSED or event=="Exit":
         break

        elif event == "OK":
            excelfile_path = values["-IN-"]
            
            df=pd.read_excel(excelfile_path)
            
            '''df.columns=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz',
            'aaa','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','iiii','iiiii','iiiiii','iiiiii','iiiiiiii','iiiiiiii','iiiiiiiii','iiiiiiiiiiii','iiai','iibi','iici',
            'idii','ieii','iifi','iigi','iihi','iiki','ijii','iili'
            ,'iimi','iini','ioii','ipii']'''
            print(savanyukaposztaelemek)
            print(paprikakremelemek)

            eredmenysuly072=0
            eredmenyosszeg072=0
            i=10
            a=0
            januarsorokszama=0
            februarsorokszama=0
            kilenc=[]
            
            janudatum=datetime.datetime(datumelemek[0],1,31)
            januelsodatum=datetime.datetime(datumelemek[0],2,1)
            februdatum=datetime.datetime(datumelemek[0],2,28)
            marcdatum=datetime.datetime(datumelemek[0],3,31)
            aprdatum=datetime.datetime(datumelemek[0],4,30)
            majdatum=datetime.datetime(datumelemek[0],5,31)
            jundatum=datetime.datetime(datumelemek[0],6,30)
            juldatum=datetime.datetime(datumelemek[0],7,31)
            augdatum=datetime.datetime(datumelemek[0],8,31)
            szepdatum=datetime.datetime(datumelemek[0],9,30)
            oktdatum=datetime.datetime(datumelemek[0],10,31)
            novdatum=datetime.datetime(datumelemek[0],11,30)
            decdatum=datetime.datetime(datumelemek[0],12,31)
            ba=0
            bb=0
            muv=0
            currentho=''
            currenthosor=12
            currenthooszlop=0
            colcount=7
            osszosorcount=0
            hulzevalt='...'
            osszosorcount2=0
            progval=0
            osszosorcount3=0
            nyolc=[]
            hat=""
            FebruKiir=""
            MarcKiir=""
            AprKiir=""
            MajKiir=""
            JunKiir=""
            JulKiir=""
            AugKiir=""
            SzeptKiir=""
            OktKiir=""
            NovKiir=""
            DecKiir=""
            harminc=[]
            negyven=[]
            otven=[]
            hatvan=[]
            hetven=[]
            nyolcvan=[]
            kilencven=[]
            szaz=[]
            szaztiz=[]
            szazhusz=[]
            szazharminc=[]
            elozoszamlaszamarray=[]
            husz=0
            tizenegy=[]
            harmincharom=[]
            negyvenharom=[]
            otvenharom=[]
            hatvanharom=[]
            hetvenharom=[]
            nyolcvanharom=[]
            kilencvenharom=[]
            szazharom=[]
            szaztizharom=[]
            szazhuszharom=[]
            szazharmincharom=[]
            tru=False
            savoszloprowcount=df[df.columns[2]].count()
            kovetkezoszam=1
            mostaniszam=0
            osseg=0
            ossegarray=[]
            elozodatumarray=[]
            kovidatumarray=[]
            
            janusuly=[]
            januosszeg=[]
            
            lekvvekt=[]
            paprikkvekt=[]
            befottvekt=[]
            savanvekt=[]
            savkapvekt=[]
            szorpvekt=[]
            paprkremsuly = 0
            paprkremosszeg=0
            lekvsuly=0
            lekvosszeg=0
            befsuly=0
            befosszeg=0
            savanysuly=0
            savanyosszeg=0
            savkapsuly=0
            savkaposszeg=0
            szorpsuly=0
            szorposszeg=0
            Voltsavanyitotetel=False
            lekvvektprint=''
            paprikkvektprint=''
            columnJan=[[sg.Text(' ')]]
            columnJan2=[[sg.Text(' ')]]
            columnFeb=[[sg.Text(' ')]]
            columnFeb2=[[sg.Text(' ')]]
            columnMarc=[[sg.Text(' ')]]
            columnMarc2=[[sg.Text(' ')]]
            columnApr=[[sg.Text(' ')]]
            columnApr2=[[sg.Text(' ')]]
            columnMaj=[[sg.Text(' ')]]
            columnMaj2=[[sg.Text(' ')]]
            columnJun=[[sg.Text(' ')]]
            columnJun2=[[sg.Text(' ')]]
            columnJul=[[sg.Text(' ')]]
            columnJul2=[[sg.Text(' ')]]
            columnAug=[[sg.Text(' ')]]
            columnAug2=[[sg.Text(' ')]]
            columnSzept=[[sg.Text(' ')]]
            columnSzep2=[[sg.Text(' ')]]
            columnOkt=[[sg.Text(' ')]]
            columnOkt2=[[sg.Text(' ')]]
            columnNov=[[sg.Text(' ')]]
            columnNov2=[[sg.Text(' ')]]
            columnDec=[[sg.Text(' ')]]
            columnDec2=[[sg.Text(' ')]]


           



            while osszosorcount3<500000:
                if df.iloc[osszosorcount3,2] == 'EndDec':
                    break
                osszosorcount3+=1
            
            while osszosorcount<500000:
                if df.iloc[osszosorcount,2] == 'EndDec':
                    break
                
                datum=df.iloc[osszosorcount,86]
                mostaniszam+=1
                while colcount < 87:
                    if colcount== 87:
                        break
                    tizenegy=''
                    harmincharom=''
                    negyvenharom=''
                    otvenharom=''
                    hatvanharom=''
                    hetvenharom=''
                    nyolcvanharom=''
                    kilencvenharom=''
                    szazharom=''
                    szaztizharom=''
                    szazhuszharom=''
                    szazharmincharom=''
                    while osszosorcount2<500000:
                        
                        if df.iloc[osszosorcount2,2] == 'EndDec':
                            break
                        else:
                            if df.iloc[osszosorcount2,colcount] ==datum:
                                mennyiseg=df.iloc[osszosorcount2,colcount-2]
                                termekara=df.iloc[osszosorcount2,colcount-1]
                                egyseg=df.iloc[osszosorcount2,colcount-3]
                                termek=df.iloc[osszosorcount2,colcount-4]
                                szamla=df.iloc[osszosorcount2,colcount+1]
                                datedatem=df.iloc[osszosorcount2,colcount]
                                def createTetelek():
                                 today = datetime.datetime.now()
                                 db.collection('BevetelProg').document('Tetelek').set(
                                 {
                                 'tetelnev': termek ,
                                 'darab': mennyiseg,
                                 'egyseg': egyseg,
                                 'termekara': termekara,
                                 'datum': datedatem,
                                 'szamla':szamla
                                 }
                                 )
                                def createOsszeg():
                                 db.collection('BevetelProg').document(jelenhonap).set(
                                 {
                                        'savanyito':savanyitoprint,
                                        'tetelek':kilencprint,
                                        'szamolas':lekvvektprint

                                 }     
                                 )

                                '''DEC'''
                                if datum>novdatum:
                                    if decboolean == True:
                                        #valtozok nullazasa elso belepeskor
                                        columnDec = [[sg.Text(' ', visible=True, key="__MINDENMASDec"), sg.Text(' ', key="__SAVADec",visible=False)]]
                                        savkapsuly=0
                                        jelenhonap='December'
                                        savkaposszeg=0
                                        szorpsuly=0
                                        szorposszeg=0
                                        savanysuly=0
                                        savanyosszeg=0
                                        befsuly=0
                                        befosszeg=0
                                        paprkremsuly=0
                                        paprkremosszeg=0
                                        lekvsuly =0
                                        lekvosszeg =0
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        lekvvekt=[]
                                        lekvvektprint=''
                                        paprikkvekt=[]
                                        paprikkvektprint=''
                                        befottvekt=[]
                                        befottvektprint=''
                                        savanvekt=[]
                                        savanvektprint=''
                                        savkapvekt=[]
                                        savkapvektprint=''
                                        szorpvekt=[]
                                        szorpvektprint=''
                                        decboolean=False
                                        kilencprint=''
                                        savanyitoprint=''
                                        tiz=''
                                        tizenegy=''
                                        tizenketto=''
                                        kilenc=[]
                                        savanyito=[]
                                    elozodatumarray.append(datum)
                                    elozoszamlaszamarray.append(szamla)
                                    datumdatum=elozodatumarray[0]
                                    szamlaszamla=elozoszamlaszamarray[0]
                                    tiz=str(df.iloc[osszosorcount2,colcount]).split(" ")
                                    # tetelek osszeadasa
                                    if datum == datumdatum:
                                        
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if Voltsavanyitotetel==True and szamlaszamla!=szamla:
                                                print("belep")
                                                SameDatumDifferentSzamla=True
                                    # datumvaltozas
                                    if datum!=datumdatum or SameDatumDifferentSzamla == True:
                                        datumsplit=str(elozodatumarray[0]).split(" ")
                                        if Voltsavanyitotetel==True:
                                            voltteteldec=True
                                            lekvvekt.append("===Lekvár===")
                                            lekvvekt.append("\n")
                                            lekvvekt.append(lekvsuly)
                                            lekvvekt.append(lekvosszeg)
                                            lekvvekt.append(datumsplit)
                                            lekvvekt.append(elozoszamlaszamarray[0])
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvektprint=str(lekvvekt)
                                            lekvvektprint=lekvvektprint.replace(r'\n','\n')
                                            
                                            paprikkvekt.append("===Paprikakrém===")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append(str(paprkremsuly))
                                            paprikkvekt.append(str(paprkremosszeg))
                                            paprikkvekt.append(datumsplit)
                                            paprikkvekt.append(str(elozoszamlaszamarray[0]))
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvektprint=str(paprikkvekt)
                                            paprikkvektprint=paprikkvektprint.replace(r'\n','\n')
                                            
                                            befottvekt.append("===Befőtt===")
                                            befottvekt.append("\n")
                                            befottvekt.append(befsuly)
                                            befottvekt.append(befosszeg)
                                            befottvekt.append(datumsplit)
                                            befottvekt.append(elozoszamlaszamarray[0])
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvektprint=str(befottvekt)
                                            befottvektprint=befottvektprint.replace(r'\n','\n')

                                            savanvekt.append("===Savanyúság===")
                                            savanvekt.append("\n")
                                            savanvekt.append(savanysuly)
                                            savanvekt.append(savanyosszeg)
                                            savanvekt.append(datumsplit)
                                            savanvekt.append(elozoszamlaszamarray[0])
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvektprint=str(savanvekt)
                                            savanvektprint=savanvektprint.replace(r'\n','\n')


                                            savkapvekt.append("===Savanyú Káposzta===")
                                            savkapvekt.append("\n")
                                            savkapvekt.append(savkapsuly)
                                            savkapvekt.append(savkaposszeg)
                                            savkapvekt.append(datumsplit)
                                            savkapvekt.append(elozoszamlaszamarray[0])
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvektprint=str(savkapvekt)
                                            savkapvektprint=savkapvektprint.replace(r'\n','\n')
                                            
                                            szorpvekt.append("===Szörp===")
                                            szorpvekt.append("\n")
                                            szorpvekt.append(szorpsuly)
                                            szorpvekt.append(szorposszeg)
                                            szorpvekt.append(datumsplit)
                                            szorpvekt.append(elozoszamlaszamarray[0])
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvektprint=str(szorpvekt)
                                            szorpvektprint=szorpvektprint.replace(r'\n','\n')


                                            savkapsuly=0
                                            savkaposszeg=0
                                            szorpsuly=0
                                            szorposszeg=0
                                            savanysuly=0
                                            savanyosszeg=0
                                            befsuly=0
                                            befosszeg=0
                                            paprkremsuly=0
                                            paprkremosszeg=0
                                            lekvsuly =0
                                            lekvosszeg =0
                                            lekvvektprint=lekvvektprint+paprikkvektprint+befottvektprint+savanvektprint+savkapvektprint+szorpvektprint
                                            columnDec2 = [[sg.Text(lekvvektprint)]]
                                                             
                                            
                                            
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        elozodatumarray.append(datum)
                                        elozoszamlaszamarray.append(szamla)
                                        Voltsavanyitotetel=False
                                        SameDatumDifferentSzamla=False





                                    if colcount == 6:
                                        savanyito.append('\n')
                                        savanyito.append(df.iloc[osszosorcount2,colcount+1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-2])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-3])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-4])
                                        savanyito.append('\n')
                                        savanyito.append('\n')
                                        savanyitoprint=str(savanyito)
                                        savanyitoprint= savanyitoprint.replace(r'\n','\n')   
                                    else:
                                        kilenc.append('\n')
                                        
                                        kilenc.append(df.iloc[osszosorcount2,colcount+1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-2])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-3])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-4])
                                        kilenc.append('\n')
                                        kilenc.append('\n')
                                        kilencprint=str(kilenc)
                                        kilencprint=kilencprint.replace(r'\n','\n')
                                    columnDec = [[sg.Text(kilencprint, visible=True, key="__MINDENMASDec"), sg.Text(savanyitoprint, key="__SAVADec",visible=False)]]
                                    createOsszeg()
                                    tizenketto=tiz[0]
                                
                                    
                                    if tizenegy != tizenketto:
                                        tizenegy=tiz[0]
                                        kilenc.append(tiz[0])
                                        savanyito.append(tiz[0])
                                
                                
                                    else:
                                        
                                        tizenegy=tizenketto
                                '''NOV'''
                                if datum>oktdatum and datum<=novdatum:
                                    if novboolean == True:
                                        #valtozok nullazasa elso belepeskor
                                        
                                        columnNov = [[sg.Text(' ', visible=True, key="__MINDENMASNov"), sg.Text(' ', key="__SAVANov",visible=False)]]
                                        savkapsuly=0
                                        jelenhonap='November'
                                        savkaposszeg=0
                                        szorpsuly=0
                                        szorposszeg=0
                                        savanysuly=0
                                        savanyosszeg=0
                                        befsuly=0
                                        befosszeg=0
                                        paprkremsuly=0
                                        paprkremosszeg=0
                                        lekvsuly =0
                                        lekvosszeg =0
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        lekvvekt=[]
                                        lekvvektprint=''
                                        paprikkvekt=[]
                                        paprikkvektprint=''
                                        befottvekt=[]
                                        befottvektprint=''
                                        savanvekt=[]
                                        savanvektprint=''
                                        savkapvekt=[]
                                        savkapvektprint=''
                                        szorpvekt=[]
                                        szorpvektprint=''
                                        novboolean=False
                                        kilencprint=''
                                        savanyitoprint=''
                                        tiz=''
                                        tizenegy=''
                                        tizenketto=''
                                        kilenc=[]
                                        savanyito=[]
                                    elozodatumarray.append(datum)
                                    elozoszamlaszamarray.append(szamla)
                                    datumdatum=elozodatumarray[0]
                                    szamlaszamla=elozoszamlaszamarray[0]
                                    tiz=str(df.iloc[osszosorcount2,colcount]).split(" ")
                                    # tetelek osszeadasa
                                    if datum == datumdatum:
                                        
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if Voltsavanyitotetel==True and szamlaszamla!=szamla:
                                                print("belep")
                                                SameDatumDifferentSzamla=True
                                    # datumvaltozas
                                    if datum!=datumdatum or SameDatumDifferentSzamla == True:
                                        datumsplit=str(elozodatumarray[0]).split(" ")
                                        if Voltsavanyitotetel==True:
                                            volttetelnov=True
                                            lekvvekt.append("===Lekvár===")
                                            lekvvekt.append("\n")
                                            lekvvekt.append(lekvsuly)
                                            lekvvekt.append(lekvosszeg)
                                            lekvvekt.append(datumsplit)
                                            lekvvekt.append(elozoszamlaszamarray[0])
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvektprint=str(lekvvekt)
                                            lekvvektprint=lekvvektprint.replace(r'\n','\n')
                                            
                                            paprikkvekt.append("===Paprikakrém===")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append(str(paprkremsuly))
                                            paprikkvekt.append(str(paprkremosszeg))
                                            paprikkvekt.append(datumsplit)
                                            paprikkvekt.append(str(elozoszamlaszamarray[0]))
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvektprint=str(paprikkvekt)
                                            paprikkvektprint=paprikkvektprint.replace(r'\n','\n')
                                            
                                            befottvekt.append("===Befőtt===")
                                            befottvekt.append("\n")
                                            befottvekt.append(befsuly)
                                            befottvekt.append(befosszeg)
                                            befottvekt.append(datumsplit)
                                            befottvekt.append(elozoszamlaszamarray[0])
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvektprint=str(befottvekt)
                                            befottvektprint=befottvektprint.replace(r'\n','\n')

                                            savanvekt.append("===Savanyúság===")
                                            savanvekt.append("\n")
                                            savanvekt.append(savanysuly)
                                            savanvekt.append(savanyosszeg)
                                            savanvekt.append(datumsplit)
                                            savanvekt.append(elozoszamlaszamarray[0])
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvektprint=str(savanvekt)
                                            savanvektprint=savanvektprint.replace(r'\n','\n')


                                            savkapvekt.append("===Savanyú Káposzta===")
                                            savkapvekt.append("\n")
                                            savkapvekt.append(savkapsuly)
                                            savkapvekt.append(savkaposszeg)
                                            savkapvekt.append(datumsplit)
                                            savkapvekt.append(elozoszamlaszamarray[0])
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvektprint=str(savkapvekt)
                                            savkapvektprint=savkapvektprint.replace(r'\n','\n')
                                            
                                            szorpvekt.append("===Szörp===")
                                            szorpvekt.append("\n")
                                            szorpvekt.append(szorpsuly)
                                            szorpvekt.append(szorposszeg)
                                            szorpvekt.append(datumsplit)
                                            szorpvekt.append(elozoszamlaszamarray[0])
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvektprint=str(szorpvekt)
                                            szorpvektprint=szorpvektprint.replace(r'\n','\n')


                                            savkapsuly=0
                                            savkaposszeg=0
                                            szorpsuly=0
                                            szorposszeg=0
                                            savanysuly=0
                                            savanyosszeg=0
                                            befsuly=0
                                            befosszeg=0
                                            paprkremsuly=0
                                            paprkremosszeg=0
                                            lekvsuly =0
                                            lekvosszeg =0
                                            lekvvektprint=lekvvektprint+paprikkvektprint+befottvektprint+savanvektprint+savkapvektprint+szorpvektprint
                                            columnNov2 = [[sg.Text(lekvvektprint)]]
                                                             
                                            
                                            
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        elozodatumarray.append(datum)
                                        elozoszamlaszamarray.append(szamla)
                                        Voltsavanyitotetel=False
                                        SameDatumDifferentSzamla=False





                                    if colcount == 6:
                                        savanyito.append('\n')
                                        savanyito.append(df.iloc[osszosorcount2,colcount+1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-2])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-3])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-4])
                                        savanyito.append('\n')
                                        savanyito.append('\n')
                                        savanyitoprint=str(savanyito)
                                        savanyitoprint= savanyitoprint.replace(r'\n','\n')   
                                    else:
                                        kilenc.append('\n')
                                        
                                        kilenc.append(df.iloc[osszosorcount2,colcount+1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-2])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-3])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-4])
                                        kilenc.append('\n')
                                        kilenc.append('\n')
                                        kilencprint=str(kilenc)
                                        kilencprint=kilencprint.replace(r'\n','\n')
                                    columnNov = [[sg.Text(kilencprint, visible=True, key="__MINDENMASNov"), sg.Text(savanyitoprint, key="__SAVANov",visible=False)]]
                                    createOsszeg()
                                    tizenketto=tiz[0]
                                
                                    
                                    if tizenegy != tizenketto:
                                        tizenegy=tiz[0]
                                        kilenc.append(tiz[0])
                                        savanyito.append(tiz[0])
                                
                                
                                    else:
                                        
                                        tizenegy=tizenketto
                                '''OKT'''
                                if datum>szepdatum and datum<=oktdatum:
                                    if oktboolean == True:
                                        #valtozok nullazasa elso belepeskor
                                        columnOkt = [[sg.Text(' ', visible=True, key="__MINDENMASOkt"), sg.Text(' ', key="__SAVAOkt",visible=False)]]
                                        savkapsuly=0
                                        jelenhonap='Oktober'
                                        savkaposszeg=0
                                        szorpsuly=0
                                        szorposszeg=0
                                        savanysuly=0
                                        savanyosszeg=0
                                        befsuly=0
                                        befosszeg=0
                                        paprkremsuly=0
                                        paprkremosszeg=0
                                        lekvsuly =0
                                        lekvosszeg =0
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        lekvvekt=[]
                                        lekvvektprint=''
                                        paprikkvekt=[]
                                        paprikkvektprint=''
                                        befottvekt=[]
                                        befottvektprint=''
                                        savanvekt=[]
                                        savanvektprint=''
                                        savkapvekt=[]
                                        savkapvektprint=''
                                        szorpvekt=[]
                                        szorpvektprint=''
                                        oktboolean=False
                                        kilencprint=''
                                        savanyitoprint=''
                                        tiz=''
                                        tizenegy=''
                                        tizenketto=''
                                        kilenc=[]
                                        savanyito=[]
                                    elozodatumarray.append(datum)
                                    elozoszamlaszamarray.append(szamla)
                                    datumdatum=elozodatumarray[0]
                                    szamlaszamla=elozoszamlaszamarray[0]
                                    tiz=str(df.iloc[osszosorcount2,colcount]).split(" ")
                                    # tetelek osszeadasa
                                    if datum == datumdatum:
                                        
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if Voltsavanyitotetel==True and szamlaszamla!=szamla:
                                                print("belep")
                                                SameDatumDifferentSzamla=True
                                    # datumvaltozas
                                    if datum!=datumdatum or SameDatumDifferentSzamla == True:
                                        datumsplit=str(elozodatumarray[0]).split(" ")
                                        if Voltsavanyitotetel==True:
                                            volttetelokt=True
                                            lekvvekt.append("===Lekvár===")
                                            lekvvekt.append("\n")
                                            lekvvekt.append(lekvsuly)
                                            lekvvekt.append(lekvosszeg)
                                            lekvvekt.append(datumsplit)
                                            lekvvekt.append(elozoszamlaszamarray[0])
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvektprint=str(lekvvekt)
                                            lekvvektprint=lekvvektprint.replace(r'\n','\n')
                                            
                                            paprikkvekt.append("===Paprikakrém===")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append(str(paprkremsuly))
                                            paprikkvekt.append(str(paprkremosszeg))
                                            paprikkvekt.append(datumsplit)
                                            paprikkvekt.append(str(elozoszamlaszamarray[0]))
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvektprint=str(paprikkvekt)
                                            paprikkvektprint=paprikkvektprint.replace(r'\n','\n')
                                            
                                            befottvekt.append("===Befőtt===")
                                            befottvekt.append("\n")
                                            befottvekt.append(befsuly)
                                            befottvekt.append(befosszeg)
                                            befottvekt.append(datumsplit)
                                            befottvekt.append(elozoszamlaszamarray[0])
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvektprint=str(befottvekt)
                                            befottvektprint=befottvektprint.replace(r'\n','\n')

                                            savanvekt.append("===Savanyúság===")
                                            savanvekt.append("\n")
                                            savanvekt.append(savanysuly)
                                            savanvekt.append(savanyosszeg)
                                            savanvekt.append(datumsplit)
                                            savanvekt.append(elozoszamlaszamarray[0])
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvektprint=str(savanvekt)
                                            savanvektprint=savanvektprint.replace(r'\n','\n')


                                            savkapvekt.append("===Savanyú Káposzta===")
                                            savkapvekt.append("\n")
                                            savkapvekt.append(savkapsuly)
                                            savkapvekt.append(savkaposszeg)
                                            savkapvekt.append(datumsplit)
                                            savkapvekt.append(elozoszamlaszamarray[0])
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvektprint=str(savkapvekt)
                                            savkapvektprint=savkapvektprint.replace(r'\n','\n')
                                            
                                            szorpvekt.append("===Szörp===")
                                            szorpvekt.append("\n")
                                            szorpvekt.append(szorpsuly)
                                            szorpvekt.append(szorposszeg)
                                            szorpvekt.append(datumsplit)
                                            szorpvekt.append(elozoszamlaszamarray[0])
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvektprint=str(szorpvekt)
                                            szorpvektprint=szorpvektprint.replace(r'\n','\n')


                                            savkapsuly=0
                                            savkaposszeg=0
                                            szorpsuly=0
                                            szorposszeg=0
                                            savanysuly=0
                                            savanyosszeg=0
                                            befsuly=0
                                            befosszeg=0
                                            paprkremsuly=0
                                            paprkremosszeg=0
                                            lekvsuly =0
                                            lekvosszeg =0
                                            lekvvektprint=lekvvektprint+paprikkvektprint+befottvektprint+savanvektprint+savkapvektprint+szorpvektprint
                                            columnOkt2 = [[sg.Text(lekvvektprint)]]
                                                             
                                            
                                            
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        elozodatumarray.append(datum)
                                        elozoszamlaszamarray.append(szamla)
                                        Voltsavanyitotetel=False
                                        SameDatumDifferentSzamla=False





                                    if colcount == 6:
                                        savanyito.append('\n')
                                        savanyito.append(df.iloc[osszosorcount2,colcount+1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-2])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-3])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-4])
                                        savanyito.append('\n')
                                        savanyito.append('\n')
                                        savanyitoprint=str(savanyito)
                                        savanyitoprint= savanyitoprint.replace(r'\n','\n')   
                                    else:
                                        kilenc.append('\n')
                                        
                                        kilenc.append(df.iloc[osszosorcount2,colcount+1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-2])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-3])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-4])
                                        kilenc.append('\n')
                                        kilenc.append('\n')
                                        kilencprint=str(kilenc)
                                        kilencprint=kilencprint.replace(r'\n','\n')
                                    columnOkt = [[sg.Text(kilencprint, visible=True, key="__MINDENMASOkt"), sg.Text(savanyitoprint, key="__SAVAOkt",visible=False)]]
                                    createOsszeg()
                                    tizenketto=tiz[0]
                                
                                    
                                    if tizenegy != tizenketto:
                                        tizenegy=tiz[0]
                                        kilenc.append(tiz[0])
                                        savanyito.append(tiz[0])
                                
                                
                                    else:
                                        
                                        tizenegy=tizenketto
                                '''SZEPT'''
                                if datum>augdatum and datum<=szepdatum:
                                    if szeptboolean == True:
                                        #valtozok nullazasa elso belepeskor
                                        columnSzept = [[sg.Text(' ', visible=True, key="__MINDENMASSzep"), sg.Text(' ', key="__SAVASzep",visible=False)]]
                                        savkapsuly=0
                                        jelenhonap='Szeptember'
                                        savkaposszeg=0
                                        szorpsuly=0
                                        szorposszeg=0
                                        savanysuly=0
                                        savanyosszeg=0
                                        befsuly=0
                                        befosszeg=0
                                        paprkremsuly=0
                                        paprkremosszeg=0
                                        lekvsuly =0
                                        lekvosszeg =0
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        lekvvekt=[]
                                        lekvvektprint=''
                                        paprikkvekt=[]
                                        paprikkvektprint=''
                                        befottvekt=[]
                                        befottvektprint=''
                                        savanvekt=[]
                                        savanvektprint=''
                                        savkapvekt=[]
                                        savkapvektprint=''
                                        szorpvekt=[]
                                        szorpvektprint=''
                                        szeptboolean=False
                                        kilencprint=''
                                        savanyitoprint=''
                                        tiz=''
                                        tizenegy=''
                                        tizenketto=''
                                        kilenc=[]
                                        savanyito=[]
                                    elozodatumarray.append(datum)
                                    elozoszamlaszamarray.append(szamla)
                                    datumdatum=elozodatumarray[0]
                                    szamlaszamla=elozoszamlaszamarray[0]
                                    tiz=str(df.iloc[osszosorcount2,colcount]).split(" ")
                                    # tetelek osszeadasa
                                    if datum == datumdatum:
                                        
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if Voltsavanyitotetel==True and szamlaszamla!=szamla:
                                                print("belep")
                                                SameDatumDifferentSzamla=True
                                    # datumvaltozas
                                    if datum!=datumdatum or SameDatumDifferentSzamla == True:
                                        datumsplit=str(elozodatumarray[0]).split(" ")
                                        if Voltsavanyitotetel==True:
                                            volttetelszep=True
                                            lekvvekt.append("===Lekvár===")
                                            lekvvekt.append("\n")
                                            lekvvekt.append(lekvsuly)
                                            lekvvekt.append(lekvosszeg)
                                            lekvvekt.append(datumsplit)
                                            lekvvekt.append(elozoszamlaszamarray[0])
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvektprint=str(lekvvekt)
                                            lekvvektprint=lekvvektprint.replace(r'\n','\n')
                                            
                                            paprikkvekt.append("===Paprikakrém===")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append(str(paprkremsuly))
                                            paprikkvekt.append(str(paprkremosszeg))
                                            paprikkvekt.append(datumsplit)
                                            paprikkvekt.append(str(elozoszamlaszamarray[0]))
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvektprint=str(paprikkvekt)
                                            paprikkvektprint=paprikkvektprint.replace(r'\n','\n')
                                            
                                            befottvekt.append("===Befőtt===")
                                            befottvekt.append("\n")
                                            befottvekt.append(befsuly)
                                            befottvekt.append(befosszeg)
                                            befottvekt.append(datumsplit)
                                            befottvekt.append(elozoszamlaszamarray[0])
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvektprint=str(befottvekt)
                                            befottvektprint=befottvektprint.replace(r'\n','\n')

                                            savanvekt.append("===Savanyúság===")
                                            savanvekt.append("\n")
                                            savanvekt.append(savanysuly)
                                            savanvekt.append(savanyosszeg)
                                            savanvekt.append(datumsplit)
                                            savanvekt.append(elozoszamlaszamarray[0])
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvektprint=str(savanvekt)
                                            savanvektprint=savanvektprint.replace(r'\n','\n')


                                            savkapvekt.append("===Savanyú Káposzta===")
                                            savkapvekt.append("\n")
                                            savkapvekt.append(savkapsuly)
                                            savkapvekt.append(savkaposszeg)
                                            savkapvekt.append(datumsplit)
                                            savkapvekt.append(elozoszamlaszamarray[0])
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvektprint=str(savkapvekt)
                                            savkapvektprint=savkapvektprint.replace(r'\n','\n')
                                            
                                            szorpvekt.append("===Szörp===")
                                            szorpvekt.append("\n")
                                            szorpvekt.append(szorpsuly)
                                            szorpvekt.append(szorposszeg)
                                            szorpvekt.append(datumsplit)
                                            szorpvekt.append(elozoszamlaszamarray[0])
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvektprint=str(szorpvekt)
                                            szorpvektprint=szorpvektprint.replace(r'\n','\n')


                                            savkapsuly=0
                                            savkaposszeg=0
                                            szorpsuly=0
                                            szorposszeg=0
                                            savanysuly=0
                                            savanyosszeg=0
                                            befsuly=0
                                            befosszeg=0
                                            paprkremsuly=0
                                            paprkremosszeg=0
                                            lekvsuly =0
                                            lekvosszeg =0
                                            lekvvektprint=lekvvektprint+paprikkvektprint+befottvektprint+savanvektprint+savkapvektprint+szorpvektprint
                                            columnSzep2 = [[sg.Text(lekvvektprint)]]
                                                             
                                            
                                            
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        elozodatumarray.append(datum)
                                        elozoszamlaszamarray.append(szamla)
                                        Voltsavanyitotetel=False
                                        SameDatumDifferentSzamla=False





                                    if colcount == 6:
                                        savanyito.append('\n')
                                        savanyito.append(df.iloc[osszosorcount2,colcount+1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-2])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-3])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-4])
                                        savanyito.append('\n')
                                        savanyito.append('\n')
                                        savanyitoprint=str(savanyito)
                                        savanyitoprint= savanyitoprint.replace(r'\n','\n')   
                                    else:
                                        kilenc.append('\n')
                                        
                                        kilenc.append(df.iloc[osszosorcount2,colcount+1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-2])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-3])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-4])
                                        kilenc.append('\n')
                                        kilenc.append('\n')
                                        kilencprint=str(kilenc)
                                        kilencprint=kilencprint.replace(r'\n','\n')
                                    columnSzept = [[sg.Text(kilencprint, visible=True, key="__MINDENMASSzep"), sg.Text(savanyitoprint, key="__SAVASzep",visible=False)]]
                                    createOsszeg()
                                    tizenketto=tiz[0]
                                
                                    
                                    if tizenegy != tizenketto:
                                        tizenegy=tiz[0]
                                        kilenc.append(tiz[0])
                                        savanyito.append(tiz[0])
                                
                                
                                    else:
                                        
                                        tizenegy=tizenketto
                                '''AUG'''
                                if datum>juldatum and datum<=augdatum:
                                    if augboolean == True:
                                        #valtozok nullazasa elso belepeskor
                                        columnAug = [[sg.Text(' ', visible=True, key="__MINDENMASAug"), sg.Text(' ', key="__SAVAAug",visible=False)]]
                                        savkapsuly=0
                                        jelenhonap='Augusztus'
                                        savkaposszeg=0
                                        szorpsuly=0
                                        szorposszeg=0
                                        savanysuly=0
                                        savanyosszeg=0
                                        befsuly=0
                                        befosszeg=0
                                        paprkremsuly=0
                                        paprkremosszeg=0
                                        lekvsuly =0
                                        lekvosszeg =0
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        lekvvekt=[]
                                        lekvvektprint=''
                                        paprikkvekt=[]
                                        paprikkvektprint=''
                                        befottvekt=[]
                                        befottvektprint=''
                                        savanvekt=[]
                                        savanvektprint=''
                                        savkapvekt=[]
                                        savkapvektprint=''
                                        szorpvekt=[]
                                        szorpvektprint=''
                                        augboolean=False
                                        kilencprint=''
                                        savanyitoprint=''
                                        tiz=''
                                        tizenegy=''
                                        tizenketto=''
                                        kilenc=[]
                                        savanyito=[]
                                    elozodatumarray.append(datum)
                                    elozoszamlaszamarray.append(szamla)
                                    datumdatum=elozodatumarray[0]
                                    szamlaszamla=elozoszamlaszamarray[0]
                                    tiz=str(df.iloc[osszosorcount2,colcount]).split(" ")
                                    # tetelek osszeadasa
                                    if datum == datumdatum:
                                        
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if Voltsavanyitotetel==True and szamlaszamla!=szamla:
                                                print("belep")
                                                SameDatumDifferentSzamla=True
                                    # datumvaltozas
                                    if datum!=datumdatum or SameDatumDifferentSzamla == True:
                                        datumsplit=str(elozodatumarray[0]).split(" ")
                                        if Voltsavanyitotetel==True:
                                            volttetelaug=True
                                            lekvvekt.append("===Lekvár===")
                                            lekvvekt.append("\n")
                                            lekvvekt.append(lekvsuly)
                                            lekvvekt.append(lekvosszeg)
                                            lekvvekt.append(datumsplit)
                                            lekvvekt.append(elozoszamlaszamarray[0])
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvektprint=str(lekvvekt)
                                            lekvvektprint=lekvvektprint.replace(r'\n','\n')
                                            
                                            paprikkvekt.append("===Paprikakrém===")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append(str(paprkremsuly))
                                            paprikkvekt.append(str(paprkremosszeg))
                                            paprikkvekt.append(datumsplit)
                                            paprikkvekt.append(str(elozoszamlaszamarray[0]))
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvektprint=str(paprikkvekt)
                                            paprikkvektprint=paprikkvektprint.replace(r'\n','\n')
                                            
                                            befottvekt.append("===Befőtt===")
                                            befottvekt.append("\n")
                                            befottvekt.append(befsuly)
                                            befottvekt.append(befosszeg)
                                            befottvekt.append(datumsplit)
                                            befottvekt.append(elozoszamlaszamarray[0])
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvektprint=str(befottvekt)
                                            befottvektprint=befottvektprint.replace(r'\n','\n')

                                            savanvekt.append("===Savanyúság===")
                                            savanvekt.append("\n")
                                            savanvekt.append(savanysuly)
                                            savanvekt.append(savanyosszeg)
                                            savanvekt.append(datumsplit)
                                            savanvekt.append(elozoszamlaszamarray[0])
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvektprint=str(savanvekt)
                                            savanvektprint=savanvektprint.replace(r'\n','\n')


                                            savkapvekt.append("===Savanyú Káposzta===")
                                            savkapvekt.append("\n")
                                            savkapvekt.append(savkapsuly)
                                            savkapvekt.append(savkaposszeg)
                                            savkapvekt.append(datumsplit)
                                            savkapvekt.append(elozoszamlaszamarray[0])
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvektprint=str(savkapvekt)
                                            savkapvektprint=savkapvektprint.replace(r'\n','\n')
                                            
                                            szorpvekt.append("===Szörp===")
                                            szorpvekt.append("\n")
                                            szorpvekt.append(szorpsuly)
                                            szorpvekt.append(szorposszeg)
                                            szorpvekt.append(datumsplit)
                                            szorpvekt.append(elozoszamlaszamarray[0])
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvektprint=str(szorpvekt)
                                            szorpvektprint=szorpvektprint.replace(r'\n','\n')


                                            savkapsuly=0
                                            savkaposszeg=0
                                            szorpsuly=0
                                            szorposszeg=0
                                            savanysuly=0
                                            savanyosszeg=0
                                            befsuly=0
                                            befosszeg=0
                                            paprkremsuly=0
                                            paprkremosszeg=0
                                            lekvsuly =0
                                            lekvosszeg =0
                                            lekvvektprint=lekvvektprint+paprikkvektprint+befottvektprint+savanvektprint+savkapvektprint+szorpvektprint
                                            columnAug2 = [[sg.Text(lekvvektprint)]]
                                                             
                                            
                                            
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        elozodatumarray.append(datum)
                                        elozoszamlaszamarray.append(szamla)
                                        Voltsavanyitotetel=False
                                        SameDatumDifferentSzamla=False





                                    if colcount == 6:
                                        savanyito.append('\n')
                                        savanyito.append(df.iloc[osszosorcount2,colcount+1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-2])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-3])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-4])
                                        savanyito.append('\n')
                                        savanyito.append('\n')
                                        savanyitoprint=str(savanyito)
                                        savanyitoprint= savanyitoprint.replace(r'\n','\n')   
                                    else:
                                        kilenc.append('\n')
                                        
                                        kilenc.append(df.iloc[osszosorcount2,colcount+1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-2])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-3])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-4])
                                        kilenc.append('\n')
                                        kilenc.append('\n')
                                        kilencprint=str(kilenc)
                                        kilencprint=kilencprint.replace(r'\n','\n')
                                    columnAug = [[sg.Text(kilencprint, visible=True, key="__MINDENMASAug"), sg.Text(savanyitoprint, key="__SAVAAug",visible=False)]]
                                    createOsszeg()
                                    tizenketto=tiz[0]
                                
                                    
                                    if tizenegy != tizenketto:
                                        tizenegy=tiz[0]
                                        kilenc.append(tiz[0])
                                        savanyito.append(tiz[0])
                                
                                
                                    else:
                                        
                                        tizenegy=tizenketto
                                '''JUL'''
                                if datum>jundatum and datum<=juldatum:
                                    if julboolean == True:
                                        #valtozok nullazasa elso belepeskor
                                        columnJul = [[sg.Text(' ', visible=True, key="__MINDENMASJul"), sg.Text(' ', key="__SAVAJul",visible=False)]]
                                        savkapsuly=0
                                        savkaposszeg=0
                                        jelenhonap='Julius'
                                        szorpsuly=0
                                        szorposszeg=0
                                        savanysuly=0
                                        savanyosszeg=0
                                        befsuly=0
                                        befosszeg=0
                                        paprkremsuly=0
                                        paprkremosszeg=0
                                        lekvsuly =0
                                        lekvosszeg =0
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        lekvvekt=[]
                                        lekvvektprint=''
                                        paprikkvekt=[]
                                        paprikkvektprint=''
                                        befottvekt=[]
                                        befottvektprint=''
                                        savanvekt=[]
                                        savanvektprint=''
                                        savkapvekt=[]
                                        savkapvektprint=''
                                        szorpvekt=[]
                                        szorpvektprint=''
                                        julboolean=False
                                        kilencprint=''
                                        savanyitoprint=''
                                        tiz=''
                                        tizenegy=''
                                        tizenketto=''
                                        kilenc=[]
                                        savanyito=[]
                                    elozodatumarray.append(datum)
                                    elozoszamlaszamarray.append(szamla)
                                    datumdatum=elozodatumarray[0]
                                    szamlaszamla=elozoszamlaszamarray[0]
                                    tiz=str(df.iloc[osszosorcount2,colcount]).split(" ")
                                    # tetelek osszeadasa
                                    if datum == datumdatum:
                                        
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if Voltsavanyitotetel==True and szamlaszamla!=szamla:
                                                print("belep")
                                                SameDatumDifferentSzamla=True
                                    # datumvaltozas
                                    if datum!=datumdatum or SameDatumDifferentSzamla == True:
                                        datumsplit=str(elozodatumarray[0]).split(" ")
                                        if Voltsavanyitotetel==True:
                                            voltteteljul=True
                                            lekvvekt.append("===Lekvár===")
                                            lekvvekt.append("\n")
                                            lekvvekt.append(lekvsuly)
                                            lekvvekt.append(lekvosszeg)
                                            lekvvekt.append(datumsplit)
                                            lekvvekt.append(elozoszamlaszamarray[0])
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvektprint=str(lekvvekt)
                                            lekvvektprint=lekvvektprint.replace(r'\n','\n')
                                            
                                            paprikkvekt.append("===Paprikakrém===")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append(str(paprkremsuly))
                                            paprikkvekt.append(str(paprkremosszeg))
                                            paprikkvekt.append(datumsplit)
                                            paprikkvekt.append(str(elozoszamlaszamarray[0]))
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvektprint=str(paprikkvekt)
                                            paprikkvektprint=paprikkvektprint.replace(r'\n','\n')
                                            
                                            befottvekt.append("===Befőtt===")
                                            befottvekt.append("\n")
                                            befottvekt.append(befsuly)
                                            befottvekt.append(befosszeg)
                                            befottvekt.append(datumsplit)
                                            befottvekt.append(elozoszamlaszamarray[0])
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvektprint=str(befottvekt)
                                            befottvektprint=befottvektprint.replace(r'\n','\n')

                                            savanvekt.append("===Savanyúság===")
                                            savanvekt.append("\n")
                                            savanvekt.append(savanysuly)
                                            savanvekt.append(savanyosszeg)
                                            savanvekt.append(datumsplit)
                                            savanvekt.append(elozoszamlaszamarray[0])
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvektprint=str(savanvekt)
                                            savanvektprint=savanvektprint.replace(r'\n','\n')


                                            savkapvekt.append("===Savanyú Káposzta===")
                                            savkapvekt.append("\n")
                                            savkapvekt.append(savkapsuly)
                                            savkapvekt.append(savkaposszeg)
                                            savkapvekt.append(datumsplit)
                                            savkapvekt.append(elozoszamlaszamarray[0])
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvektprint=str(savkapvekt)
                                            savkapvektprint=savkapvektprint.replace(r'\n','\n')
                                            
                                            szorpvekt.append("===Szörp===")
                                            szorpvekt.append("\n")
                                            szorpvekt.append(szorpsuly)
                                            szorpvekt.append(szorposszeg)
                                            szorpvekt.append(datumsplit)
                                            szorpvekt.append(elozoszamlaszamarray[0])
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvektprint=str(szorpvekt)
                                            szorpvektprint=szorpvektprint.replace(r'\n','\n')


                                            savkapsuly=0
                                            savkaposszeg=0
                                            szorpsuly=0
                                            szorposszeg=0
                                            savanysuly=0
                                            savanyosszeg=0
                                            befsuly=0
                                            befosszeg=0
                                            paprkremsuly=0
                                            paprkremosszeg=0
                                            lekvsuly =0
                                            lekvosszeg =0
                                            lekvvektprint=lekvvektprint+paprikkvektprint+befottvektprint+savanvektprint+savkapvektprint+szorpvektprint
                                            columnJul2 = [[sg.Text(lekvvektprint)]]
                                                             
                                            
                                            
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        elozodatumarray.append(datum)
                                        elozoszamlaszamarray.append(szamla)
                                        Voltsavanyitotetel=False
                                        SameDatumDifferentSzamla=False





                                    if colcount == 6:
                                        savanyito.append('\n')
                                        savanyito.append(df.iloc[osszosorcount2,colcount+1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-2])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-3])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-4])
                                        savanyito.append('\n')
                                        savanyito.append('\n')
                                        savanyitoprint=str(savanyito)
                                        savanyitoprint= savanyitoprint.replace(r'\n','\n')   
                                    else:
                                        kilenc.append('\n')
                                        
                                        kilenc.append(df.iloc[osszosorcount2,colcount+1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-2])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-3])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-4])
                                        kilenc.append('\n')
                                        kilenc.append('\n')
                                        kilencprint=str(kilenc)
                                        kilencprint=kilencprint.replace(r'\n','\n')
                                    columnJul = [[sg.Text(kilencprint, visible=True, key="__MINDENMASJul"), sg.Text(savanyitoprint, key="__SAVAJul",visible=False)]]
                                    createOsszeg()
                                    tizenketto=tiz[0]
                                
                                    
                                    if tizenegy != tizenketto:
                                        tizenegy=tiz[0]
                                        kilenc.append(tiz[0])
                                        savanyito.append(tiz[0])
                                
                                
                                    else:
                                        
                                        tizenegy=tizenketto
                                '''JUN'''
                                if datum>majdatum and datum<=jundatum:
                                    if junboolean == True:
                                        #valtozok nullazasa elso belepeskor
                                        columnJun = [[sg.Text(' ', visible=True, key="__MINDENMASJun"), sg.Text(' ', key="__SAVAJun",visible=False)]]
                                        savkapsuly=0
                                        jelenhonap='Junius'
                                        savkaposszeg=0
                                        szorpsuly=0
                                        szorposszeg=0
                                        savanysuly=0
                                        savanyosszeg=0
                                        befsuly=0
                                        befosszeg=0
                                        paprkremsuly=0
                                        paprkremosszeg=0
                                        lekvsuly =0
                                        lekvosszeg =0
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        lekvvekt=[]
                                        lekvvektprint=''
                                        paprikkvekt=[]
                                        paprikkvektprint=''
                                        befottvekt=[]
                                        befottvektprint=''
                                        savanvekt=[]
                                        savanvektprint=''
                                        savkapvekt=[]
                                        savkapvektprint=''
                                        szorpvekt=[]
                                        szorpvektprint=''
                                        junboolean=False
                                        kilencprint=''
                                        savanyitoprint=''
                                        tiz=''
                                        tizenegy=''
                                        tizenketto=''
                                        kilenc=[]
                                        savanyito=[]
                                    elozodatumarray.append(datum)
                                    elozoszamlaszamarray.append(szamla)
                                    datumdatum=elozodatumarray[0]
                                    szamlaszamla=elozoszamlaszamarray[0]
                                    tiz=str(df.iloc[osszosorcount2,colcount]).split(" ")
                                    # tetelek osszeadasa
                                    if datum == datumdatum:
                                        
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if Voltsavanyitotetel==True and szamlaszamla!=szamla:
                                                print("belep")
                                                SameDatumDifferentSzamla=True
                                    # datumvaltozas
                                    if datum!=datumdatum or SameDatumDifferentSzamla == True:
                                        datumsplit=str(elozodatumarray[0]).split(" ")
                                        if Voltsavanyitotetel==True:
                                            voltteteljun=True
                                            lekvvekt.append("===Lekvár===")
                                            lekvvekt.append("\n")
                                            lekvvekt.append(lekvsuly)
                                            lekvvekt.append(lekvosszeg)
                                            lekvvekt.append(datumsplit)
                                            lekvvekt.append(elozoszamlaszamarray[0])
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvektprint=str(lekvvekt)
                                            lekvvektprint=lekvvektprint.replace(r'\n','\n')
                                            
                                            paprikkvekt.append("===Paprikakrém===")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append(str(paprkremsuly))
                                            paprikkvekt.append(str(paprkremosszeg))
                                            paprikkvekt.append(datumsplit)
                                            paprikkvekt.append(str(elozoszamlaszamarray[0]))
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvektprint=str(paprikkvekt)
                                            paprikkvektprint=paprikkvektprint.replace(r'\n','\n')
                                            
                                            befottvekt.append("===Befőtt===")
                                            befottvekt.append("\n")
                                            befottvekt.append(befsuly)
                                            befottvekt.append(befosszeg)
                                            befottvekt.append(datumsplit)
                                            befottvekt.append(elozoszamlaszamarray[0])
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvektprint=str(befottvekt)
                                            befottvektprint=befottvektprint.replace(r'\n','\n')

                                            savanvekt.append("===Savanyúság===")
                                            savanvekt.append("\n")
                                            savanvekt.append(savanysuly)
                                            savanvekt.append(savanyosszeg)
                                            savanvekt.append(datumsplit)
                                            savanvekt.append(elozoszamlaszamarray[0])
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvektprint=str(savanvekt)
                                            savanvektprint=savanvektprint.replace(r'\n','\n')


                                            savkapvekt.append("===Savanyú Káposzta===")
                                            savkapvekt.append("\n")
                                            savkapvekt.append(savkapsuly)
                                            savkapvekt.append(savkaposszeg)
                                            savkapvekt.append(datumsplit)
                                            savkapvekt.append(elozoszamlaszamarray[0])
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvektprint=str(savkapvekt)
                                            savkapvektprint=savkapvektprint.replace(r'\n','\n')
                                            
                                            szorpvekt.append("===Szörp===")
                                            szorpvekt.append("\n")
                                            szorpvekt.append(szorpsuly)
                                            szorpvekt.append(szorposszeg)
                                            szorpvekt.append(datumsplit)
                                            szorpvekt.append(elozoszamlaszamarray[0])
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvektprint=str(szorpvekt)
                                            szorpvektprint=szorpvektprint.replace(r'\n','\n')


                                            savkapsuly=0
                                            savkaposszeg=0
                                            szorpsuly=0
                                            szorposszeg=0
                                            savanysuly=0
                                            savanyosszeg=0
                                            befsuly=0
                                            befosszeg=0
                                            paprkremsuly=0
                                            paprkremosszeg=0
                                            lekvsuly =0
                                            lekvosszeg =0
                                            lekvvektprint=lekvvektprint+paprikkvektprint+befottvektprint+savanvektprint+savkapvektprint+szorpvektprint
                                            columnJun2 = [[sg.Text(lekvvektprint)]]
                                                             
                                            
                                            
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        elozodatumarray.append(datum)
                                        elozoszamlaszamarray.append(szamla)
                                        Voltsavanyitotetel=False
                                        SameDatumDifferentSzamla=False





                                    if colcount == 6:
                                        savanyito.append('\n')
                                        savanyito.append(df.iloc[osszosorcount2,colcount+1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-2])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-3])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-4])
                                        savanyito.append('\n')
                                        savanyito.append('\n')
                                        savanyitoprint=str(savanyito)
                                        savanyitoprint= savanyitoprint.replace(r'\n','\n')   
                                    else:
                                        kilenc.append('\n')
                                        
                                        kilenc.append(df.iloc[osszosorcount2,colcount+1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-2])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-3])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-4])
                                        kilenc.append('\n')
                                        kilenc.append('\n')
                                        kilencprint=str(kilenc)
                                        kilencprint=kilencprint.replace(r'\n','\n')
                                    columnJun = [[sg.Text(kilencprint, visible=True, key="__MINDENMASJun"), sg.Text(savanyitoprint, key="__SAVAJun",visible=False)]]
                                    createOsszeg()
                                    tizenketto=tiz[0]
                                
                                    
                                    if tizenegy != tizenketto:
                                        tizenegy=tiz[0]
                                        kilenc.append(tiz[0])
                                        savanyito.append(tiz[0])
                                
                                
                                    else:
                                        
                                        tizenegy=tizenketto
                                '''MAJ'''
                                if datum>aprdatum and datum<=majdatum:
                                    if majboolean == True:
                                        #valtozok nullazasa elso belepeskor
                                        columnMaj = [[sg.Text(' ', visible=True, key="__MINDENMASMaj"), sg.Text(' ', key="__SAVAMaj",visible=False)]]
                                        savkapsuly=0
                                        savkaposszeg=0
                                        jelenhonap='Majus'
                                        szorpsuly=0
                                        szorposszeg=0
                                        savanysuly=0
                                        savanyosszeg=0
                                        befsuly=0
                                        befosszeg=0
                                        paprkremsuly=0
                                        paprkremosszeg=0
                                        lekvsuly =0
                                        lekvosszeg =0
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        lekvvekt=[]
                                        lekvvektprint=''
                                        paprikkvekt=[]
                                        paprikkvektprint=''
                                        befottvekt=[]
                                        befottvektprint=''
                                        savanvekt=[]
                                        savanvektprint=''
                                        savkapvekt=[]
                                        savkapvektprint=''
                                        szorpvekt=[]
                                        szorpvektprint=''
                                        majboolean=False
                                        kilencprint=''
                                        savanyitoprint=''
                                        tiz=''
                                        tizenegy=''
                                        tizenketto=''
                                        kilenc=[]
                                        savanyito=[]
                                    elozodatumarray.append(datum)
                                    elozoszamlaszamarray.append(szamla)
                                    datumdatum=elozodatumarray[0]
                                    szamlaszamla=elozoszamlaszamarray[0]
                                    tiz=str(df.iloc[osszosorcount2,colcount]).split(" ")
                                    # tetelek osszeadasa
                                    if datum == datumdatum:
                                        
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if Voltsavanyitotetel==True and szamlaszamla!=szamla:
                                                print("belep")
                                                SameDatumDifferentSzamla=True
                                    # datumvaltozas
                                    if datum!=datumdatum or SameDatumDifferentSzamla == True:
                                        datumsplit=str(elozodatumarray[0]).split(" ")
                                        if Voltsavanyitotetel==True:
                                            volttetelmaj=True
                                            lekvvekt.append("===Lekvár===")
                                            lekvvekt.append("\n")
                                            lekvvekt.append(lekvsuly)
                                            lekvvekt.append(lekvosszeg)
                                            lekvvekt.append(datumsplit)
                                            lekvvekt.append(elozoszamlaszamarray[0])
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvektprint=str(lekvvekt)
                                            lekvvektprint=lekvvektprint.replace(r'\n','\n')
                                            
                                            paprikkvekt.append("===Paprikakrém===")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append(str(paprkremsuly))
                                            paprikkvekt.append(str(paprkremosszeg))
                                            paprikkvekt.append(datumsplit)
                                            paprikkvekt.append(str(elozoszamlaszamarray[0]))
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvektprint=str(paprikkvekt)
                                            paprikkvektprint=paprikkvektprint.replace(r'\n','\n')
                                            
                                            befottvekt.append("===Befőtt===")
                                            befottvekt.append("\n")
                                            befottvekt.append(befsuly)
                                            befottvekt.append(befosszeg)
                                            befottvekt.append(datumsplit)
                                            befottvekt.append(elozoszamlaszamarray[0])
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvektprint=str(befottvekt)
                                            befottvektprint=befottvektprint.replace(r'\n','\n')

                                            savanvekt.append("===Savanyúság===")
                                            savanvekt.append("\n")
                                            savanvekt.append(savanysuly)
                                            savanvekt.append(savanyosszeg)
                                            savanvekt.append(datumsplit)
                                            savanvekt.append(elozoszamlaszamarray[0])
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvektprint=str(savanvekt)
                                            savanvektprint=savanvektprint.replace(r'\n','\n')


                                            savkapvekt.append("===Savanyú Káposzta===")
                                            savkapvekt.append("\n")
                                            savkapvekt.append(savkapsuly)
                                            savkapvekt.append(savkaposszeg)
                                            savkapvekt.append(datumsplit)
                                            savkapvekt.append(elozoszamlaszamarray[0])
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvektprint=str(savkapvekt)
                                            savkapvektprint=savkapvektprint.replace(r'\n','\n')
                                            
                                            szorpvekt.append("===Szörp===")
                                            szorpvekt.append("\n")
                                            szorpvekt.append(szorpsuly)
                                            szorpvekt.append(szorposszeg)
                                            szorpvekt.append(datumsplit)
                                            szorpvekt.append(elozoszamlaszamarray[0])
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvektprint=str(szorpvekt)
                                            szorpvektprint=szorpvektprint.replace(r'\n','\n')


                                            savkapsuly=0
                                            savkaposszeg=0
                                            szorpsuly=0
                                            szorposszeg=0
                                            savanysuly=0
                                            savanyosszeg=0
                                            befsuly=0
                                            befosszeg=0
                                            paprkremsuly=0
                                            paprkremosszeg=0
                                            lekvsuly =0
                                            lekvosszeg =0
                                            lekvvektprint=lekvvektprint+paprikkvektprint+befottvektprint+savanvektprint+savkapvektprint+szorpvektprint
                                            columnMaj2 = [[sg.Text(lekvvektprint)]]
                                                             
                                            
                                            
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        elozodatumarray.append(datum)
                                        elozoszamlaszamarray.append(szamla)
                                        Voltsavanyitotetel=False
                                        SameDatumDifferentSzamla=False





                                    if colcount == 6:
                                        savanyito.append('\n')
                                        savanyito.append(df.iloc[osszosorcount2,colcount+1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-2])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-3])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-4])
                                        savanyito.append('\n')
                                        savanyito.append('\n')
                                        savanyitoprint=str(savanyito)
                                        savanyitoprint= savanyitoprint.replace(r'\n','\n')   
                                    else:
                                        kilenc.append('\n')
                                        
                                        kilenc.append(df.iloc[osszosorcount2,colcount+1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-2])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-3])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-4])
                                        kilenc.append('\n')
                                        kilenc.append('\n')
                                        kilencprint=str(kilenc)
                                        kilencprint=kilencprint.replace(r'\n','\n')
                                    columnMaj = [[sg.Text(kilencprint, visible=True, key="__MINDENMASMaj"), sg.Text(savanyitoprint, key="__SAVAMaj",visible=False)]]
                                    createOsszeg()
                                    tizenketto=tiz[0]
                                
                                    
                                    if tizenegy != tizenketto:
                                        tizenegy=tiz[0]
                                        kilenc.append(tiz[0])
                                        savanyito.append(tiz[0])
                                
                                
                                    else:
                                        
                                        tizenegy=tizenketto
                                '''APRil'''
                                if datum>marcdatum and datum<=aprdatum:
                                    if aprboolean == True:
                                        #valtozok nullazasa elso belepeskor
                                        columnApr = [[sg.Text(' ', visible=True, key="__MINDENMASApr"), sg.Text(' ', key="__SAVAApr",visible=False)]]
                                        savkapsuly=0
                                        savkaposszeg=0
                                        szorpsuly=0
                                        jelenhonap='Aprilis'
                                        szorposszeg=0
                                        savanysuly=0
                                        savanyosszeg=0
                                        befsuly=0
                                        befosszeg=0
                                        paprkremsuly=0
                                        paprkremosszeg=0
                                        lekvsuly =0
                                        lekvosszeg =0
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        lekvvekt=[]
                                        lekvvektprint=''
                                        paprikkvekt=[]
                                        paprikkvektprint=''
                                        befottvekt=[]
                                        befottvektprint=''
                                        savanvekt=[]
                                        savanvektprint=''
                                        savkapvekt=[]
                                        savkapvektprint=''
                                        szorpvekt=[]
                                        szorpvektprint=''
                                        aprboolean=False
                                        kilencprint=''
                                        savanyitoprint=''
                                        tiz=''
                                        tizenegy=''
                                        tizenketto=''
                                        kilenc=[]
                                        savanyito=[]
                                    elozodatumarray.append(datum)
                                    elozoszamlaszamarray.append(szamla)
                                    datumdatum=elozodatumarray[0]
                                    szamlaszamla=elozoszamlaszamarray[0]
                                    tiz=str(df.iloc[osszosorcount2,colcount]).split(" ")
                                    # tetelek osszeadasa
                                    if datum == datumdatum:
                                        
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if Voltsavanyitotetel==True and szamlaszamla!=szamla:
                                                print("belep")
                                                SameDatumDifferentSzamla=True
                                    # datumvaltozas
                                    if datum!=datumdatum or SameDatumDifferentSzamla == True:
                                        datumsplit=str(elozodatumarray[0]).split(" ")
                                        if Voltsavanyitotetel==True:
                                            volttetelapr=True
                                            lekvvekt.append("===Lekvár===")
                                            lekvvekt.append("\n")
                                            lekvvekt.append(lekvsuly)
                                            lekvvekt.append(lekvosszeg)
                                            lekvvekt.append(datumsplit)
                                            lekvvekt.append(elozoszamlaszamarray[0])
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvektprint=str(lekvvekt)
                                            lekvvektprint=lekvvektprint.replace(r'\n','\n')
                                            
                                            paprikkvekt.append("===Paprikakrém===")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append(str(paprkremsuly))
                                            paprikkvekt.append(str(paprkremosszeg))
                                            paprikkvekt.append(datumsplit)
                                            paprikkvekt.append(str(elozoszamlaszamarray[0]))
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvektprint=str(paprikkvekt)
                                            paprikkvektprint=paprikkvektprint.replace(r'\n','\n')
                                            
                                            befottvekt.append("===Befőtt===")
                                            befottvekt.append("\n")
                                            befottvekt.append(befsuly)
                                            befottvekt.append(befosszeg)
                                            befottvekt.append(datumsplit)
                                            befottvekt.append(elozoszamlaszamarray[0])
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvektprint=str(befottvekt)
                                            befottvektprint=befottvektprint.replace(r'\n','\n')

                                            savanvekt.append("===Savanyúság===")
                                            savanvekt.append("\n")
                                            savanvekt.append(savanysuly)
                                            savanvekt.append(savanyosszeg)
                                            savanvekt.append(datumsplit)
                                            savanvekt.append(elozoszamlaszamarray[0])
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvektprint=str(savanvekt)
                                            savanvektprint=savanvektprint.replace(r'\n','\n')


                                            savkapvekt.append("===Savanyú Káposzta===")
                                            savkapvekt.append("\n")
                                            savkapvekt.append(savkapsuly)
                                            savkapvekt.append(savkaposszeg)
                                            savkapvekt.append(datumsplit)
                                            savkapvekt.append(elozoszamlaszamarray[0])
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvektprint=str(savkapvekt)
                                            savkapvektprint=savkapvektprint.replace(r'\n','\n')
                                            
                                            szorpvekt.append("===Szörp===")
                                            szorpvekt.append("\n")
                                            szorpvekt.append(szorpsuly)
                                            szorpvekt.append(szorposszeg)
                                            szorpvekt.append(datumsplit)
                                            szorpvekt.append(elozoszamlaszamarray[0])
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvektprint=str(szorpvekt)
                                            szorpvektprint=szorpvektprint.replace(r'\n','\n')


                                            savkapsuly=0
                                            savkaposszeg=0
                                            szorpsuly=0
                                            szorposszeg=0
                                            savanysuly=0
                                            savanyosszeg=0
                                            befsuly=0
                                            befosszeg=0
                                            paprkremsuly=0
                                            paprkremosszeg=0
                                            lekvsuly =0
                                            lekvosszeg =0
                                            lekvvektprint=lekvvektprint+paprikkvektprint+befottvektprint+savanvektprint+savkapvektprint+szorpvektprint
                                            columnApr2 = [[sg.Text(lekvvektprint)]]
                                                             
                                            
                                            
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        elozodatumarray.append(datum)
                                        elozoszamlaszamarray.append(szamla)
                                        Voltsavanyitotetel=False
                                        SameDatumDifferentSzamla=False





                                    if colcount == 6:
                                        savanyito.append('\n')
                                        savanyito.append(df.iloc[osszosorcount2,colcount+1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-2])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-3])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-4])
                                        savanyito.append('\n')
                                        savanyito.append('\n')
                                        savanyitoprint=str(savanyito)
                                        savanyitoprint= savanyitoprint.replace(r'\n','\n')   
                                    else:
                                        kilenc.append('\n')
                                        
                                        kilenc.append(df.iloc[osszosorcount2,colcount+1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-2])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-3])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-4])
                                        kilenc.append('\n')
                                        kilenc.append('\n')
                                        kilencprint=str(kilenc)
                                        kilencprint=kilencprint.replace(r'\n','\n')
                                    columnApr = [[sg.Text(kilencprint, visible=True, key="__MINDENMASApr"), sg.Text(savanyitoprint, key="__SAVAApr",visible=False)]]
                                    createOsszeg()
                                    tizenketto=tiz[0]
                                
                                    
                                    if tizenegy != tizenketto:
                                        tizenegy=tiz[0]
                                        kilenc.append(tiz[0])
                                        savanyito.append(tiz[0])
                                
                                
                                    else:
                                        
                                        tizenegy=tizenketto
                                '''MARC'''
                                if datum>februdatum and datum<=marcdatum:
                                    if marcboolean == True:
                                        #valtozok nullazasa elso belepeskor
                                        columnMarc = [[sg.Text(' ', visible=True, key="__MINDENMASMar"), sg.Text(' ', key="__SAVAMar",visible=False)]]
                                        savkapsuly=0
                                        savkaposszeg=0
                                        szorpsuly=0
                                        szorposszeg=0
                                        jelenhonap='Marcius'
                                        savanysuly=0
                                        savanyosszeg=0
                                        befsuly=0
                                        befosszeg=0
                                        paprkremsuly=0
                                        paprkremosszeg=0
                                        lekvsuly =0
                                        lekvosszeg =0
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        lekvvekt=[]
                                        lekvvektprint=''
                                        paprikkvekt=[]
                                        paprikkvektprint=''
                                        befottvekt=[]
                                        befottvektprint=''
                                        savanvekt=[]
                                        savanvektprint=''
                                        savkapvekt=[]
                                        savkapvektprint=''
                                        szorpvekt=[]
                                        szorpvektprint=''
                                        marcboolean=False
                                        kilencprint=''
                                        savanyitoprint=''
                                        tiz=''
                                        tizenegy=''
                                        tizenketto=''
                                        kilenc=[]
                                        savanyito=[]
                                    elozodatumarray.append(datum)
                                    elozoszamlaszamarray.append(szamla)
                                    datumdatum=elozodatumarray[0]
                                    szamlaszamla=elozoszamlaszamarray[0]
                                    tiz=str(df.iloc[osszosorcount2,colcount]).split(" ")
                                    # tetelek osszeadasa
                                    if datum == datumdatum:
                                        
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if Voltsavanyitotetel==True and szamlaszamla!=szamla:
                                                print("belep")
                                                SameDatumDifferentSzamla=True
                                    # datumvaltozas
                                    if datum!=datumdatum or SameDatumDifferentSzamla == True:
                                        datumsplit=str(elozodatumarray[0]).split(" ")
                                        if Voltsavanyitotetel==True:
                                            volttetelmar=True
                                            lekvvekt.append("===Lekvár===")
                                            lekvvekt.append("\n")
                                            lekvvekt.append(lekvsuly)
                                            lekvvekt.append(lekvosszeg)
                                            lekvvekt.append(datumsplit)
                                            lekvvekt.append(elozoszamlaszamarray[0])
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvektprint=str(lekvvekt)
                                            lekvvektprint=lekvvektprint.replace(r'\n','\n')
                                            
                                            paprikkvekt.append("===Paprikakrém===")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append(str(paprkremsuly))
                                            paprikkvekt.append(str(paprkremosszeg))
                                            paprikkvekt.append(datumsplit)
                                            paprikkvekt.append(str(elozoszamlaszamarray[0]))
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvektprint=str(paprikkvekt)
                                            paprikkvektprint=paprikkvektprint.replace(r'\n','\n')
                                            
                                            befottvekt.append("===Befőtt===")
                                            befottvekt.append("\n")
                                            befottvekt.append(befsuly)
                                            befottvekt.append(befosszeg)
                                            befottvekt.append(datumsplit)
                                            befottvekt.append(elozoszamlaszamarray[0])
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvektprint=str(befottvekt)
                                            befottvektprint=befottvektprint.replace(r'\n','\n')

                                            savanvekt.append("===Savanyúság===")
                                            savanvekt.append("\n")
                                            savanvekt.append(savanysuly)
                                            savanvekt.append(savanyosszeg)
                                            savanvekt.append(datumsplit)
                                            savanvekt.append(elozoszamlaszamarray[0])
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvektprint=str(savanvekt)
                                            savanvektprint=savanvektprint.replace(r'\n','\n')


                                            savkapvekt.append("===Savanyú Káposzta===")
                                            savkapvekt.append("\n")
                                            savkapvekt.append(savkapsuly)
                                            savkapvekt.append(savkaposszeg)
                                            savkapvekt.append(datumsplit)
                                            savkapvekt.append(elozoszamlaszamarray[0])
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvektprint=str(savkapvekt)
                                            savkapvektprint=savkapvektprint.replace(r'\n','\n')
                                            
                                            szorpvekt.append("===Szörp===")
                                            szorpvekt.append("\n")
                                            szorpvekt.append(szorpsuly)
                                            szorpvekt.append(szorposszeg)
                                            szorpvekt.append(datumsplit)
                                            szorpvekt.append(elozoszamlaszamarray[0])
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvektprint=str(szorpvekt)
                                            szorpvektprint=szorpvektprint.replace(r'\n','\n')


                                            savkapsuly=0
                                            savkaposszeg=0
                                            szorpsuly=0
                                            szorposszeg=0
                                            savanysuly=0
                                            savanyosszeg=0
                                            befsuly=0
                                            befosszeg=0
                                            paprkremsuly=0
                                            paprkremosszeg=0
                                            lekvsuly =0
                                            lekvosszeg =0
                                            lekvvektprint=lekvvektprint+paprikkvektprint+befottvektprint+savanvektprint+savkapvektprint+szorpvektprint
                                            columnMarc2 = [[sg.Text(lekvvektprint)]]
                                                             
                                            
                                            
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        elozodatumarray.append(datum)
                                        elozoszamlaszamarray.append(szamla)
                                        Voltsavanyitotetel=False
                                        SameDatumDifferentSzamla=False





                                    if colcount == 6:
                                        savanyito.append('\n')
                                        savanyito.append(df.iloc[osszosorcount2,colcount+1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-2])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-3])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-4])
                                        savanyito.append('\n')
                                        savanyito.append('\n')
                                        savanyitoprint=str(savanyito)
                                        savanyitoprint= savanyitoprint.replace(r'\n','\n')   
                                    else:
                                        kilenc.append('\n')
                                        
                                        kilenc.append(df.iloc[osszosorcount2,colcount+1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-2])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-3])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-4])
                                        kilenc.append('\n')
                                        kilenc.append('\n')
                                        kilencprint=str(kilenc)
                                        kilencprint=kilencprint.replace(r'\n','\n')
                                    columnMarc = [[sg.Text(kilencprint, visible=True, key="__MINDENMASMar"), sg.Text(savanyitoprint, key="__SAVAMar",visible=False)]]
                                    createOsszeg()
                                    tizenketto=tiz[0]
                                
                                    
                                    if tizenegy != tizenketto:
                                        tizenegy=tiz[0]
                                        kilenc.append(tiz[0])
                                        savanyito.append(tiz[0])
                                
                                
                                    else:
                                        
                                        tizenegy=tizenketto
                                '''FEBR'''
                                if datum>janudatum and datum<=februdatum:
                                    if februboolean == True:
                                        columnFeb = [[sg.Text(' ', visible=True, key="__MINDENMASFeb"), sg.Text(' ', key="__SAVAFeb",visible=False)]]
                                        #valtozok nullazasa elso belepeskor
                                        savkapsuly=0
                                        savkaposszeg=0
                                        jelenhonap='Februar'
                                        szorpsuly=0
                                        szorposszeg=0
                                        savanysuly=0
                                        savanyosszeg=0
                                        befsuly=0
                                        befosszeg=0
                                        paprkremsuly=0
                                        paprkremosszeg=0
                                        lekvsuly =0
                                        lekvosszeg =0
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        lekvvekt=[]
                                        lekvvektprint=''
                                        paprikkvekt=[]
                                        paprikkvektprint=''
                                        befottvekt=[]
                                        befottvektprint=''
                                        savanvekt=[]
                                        savanvektprint=''
                                        savkapvekt=[]
                                        savkapvektprint=''
                                        szorpvekt=[]
                                        szorpvektprint=''
                                        februboolean=False
                                        kilencprint=''
                                        savanyitoprint=''
                                        tiz=''
                                        tizenegy=''
                                        tizenketto=''
                                        kilenc=[]
                                        savanyito=[]
                                    elozodatumarray.append(datum)
                                    elozoszamlaszamarray.append(szamla)
                                    datumdatum=elozodatumarray[0]
                                    szamlaszamla=elozoszamlaszamarray[0]
                                    tiz=str(df.iloc[osszosorcount2,colcount]).split(" ")
                                    # tetelek osszeadasa
                                    if datum == datumdatum:
                                        
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if Voltsavanyitotetel==True and szamlaszamla!=szamla:
                                                print("belep")
                                                SameDatumDifferentSzamla=True
                                    # datumvaltozas
                                    if datum!=datumdatum or SameDatumDifferentSzamla == True:
                                        datumsplit=str(elozodatumarray[0]).split(" ")
                                        if Voltsavanyitotetel==True:
                                            volttetelfeb=True
                                            lekvvekt.append("===Lekvár===")
                                            lekvvekt.append("\n")
                                            lekvvekt.append(lekvsuly)
                                            lekvvekt.append(lekvosszeg)
                                            lekvvekt.append(datumsplit)
                                            lekvvekt.append(elozoszamlaszamarray[0])
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvektprint=str(lekvvekt)
                                            lekvvektprint=lekvvektprint.replace(r'\n','\n')
                                            
                                            paprikkvekt.append("===Paprikakrém===")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append(str(paprkremsuly))
                                            paprikkvekt.append(str(paprkremosszeg))
                                            paprikkvekt.append(datumsplit)
                                            paprikkvekt.append(str(elozoszamlaszamarray[0]))
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvektprint=str(paprikkvekt)
                                            paprikkvektprint=paprikkvektprint.replace(r'\n','\n')
                                            
                                            befottvekt.append("===Befőtt===")
                                            befottvekt.append("\n")
                                            befottvekt.append(befsuly)
                                            befottvekt.append(befosszeg)
                                            befottvekt.append(datumsplit)
                                            befottvekt.append(elozoszamlaszamarray[0])
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvektprint=str(befottvekt)
                                            befottvektprint=befottvektprint.replace(r'\n','\n')

                                            savanvekt.append("===Savanyúság===")
                                            savanvekt.append("\n")
                                            savanvekt.append(savanysuly)
                                            savanvekt.append(savanyosszeg)
                                            savanvekt.append(datumsplit)
                                            savanvekt.append(elozoszamlaszamarray[0])
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvektprint=str(savanvekt)
                                            savanvektprint=savanvektprint.replace(r'\n','\n')


                                            savkapvekt.append("===Savanyú Káposzta===")
                                            savkapvekt.append("\n")
                                            savkapvekt.append(savkapsuly)
                                            savkapvekt.append(savkaposszeg)
                                            savkapvekt.append(datumsplit)
                                            savkapvekt.append(elozoszamlaszamarray[0])
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvektprint=str(savkapvekt)
                                            savkapvektprint=savkapvektprint.replace(r'\n','\n')
                                            
                                            szorpvekt.append("===Szörp===")
                                            szorpvekt.append("\n")
                                            szorpvekt.append(szorpsuly)
                                            szorpvekt.append(szorposszeg)
                                            szorpvekt.append(datumsplit)
                                            szorpvekt.append(elozoszamlaszamarray[0])
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvektprint=str(szorpvekt)
                                            szorpvektprint=szorpvektprint.replace(r'\n','\n')


                                            savkapsuly=0
                                            savkaposszeg=0
                                            szorpsuly=0
                                            szorposszeg=0
                                            savanysuly=0
                                            savanyosszeg=0
                                            befsuly=0
                                            befosszeg=0
                                            paprkremsuly=0
                                            paprkremosszeg=0
                                            lekvsuly =0
                                            lekvosszeg =0
                                            lekvvektprint=lekvvektprint+paprikkvektprint+befottvektprint+savanvektprint+savkapvektprint+szorpvektprint
                                            columnFeb2 = [[sg.Text(lekvvektprint)]]
                                                             
                                            
                                            
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        elozodatumarray.append(datum)
                                        elozoszamlaszamarray.append(szamla)
                                        Voltsavanyitotetel=False
                                        SameDatumDifferentSzamla=False





                                    if colcount == 6:
                                        savanyito.append('\n')
                                        savanyito.append(df.iloc[osszosorcount2,colcount+1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-2])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-3])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-4])
                                        savanyito.append('\n')
                                        savanyito.append('\n')
                                        savanyitoprint=str(savanyito)
                                        savanyitoprint= savanyitoprint.replace(r'\n','\n')   
                                    else:
                                        kilenc.append('\n')
                                        
                                        kilenc.append(df.iloc[osszosorcount2,colcount+1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-2])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-3])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-4])
                                        kilenc.append('\n')
                                        kilenc.append('\n')
                                        kilencprint=str(kilenc)
                                        kilencprint=kilencprint.replace(r'\n','\n')
                                    columnFeb = [[sg.Text(kilencprint, visible=True, key="__MINDENMASFeb"), sg.Text(savanyitoprint, key="__SAVAFeb",visible=False)]]
                                    createOsszeg()
                                    tizenketto=tiz[0]
                                
                                    
                                    if tizenegy != tizenketto:
                                        tizenegy=tiz[0]
                                        kilenc.append(tiz[0])
                                        savanyito.append(tiz[0])
                                
                                
                                    else:
                                        
                                        tizenegy=tizenketto
                                '''JAN'''
                                if datum<januelsodatum:
                                    tiz=str(df.iloc[osszosorcount2,colcount]).split(" ")
                                    elozodatumarray.append(datum)
                                    elozoszamlaszamarray.append(szamla)
                                    datumdatum=elozodatumarray[0]
                                    jelenhonap='Januar'
                                    szamlaszamla=elozoszamlaszamarray[0]
                                    # tetelek osszeadasa
                                    if datum == datumdatum:
                                        
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        if Voltsavanyitotetel==True and szamlaszamla!=szamla:
                                                print("belep")
                                                SameDatumDifferentSzamla=True
                                    # datumvaltozas
                                    if datum!=datumdatum or SameDatumDifferentSzamla ==True:
                                        datumsplit=str(elozodatumarray[0]).split(" ")
                                        if Voltsavanyitotetel==True:
                                            voltteteljan=True
                                            lekvvekt.append("===Lekvár===")
                                            lekvvekt.append("\n")
                                            lekvvekt.append(lekvsuly)
                                            lekvvekt.append(lekvosszeg)
                                            lekvvekt.append(datumsplit)
                                            lekvvekt.append(elozoszamlaszamarray[0])
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvekt.append("\n")
                                            lekvvektprint=str(lekvvekt)
                                            lekvvektprint=lekvvektprint.replace(r'\n','\n')
                                            
                                            paprikkvekt.append("===Paprikakrém===")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append(str(paprkremsuly))
                                            paprikkvekt.append(str(paprkremosszeg))
                                            paprikkvekt.append(datumsplit)
                                            paprikkvekt.append(str(elozoszamlaszamarray[0]))
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvekt.append("\n")
                                            paprikkvektprint=str(paprikkvekt)
                                            paprikkvektprint=paprikkvektprint.replace(r'\n','\n')
                                            
                                            befottvekt.append("===Befőtt===")
                                            befottvekt.append("\n")
                                            befottvekt.append(befsuly)
                                            befottvekt.append(befosszeg)
                                            befottvekt.append(datumsplit)
                                            befottvekt.append(elozoszamlaszamarray[0])
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvekt.append("\n")
                                            befottvektprint=str(befottvekt)
                                            befottvektprint=befottvektprint.replace(r'\n','\n')

                                            savanvekt.append("===Savanyúság===")
                                            savanvekt.append("\n")
                                            savanvekt.append(savanysuly)
                                            savanvekt.append(savanyosszeg)
                                            savanvekt.append(datumsplit)
                                            savanvekt.append(elozoszamlaszamarray[0])
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvekt.append("\n")
                                            savanvektprint=str(savanvekt)
                                            savanvektprint=savanvektprint.replace(r'\n','\n')


                                            savkapvekt.append("===Savanyú Káposzta===")
                                            savkapvekt.append("\n")
                                            savkapvekt.append(savkapsuly)
                                            savkapvekt.append(savkaposszeg)
                                            savkapvekt.append(datumsplit)
                                            savkapvekt.append(elozoszamlaszamarray[0])
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvekt.append("\n")
                                            savkapvektprint=str(savkapvekt)
                                            savkapvektprint=savkapvektprint.replace(r'\n','\n')
                                            
                                            szorpvekt.append("===Szörp===")
                                            szorpvekt.append("\n")
                                            szorpvekt.append(szorpsuly)
                                            szorpvekt.append(szorposszeg)
                                            szorpvekt.append(datumsplit)
                                            szorpvekt.append(elozoszamlaszamarray[0])
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvekt.append("\n")
                                            szorpvektprint=str(szorpvekt)
                                            szorpvektprint=szorpvektprint.replace(r'\n','\n')


                                            savkapsuly=0
                                            savkaposszeg=0
                                            szorpsuly=0
                                            szorposszeg=0
                                            savanysuly=0
                                            savanyosszeg=0
                                            befsuly=0
                                            befosszeg=0
                                            paprkremsuly=0
                                            paprkremosszeg=0
                                            lekvsuly =0
                                            lekvosszeg =0
                                            lekvvektprint=lekvvektprint+paprikkvektprint+befottvektprint+savanvektprint+savkapvektprint+szorpvektprint
                                            columnJan2 = [[sg.Text(lekvvektprint)]]
                                                             
                                            
                                            
                                        if df.iloc[osszosorcount2,colcount-4] in nullhetkettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullahetvenkettosuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullharminckettoelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaharminchetsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullotelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullaotvensuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in kgelemek:
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                            if df.iloc[osszosorcount2,colcount-4] in savanyukaposztaelemek:
                                                    meghivas= kgsuly(mennyiseg)
                                                    savkapsuly = savkapsuly + round(meghivas, 2)
                                                    savkaposszeg=savkaposszeg+termekara
                                        if df.iloc[osszosorcount2,colcount-4] in nullkettokettoelemek:
                                        
                                            if df.iloc[osszosorcount2,colcount-4] in paprikakremelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    paprkremsuly = paprkremsuly + round(meghivas, 2)
                                                    paprkremosszeg=paprkremosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in lekvarelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    lekvsuly = lekvsuly + round(meghivas, 2)
                                                    lekvosszeg=lekvosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in befottelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    befsuly = befsuly + round(meghivas, 2)
                                                    befosszeg=befosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in savanyusagelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    savanysuly = savanysuly + round(meghivas, 2)
                                                    savanyosszeg=savanyosszeg+termekara
                                                    Voltsavanyitotetel=True
                                            if df.iloc[osszosorcount2,colcount-4] in szorpelemek:
                                                    meghivas= nullkettoketsuly(mennyiseg)
                                                    szorpsuly = szorpsuly + round(meghivas, 2)
                                                    szorposszeg=szorposszeg+termekara
                                                    Voltsavanyitotetel=True
                                        elozodatumarray=[]
                                        elozoszamlaszamarray=[]
                                        elozodatumarray.append(datum)
                                        elozoszamlaszamarray.append(szamla)
                                        Voltsavanyitotetel=False
                                        SameDatumDifferentSzamla=False
                                        
                                    
                                    

                                    
                                    if colcount == 6:
                                        savanyito.append('\n')
                                        savanyito.append(df.iloc[osszosorcount2,colcount+1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-1])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-2])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-3])
                                        savanyito.append(df.iloc[osszosorcount2,colcount-4])
                                        savanyito.append('\n')
                                        savanyito.append('\n')
                                        savanyitoprint=str(savanyito)
                                        savanyitoprint= savanyitoprint.replace(r'\n','\n')   
                                    else:
                                        kilenc.append('\n')
                                        
                                        kilenc.append(df.iloc[osszosorcount2,colcount+1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-1])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-2])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-3])
                                        kilenc.append(df.iloc[osszosorcount2,colcount-4])
                                        kilenc.append('\n')
                                        kilenc.append('\n')
                                        kilencprint=str(kilenc)
                                        kilencprint=kilencprint.replace(r'\n','\n')
                                    columnJan = [[sg.Text(kilencprint, visible=True, key="__MINDENMAS"), sg.Text(savanyitoprint, key="__SAVA",visible=False)]]
                                    tizenketto=tiz[0]
                                    createOsszeg()
                                    
                                    if tizenegy != tizenketto:
                                        tizenegy=tiz[0]
                                        kilenc.append(tiz[0])
                                        savanyito.append(tiz[0])
                                
                                
                                    else:
                                        
                                        tizenegy=tizenketto
                                    
                                    
                                    

                        osszosorcount2+=1
                        muv+=1
                        
                        
                    osszosorcount2=0
                    colcount+=6
                    
                colcount=0
                osszosorcount+=1
                loadingwhile=0
                
                # loading screen
                if df.iloc[osszosorcount,1] =="Január":
                    tru=True
                    window['-text3-'].update("Január")
                if df.iloc[osszosorcount,1] =="Február":
                    window['-text3-'].update("Február")
                if df.iloc[osszosorcount,1] =="Március":
                    window['-text3-'].update("Március")
                if df.iloc[osszosorcount,1] =="Április":
                    window['-text3-'].update("Április")
                if df.iloc[osszosorcount,1] =="Május":
                    window['-text3-'].update("Május")
                if df.iloc[osszosorcount,1] =="Június":
                    window['-text3-'].update("Június")
                if df.iloc[osszosorcount,1] =="Július":
                    window['-text3-'].update("Július")
                if df.iloc[osszosorcount,1] =="Augusztus":
                    window['-text3-'].update("Augusztus")
                if df.iloc[osszosorcount,1] =="Szeptember":
                    window['-text3-'].update("Szeptember")
                if df.iloc[osszosorcount,1] =="Október":
                    window['-text3-'].update("Október")
                if df.iloc[osszosorcount,1] =="November":
                    window['-text3-'].update("November")
                if df.iloc[osszosorcount,1] =="December":
                    window['-text3-'].update("December")
                progval=osszosorcount
                window['-PROGRESS_BAR-'].update(progval)
                
                window['-text-'].update(str(progval) + "/" +str(osszosorcount3-1))
                
                window['-text2-'].update(str(muv) + "/5,192,334")
            

        
            srar=0
            trutr=True
            zak=['semmi','semmi','zakuszka','semmi']
            # ablak layout
            layout_jan =[[sg.Column(columnJan, scrollable=True, key='__COLSAVA'),sg.Column(columnJan2, scrollable=True)]]
            
            layout_feb =[[sg.Column(columnFeb, scrollable=True),sg.Column(columnFeb2, scrollable=True)]]
            
            layout_marc =[[sg.Column(columnMarc, scrollable=True),sg.Column(columnMarc2, scrollable=True)]]
            
            layout_apr =[[sg.Column(columnApr, scrollable=True),sg.Column(columnApr2, scrollable=True)]]
            
            layout_maj =[[sg.Column(columnMaj, scrollable=True),sg.Column(columnMaj2, scrollable=True)]]
            
            layout_jun =[[sg.Column(columnJun, scrollable=True),sg.Column(columnJun2, scrollable=True)]]
           
            layout_jul =[[sg.Column(columnJul, scrollable=True),sg.Column(columnJul2, scrollable=True)]]
            
            layout_aug =[[sg.Column(columnAug, scrollable=True),sg.Column(columnAug2, scrollable=True)]]
            
            layout_szep =[[sg.Column(columnSzept, scrollable=True),sg.Column(columnSzep2, scrollable=True)]]
           
            layout_okt =[[sg.Column(columnOkt, scrollable=True),sg.Column(columnOkt2, scrollable=True)]]
            
            layout_nov =[[sg.Column(columnNov, scrollable=True),sg.Column(columnNov2, scrollable=True)]]
            
            layout_dec =[[sg.Column(columnDec, scrollable=True),sg.Column(columnDec2, scrollable=True)]]
            command = ['Savanyitó', 'Egyéb']
            
            layout2+= [[sg.T("")],
                [
                    sg.TabGroup([[sg.Tab('Január', layout_jan, right_click_menu=['&Right', command]), sg.Tab('Február', layout_feb, right_click_menu=['&Right', command]), sg.Tab('Március', layout_marc, right_click_menu=['&Right', command]),
                    sg.Tab('Április', layout_apr, right_click_menu=['&Right', command]), sg.Tab('Május', layout_maj, right_click_menu=['&Right', command]), sg.Tab('Június', layout_jun, right_click_menu=['&Right', command]),
                    sg.Tab('Július', layout_jul, right_click_menu=['&Right', command]), sg.Tab('Augusztus', layout_aug, right_click_menu=['&Right', command]),
                    sg.Tab('Szeptember', layout_szep, right_click_menu=['&Right', command]), sg.Tab('Október', layout_okt, right_click_menu=['&Right', command]),
                    sg.Tab('November', layout_nov, right_click_menu=['&Right', command]), sg.Tab('December', layout_dec, right_click_menu=['&Right', command])]], size=(800,1200))],[sg.VerticalSeparator()]]
            if voltteteljan==False:
                layout2+=[[sg.T(" ",key='__MINDENMAS')],[sg.T(" ",key='__SAVA')]]
            if volttetelfeb==False:
                layout2+=[[sg.T(" ",key='__MINDENMASFeb')],[sg.T(" ",key='__SAVAFeb')]]
            if volttetelmar==False:
                layout2+=[[sg.T(" ",key='__MINDENMASMar')],[sg.T(" ",key='__SAVAMar')]]
            if volttetelapr==False:
                layout2+=[[sg.T(" ",key='__MINDENMASApr')],[sg.T(" ",key='__SAVAApr')]]
            if volttetelmaj==False:
                layout2+=[[sg.T(" ",key='__MINDENMASMaj')],[sg.T(" ",key='__SAVAMaj')]]
            if voltteteljun==False:
                layout2+=[[sg.T(" ",key='__MINDENMASJun')],[sg.T(" ",key='__SAVAJun')]]
            if voltteteljul==False:
                layout2+=[[sg.T(" ",key='__MINDENMASJul')],[sg.T(" ",key='__SAVAJul')]]
            if volttetelaug==False:
                layout2+=[[sg.T(" ",key='__MINDENMASAug')],[sg.T(" ",key='__SAVAAug')]]
            if volttetelszep==False:
                layout2+=[[sg.T(" ",key='__MINDENMASSzep')],[sg.T(" ",key='__SAVASzep')]]
            if volttetelokt==False:
                layout2+=[[sg.T(" ",key='__MINDENMASOkt')],[sg.T(" ",key='__SAVAOkt')]]
            if volttetelnov==False:
                layout2+=[[sg.T(" ",key='__MINDENMASNov')],[sg.T(" ",key='__SAVANov')]]
            if voltteteldec==False:
                layout2+=[[sg.T(" ",key='__MINDENMASDec')],[sg.T(" ",key='__SAVADec')]]

            layout3=layout2
            obj = ToltEsMent(layout3)
            ToltEsMent.save_object(obj)

            window2 = sg.Window('Időszaki Számoló', layout2, size=(1000,1500),resizable=True)
            graphs = [DashGraph(window2['_CPU_'+str(i)+'_GRAPH_'],
                                window2['_CPU_'+str(i) + '_TXT_'],
                                0, colors[i % 6]) for i in range(num_cores)]
            window.close()
            
            firstenter=True
            while True:
                
                event2, values2 = window2.read(timeout=POLL_FREQUENCY)
                if firstenter== True:
                    window2['__MINDENMAS'].update(visible=False)
                    window2['__MINDENMASFeb'].update(visible=False)
                    window2['__MINDENMASMar'].update(visible=False)
                    window2['__MINDENMASApr'].update(visible=False)
                    window2['__MINDENMASMaj'].update(visible=False)
                    window2['__MINDENMASJun'].update(visible=False)
                    window2['__MINDENMASJul'].update(visible=False)
                    window2['__MINDENMASAug'].update(visible=False)
                    window2['__MINDENMASSzep'].update(visible=False)
                    window2['__MINDENMASOkt'].update(visible=False)
                    window2['__MINDENMASNov'].update(visible=False)
                    window2['__MINDENMASDec'].update(visible=False) 
                    firstenter=False
                stats = psutil.cpu_percent(percpu=True)
                for i, util in enumerate(stats):
                    graphs[i].graph_percentage_abs(util)
                    graphs[i].text_display('{} CPU {:2.0f}'.format(i, util))
                    
                if event2 == sg.WIN_CLOSED or event2=="Exit":
                    
                    quit()
                if event2 == 'Savanyitó':
                        
                                window2['__MINDENMAS'].update(visible=False)
                                window2['__SAVA'].update(visible=True)
                        
                                window2['__MINDENMASFeb'].update(visible=False)
                                window2['__SAVAFeb'].update(visible=True)
                        
                                window2['__MINDENMASMar'].update(visible=False)
                                window2['__SAVAMar'].update(visible=True)
                        
                                window2['__MINDENMASApr'].update(visible=False)
                                window2['__SAVAApr'].update(visible=True)
                        
                                window2['__MINDENMASMaj'].update(visible=False)
                                window2['__SAVAMaj'].update(visible=True)
                        
                                window2['__MINDENMASJun'].update(visible=False)
                                window2['__SAVAJun'].update(visible=True)
                        
                                window2['__MINDENMASJul'].update(visible=False)
                                window2['__SAVAJul'].update(visible=True)
                        
                                window2['__MINDENMASAug'].update(visible=False)
                                window2['__SAVAAug'].update(visible=True)
                        
                                window2['__MINDENMASSzep'].update(visible=False)
                                window2['__SAVASzep'].update(visible=True)
                        
                                window2['__MINDENMASOkt'].update(visible=False)
                                window2['__SAVAOkt'].update(visible=True)
                       
                                window2['__MINDENMASNov'].update(visible=False)
                                window2['__SAVANov'].update(visible=True)
                       
                                window2['__MINDENMASDec'].update(visible=False) 
                                window2['__SAVADec'].update(visible=True)
                if event2 == 'Egyéb':
                    window2['__SAVA'].update(visible=False)
                    window2['__SAVAFeb'].update(visible=False)
                    window2['__SAVAMar'].update(visible=False)
                    window2['__SAVAApr'].update(visible=False)
                    window2['__SAVAMaj'].update(visible=False)
                    window2['__SAVAJun'].update(visible=False)
                    window2['__SAVAJul'].update(visible=False)
                    window2['__SAVAAug'].update(visible=False)
                    window2['__SAVASzep'].update(visible=False)
                    window2['__SAVAOkt'].update(visible=False)
                    window2['__SAVANov'].update(visible=False)
                    window2['__SAVADec'].update(visible=False)
                    window2['__MINDENMAS'].update(visible=True) 
                    window2['__MINDENMASFeb'].update(visible=True)
                    window2['__MINDENMASMar'].update(visible=True)
                    window2['__MINDENMASApr'].update(visible=True)
                    window2['__MINDENMASMaj'].update(visible=True)
                    window2['__MINDENMASJun'].update(visible=True)
                    window2['__MINDENMASJul'].update(visible=True)
                    window2['__MINDENMASAug'].update(visible=True)
                    window2['__MINDENMASSzep'].update(visible=True)
                    window2['__MINDENMASOkt'].update(visible=True)
                    window2['__MINDENMASNov'].update(visible=True)
                    window2['__MINDENMASDec'].update(visible=True)      
                    
                    
            
        break
   

                
            
if vegeprogi==False:         
 if __name__ == "__main__":
    main()


    
