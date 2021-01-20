from bs4 import BeautifulSoup
from save import save_to_file
from Page import getPage
def oneFile(url,num):
    def makeTextlist(value):
      spl=value.text.strip().split('\n')
      spl[1]="("+spl[1]+")"
      return "".join(spl)
    pageText=getPage(url)
    soup=BeautifulSoup(pageText,"html.parser")
    Sec=soup.find("section",{"class":"bg-lightgray section-sm"}).find("p").find("a").text
    ParticipaintList=list(map(makeTextlist,soup.find("table",{"id":"datatable-PART_P_OC"}).find("tbody").find_all("tr")))
    ObserveList=list(map(makeTextlist,soup.find("table",{"id":"datatable-PART_O_OC"}).find("tbody").find_all("tr")))
    pLen=len(ParticipaintList)
    oLen=len(ObserveList)
    lis=[]
    for i in range(0,max(oLen,pLen)):
        
        if i>=pLen:
            ParticipaintList.append("")
        if i>=oLen:
            ObserveList.append("")
        line=[Sec,ParticipaintList[i],ObserveList[i]]
        lis.append(line)
    save_to_file(lis,num)