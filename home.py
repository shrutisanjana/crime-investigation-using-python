from tkinter import ttk 
from tkinter import *
import os
from PIL import ImageTk,Image #pip install pillow
from tkinter import messagebox


if os.path.isfile('databases/ids.dat'):
    pass
else:
    os.system("mkdir databases")
    file=open('databases/ids.dat',"w")
    file.write("0000000,000000,0000000,0000000")
    file.close()
    file=open('databases/station.dat',"w")
    file.close()
    file=open('databases/officers.dat',"w")
    file.close()
    file=open('databases/cases.dat',"w")
    file.close()
    file=open('databases/criminalinfo.dat',"w")
    file.close()

class home:
  def __init__(self,root):
            self.root=root
            self.root.title("Stations")
            #====BG Image====
            image2=Image.open("crime_station.png")
            self.bg=ImageTk.PhotoImage(image2)
            self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
            self.w = self.bg.width()
            self.h = self.bg.height()
            root.geometry('{}x{}'.format(self.w,self.h))

            self.Frame_Station=Frame(self.root)

            #components
            self.logout_button=Button(self.root,command=self.logout_function, cursor="hand2",text="Logout",bg="#333333",fg="#ffffff",font=("Calibri",20))
            self.logout_button.place(x=0,y=0,width=205,height=40)
            
            self.case_entry=Button(self.root,command=self.caseEntry_function, cursor="hand2",text="Case Entry",bg="#333333",fg="#ffffff",font=("Calibri",20))
            self.case_entry.place(x=205,y=0,width=205,height=40)
            
            self.station_entry=Button(self.root,command=self.stationEntry_function, cursor="hand2",text="Station Entry",bg="#333333",fg="#ffffff",font=("Calibri",20))
            self.station_entry.place(x=410,y=0,width=205,height=40)
            
            self.officer_entry=Button(self.root,command=self.officerEntry_function, cursor="hand2",text="Officer Entry",bg="#333333",fg="#ffffff",font=("Calibri",20))
            self.officer_entry.place(x=610,y=0,width=205,height=40)
            
            self.criminal_entry=Button(self.root,command=self.criminalEntry_function, cursor="hand2",text="Criminal Entry",bg="#333333",fg="#ffffff",font=("Calibri",20))
            self.criminal_entry.place(x=815,y=0,width=205,height=40)
            
            self.status=Button(self.root,command=self.showCases_function, cursor="hand2",text="Case Chart",bg="#333333",fg="#ffffff",font=("Calibri",20))
            self.status.place(x=1020,y=0,width=205,height=40)

            #counters for different entries.
            self.station_count=0
            self.officers_count=0
            self.cases_solved=0
            self.cases_pending=0
            self.crime_count=0

            #calling counter function
            self.counter_function()

            

            


  def counter_function(self):
        #conting entries in station Database
        file=open('databases/station.dat',"r")
        data=file.read()
        file.close()
        data=list(data.split(","))
        self.station_count=len(data)-1

        #counting entries in officers Database
        file=open('databases/officers.dat',"r")
        data=file.read()
        file.close()
        data=list(data.split(","))
        self.officers_count=len(data)-1

        #counting entries in cases Database
        file=open('databases/cases.dat',"r")
        data=file.read()
        file.close()
        self.cases_solved=data.count("solved")
        self.cases_pending=data.count("UnSolved")
        data=list(data.split(","))
        self.cases_count=len(data)-1

        #updating labels
        #labels for respective counter
        self.station_count_label=Label(self.root,text="Stations\n{}".format(str(self.station_count)),font=("Impact",25,"bold"),fg="darkgreen",bg="lightgreen").place(width=240,height=146,x=0,y=40)
        self.officers_count_label=Label(self.root,text="Officers\n{}".format(str(self.officers_count)),font=("Impact",25,"bold"),fg="white",bg="orange").place(width=240,height=146,x=0,y=186)
        self.cases_solved_label=Label(self.root,text="Cases Solved\n{}".format(str(self.cases_solved)),font=("Impact",25,"bold"),fg="#ffffff",bg="skyblue").place(width=240,height=146,x=0,y=332)
        self.cases_pending_label=Label(self.root,text="Cases Pending\n{}".format(str(self.cases_pending)),font=("Impact",25,"bold"),fg="#ffffff",bg="#eb9b9b").place(width=240,height=146,x=0,y=478)
        self.crime_count_label=Label(self.root,text="Crime Entries\n{}".format(str(self.cases_count)),font=("Impact",25,"bold"),fg="#373d02",bg="#9bc39b").place(width=240,height=146,x=0,y=624)
  def logout_function(self):
        self.root.destroy()


  def caseEntry_function(self):

            #destroyin previous frame
            self.Frame_Station.destroy()

            #creating new frame
            self.Frame_Station=Frame(self.root)
            self.Frame_Station.place(x=(self.w//2)-150,y=(self.h//2)-325,height=700,width=500)


            title=Label(self.Frame_Station,text="Case Entry",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=140,y=30)
            desc=Label(self.Frame_Station,text="Station registration area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="yellow")
            desc.place(relx=50,rely=100)

            lbl_name=Label(self.Frame_Station,text="Type",font=("Goudy old style",15,"bold"),fg="black").place(x=60,y=140)
            self.txt_type=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_type.place(x=50,y=170,width=400,height=35)

            
            lbl_name=Label(self.Frame_Station,text="Victim Name",font=("Goudy old style",15,"bold"),fg="black").place(x=60,y=210)
            self.txt_vic=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_vic.place(x=50,y=240,width=400,height=35)

            lbl_loc=Label(self.Frame_Station,text="Location of happening",font=("Goudy old style",15,"bold"),fg="black").place(x=60,y=280)
            self.txt_loc=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_loc.place(x=50,y=310,width=400,height=35)

            

            lbl_stationIn=Label(self.Frame_Station,text="Evidences slash('/') seperated",font=("Goudy old style",15,"bold"),fg="black").place(x=60,y=350)
            self.txt_evidence=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_evidence.place(x=50,y=380,width=400,height=35)

            lbl_stationIn=Label(self.Frame_Station,text="Status",font=("Goudy old style",15,"bold"),fg="black").place(x=60,y=420)
            self.txt_stat=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_stat.place(x=50,y=450,width=400,height=35)

            lbl_stationIn=Label(self.Frame_Station,text="Officer Assigned",font=("Goudy old style",15,"bold"),fg="black").place(x=60,y=490)
            self.txt_off=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_off.place(x=50,y=520,width=400,height=35)
            
            Register_btn=Button(self.root,command=self.station_function, cursor="hand2",text="Register",bg="red",fg="#ffffff",font=("times new roman",20)).place(x=self.w//2+10,y=620,width=180,height=40)

            self.status=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.suspect=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.status.place(x=150,y=600,width=200,height=35)
            self.suspect.place(x=0,y=650,width=500,height=35)
            self.suspect.insert(0,"Suspects:")
            self.status.insert(0,"leave Empty")


  def stationEntry_function(self):

            #destroyin previous frame
            self.Frame_Station.destroy()

            #creating new frame
            self.Frame_Station=Frame(self.root)
            self.Frame_Station.place(x=(self.w//2)-100,y=(self.h//2)-325,height=650,width=400)


            
            title=Label(self.Frame_Station,text="Station Entry",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=40,y=30)
            desc=Label(self.Frame_Station,text="Station registration area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="yellow")
            desc.place(relx=30,rely=100)


            lbl_name=Label(self.Frame_Station,text="Name",font=("Goudy old style",15,"bold"),fg="black").place(x=40,y=210)
            self.txt_name=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_name.place(x=30,y=240,width=350,height=35)

            lbl_loc=Label(self.Frame_Station,text="Location",font=("Goudy old style",15,"bold"),fg="black").place(x=40,y=280)
            self.txt_loc=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_loc.place(x=30,y=310,width=350,height=35)

            

            lbl_stationIn=Label(self.Frame_Station,text="Station Incharge",font=("Goudy old style",15,"bold"),fg="black").place(x=40,y=350)
            self.txt_StationIn=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_StationIn.place(x=30,y=380,width=350,height=35)
            
            

            cancel_btn=Button(self.Frame_Station,text="Cancel",cursor="hand2",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=30,y=420)
            Register_btn=Button(self.root,command=self.newStationTodb, cursor="hand2",text="Register",bg="red",fg="#ffffff",font=("times new roman",20)).place(x=self.w//2+10,y=520,width=180,height=40)
            
            

  def officerEntry_function(self):

            #destroyin previous frame
            self.Frame_Station.destroy()

            #creating new frame
            self.Frame_Station=Frame(self.root)
            self.Frame_Station.place(x=(self.w//2)-100,y=(self.h//2)-325,height=650,width=400)


            

            title=Label(self.Frame_Station,text="New Officer Entry",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=40,y=30)
            desc=Label(self.Frame_Station,text="Station registration area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="yellow")
            desc.place(relx=30,rely=100)

            lbl_name=Label(self.Frame_Station,text="Name",font=("Goudy old style",15,"bold"),fg="black").place(x=40,y=140)
            self.txt_name=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_name.place(x=30,y=170,width=350,height=35)

            
            lbl_name=Label(self.Frame_Station,text="Station Name",font=("Goudy old style",15,"bold"),fg="black").place(x=40,y=210)
            self.txt_station=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_station.place(x=30,y=240,width=350,height=35)

            lbl_loc=Label(self.Frame_Station,text="Position of Officer",font=("Goudy old style",15,"bold"),fg="black").place(x=40,y=280)
            self.txt_pos=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_pos.place(x=30,y=310,width=350,height=35)

            

            lbl_stationIn=Label(self.Frame_Station,text="CaseId Assigned",font=("Goudy old style",15,"bold"),fg="black").place(x=40,y=350)
            self.txt_caseid=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_caseid.place(x=30,y=380,width=350,height=35)

            

            Register_btn=Button(self.root,command=self.newOfficerToDb_function, cursor="hand2",text="Register",bg="red",fg="#ffffff",font=("times new roman",20)).place(x=self.w//2+10,y=520,width=180,height=40)

  def criminalEntry_function(self):

            #destroyin previous frame
            self.Frame_Station.destroy()

            #creating new frame
            self.Frame_Station=Frame(self.root)
            self.Frame_Station.place(x=(self.w//2)-100,y=(self.h//2)-325,height=650,width=400)


            title=Label(self.Frame_Station,text="Criminal Entry",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=40,y=30)
            desc=Label(self.Frame_Station,text="Station registration area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="yellow")
            desc.place(relx=30,rely=100)

            lbl_name=Label(self.Frame_Station,text="Name",font=("Goudy old style",15,"bold"),fg="black").place(x=40,y=140)
            self.txt_name=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_name.place(x=30,y=170,width=350,height=35)

            
            lbl_name=Label(self.Frame_Station,text="Crime Name",font=("Goudy old style",15,"bold"),fg="black").place(x=40,y=210)
            self.txt_crime=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_crime.place(x=30,y=240,width=350,height=35)

            lbl_loc=Label(self.Frame_Station,text="Last Location",font=("Goudy old style",15,"bold"),fg="black").place(x=40,y=280)
            self.txt_loc=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_loc.place(x=30,y=310,width=350,height=35)

            

            lbl_stationIn=Label(self.Frame_Station,text="Belonging slash('/') seperated",font=("Goudy old style",15,"bold"),fg="black").place(x=40,y=350)
            self.txt_belong=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_belong.place(x=30,y=380,width=350,height=35)

            lbl_stationIn=Label(self.Frame_Station,text="Prison Status",font=("Goudy old style",15,"bold"),fg="black").place(x=40,y=420)
            self.txt_stat=Entry(self.Frame_Station,font=("times new roman",15),bg="lightgray")
            self.txt_stat.place(x=30,y=450,width=350,height=35)

            
            Register_btn=Button(self.root,command=self.newCriminalToDb_function, cursor="hand2",text="Register",bg="red",fg="#ffffff",font=("times new roman",20)).place(x=self.w//2+10,y=620,width=180,height=40)


  def showCases_function(self):

            #destroyin previous frame
            self.Frame_Station.destroy()

            #creating new frame
            self.Frame_Station=Frame(self.root)
            self.Frame_Station.place(x=(self.w//2)-250,y=(self.h//2)-325,height=650,width=800)
            title=Label(self.Frame_Station,text="Case Entries",font=("Impact",35,"bold"),fg="#d77337").place(x=250,y=0)

            
            #creating treeview
            treev = ttk.Treeview(self.Frame_Station, selectmode ='browse',height=25) 
            treev.place(x=0,y=100)
            # Calling pack method w.r.to treeview 
            treev.pack(side ='right') 
              
            # Constructing vertical scrollbar 
            # with treeview 
            verscrlbar = ttk.Scrollbar(self.Frame_Station,  
                                       orient ="vertical",  
                                       command = treev.yview) 
              
            # Calling pack method w.r.to verical  
            # scrollbar 
            verscrlbar.pack(side ='right', fill ='y') 
              
            # Configuring treeview 
            treev.configure(xscrollcommand = verscrlbar.set) 
              
            # Defining number of columns 
            treev["columns"] = ("1", "2", "3","4","5","6","7") 
              
            # Defining heading 
            treev['show'] = 'headings'
              
            # Assigning the width and anchor to  the 
            # respective columns 
            treev.column("1", width = 60, anchor ='c') 
            treev.column("2", width = 100, anchor ='se') 
            treev.column("3", width = 110, anchor ='se')
            treev.column("4", width = 100, anchor ='se')
            treev.column("5", width = 220, anchor ='se')
            treev.column("6", width = 80, anchor ='se')
            treev.column("7", width = 110, anchor ='se')
              
            # Assigning the heading names to the  
            # respective columns 
            treev.heading("1", text ="id") 
            treev.heading("2", text ="Type") 
            treev.heading("3", text ="Victim Name")
            treev.heading("4", text ="Location")
            treev.heading("5", text ="Evidence")
            treev.heading("6", text ="Status")
            treev.heading("7", text ="Officer Assigned")

            
            #creating text data size from cases database
            #opening file
            file=open("databases/cases.dat","r")
            data=file.read()
            data=list(data.split(","))
            try:
              for i in range(len(data)):
                data[i]=list(data[i].split("|"))
                data[i][0]=data[i][0][1:]
                data[i][6]=data[i][6][0:-1]
                data[i]=tuple(data[i])
                treev.insert("", 'end', text ="L1",  
               values =data[i])
            except:
                pass
            data.pop()
            total_rows = len(data) 
            total_columns = len(data[0])
                        
            
            
            
  #functioning functions......

  def newStationTodb(self):
            file=open("databases/station.dat","r")
            data=file.read()
            file=open("databases/station.dat","at")
            if self.txt_StationIn.get()=="" or self.txt_name.get()=="" or self.txt_loc.get()=="":
                print("every field should be filled.")
                return
            else:
                #getting and writing unique id for stations
                id_file=open('databases/ids.dat',"r")
                ids=id_file.read()
                ids=list(ids.split(","))
                file.write("[")
                s_id=str(int(ids[0])+1)+"|"
                ids[0]=str(int(ids[0])+1)
                string="{},{},{},{}".format(ids[0],ids[1],ids[2],ids[3])
                id_file=open('databases/ids.dat',"w")
                id_file.write(string)
                id_file.close()
                file.write(s_id)
                

                #getting data from Entry Fields
                s_name=self.txt_name.get()+"|"
                self.txt_name.delete(0,'end')
                file.write(s_name)
                s_loc=self.txt_loc.get()+"|"
                self.txt_loc.delete(0,'end')
                file.write(s_loc)
                s_in=self.txt_StationIn.get()+"],"
                self.txt_StationIn.delete(0,'end')
                file.write(s_in)
                print("inserted.")
                file.close()
                self.counter_function()
                return



  def newOfficerToDb_function(self):
            file=open('databases/officers.dat',"r")
            data=file.read()
            file=open('databases/officers.dat',"at")
            if self.txt_name.get()=="" or self.txt_station.get()=="" or self.txt_pos.get()=="":
                print("every field should be filled.")
                return
            else:
                #getting and writing unique id for stations
                id_file=open('databases/ids.dat',"r")
                ids=id_file.read()
                ids=list(ids.split(","))
                file.write("[")
                o_id=str(int(ids[1])+1)+"|"
                ids[1]=str(int(ids[1])+1)
                string="{},{},{},{}".format(ids[0],ids[1],ids[2],ids[3])
                id_file=open('databases/ids.dat',"w")
                id_file.write(string)
                id_file.close()
                file.write(o_id)


                
                o_name=self.txt_name.get()+"|"
                self.txt_name.delete(0,'end')
                file.write(o_name)
                o_station=self.txt_station.get()+"|"
                self.txt_station.delete(0,'end')
                file.write(o_station)
                o_pos=self.txt_pos.get()+"|"
                self.txt_pos.delete(0,'end')
                file.write(o_pos)
                o_case=self.txt_caseid.get()+"],"
                self.txt_caseid.delete(0,'end')
                file.write(o_case)
                print("inserted.")
                file.close()
                self.counter_function()
                return

  def newCriminalToDb_function(self):
            file=open('databases/criminalinfo.dat',"r")
            data=file.read()
            file=open('databases/criminalinfo.dat',"at")
            if self.txt_name.get()=="" or self.txt_stat.get()=="" or self.txt_loc.get()=="" or self.txt_belong.get()=="" or self.txt_crime.get()=="":
                print("every field should be filled.")
                return
            else:
                #getting and writing unique id for stations
                id_file=open('databases/ids.dat',"r")
                ids=id_file.read()
                ids=list(ids.split(","))
                file.write("[")
                c_id=str(int(ids[3])+1)+"|"
                ids[3]=str(int(ids[3])+1)
                string="{},{},{},{}".format(ids[0],ids[1],ids[2],ids[3])
                id_file=open('databases/ids.dat',"w")
                id_file.write(string)
                id_file.close()
                file.write(c_id)


                
                c_name=self.txt_name.get()+"|"
                self.txt_name.delete(0,'end')
                file.write(c_name)
                c_crime=self.txt_crime.get()+"|"
                self.txt_crime.delete(0,'end')
                file.write(c_crime)
                c_loc=self.txt_loc.get()+"|"
                self.txt_loc.delete(0,'end')
                file.write(c_loc)
                c_belong=self.txt_belong.get()+"|"
                self.txt_belong.delete(0,'end')
                file.write(c_belong)
                c_stat=self.txt_stat.get()+"],"
                self.txt_stat.delete(0,'end')
                file.write(c_stat)
                print("inserted.")
                file.close()
                self.counter_function()
                return
              
            
  def susp_fun(self):
            sus=""
            criminal_file=open('databases/criminalinfo.dat',"rt")
            C_data=criminal_file.read()
            C_data=list(C_data.split(","))
            criminal_file.close()
            loc=self.txt_loc.get()
            for i in C_data:
                i=list(i.split("|"))
                if loc in i:
                    sus=sus+","+i[1]
            self.suspect.insert(10,sus)
            sus=list(sus.split(","))
            return sus
                    
  def solve(self,suspect):
            crminal_file=open('databases/criminalinfo.dat',"rt")
            C_data=crminal_file.read()
            C_data=list(C_data.split(","))
            crminal_file.close()
            evidences=self.txt_evidence.get()
            evidences=evidences.split("/")
            for i in evidences:
                for name in suspect:
                    for j in C_data:
                        if j.find(i) >= 0 and j.find(name)>=0:
                            self.txt_stat.delete(0,'end')
                            self.txt_stat.insert(0,'solved')
                            criminal_data=list(j.split("|"))
                            c_name="Criminal:"+criminal_data[1]
                            self.status.delete(0,'end')
                            self.status.insert(0,c_name)
                            break
                        else:
                            self.txt_stat.delete(0,'end')
                            self.txt_stat.insert(0,'UnSolved')
                            self.status.delete(0,'end')
                            self.status.insert(0,'Investigation Needed!!')
            print(C_data)
  def station_function(self):
            self.suspect.delete(0,'end')
            self.suspect.insert(0,"Suspects:")
            self.status.delete(0,'end')
            self.status.insert(0,"leave Empty")
            names=self.susp_fun()
            self.solve(names)
            file=open('databases/cases.dat',"r")
            data=file.read()
            file=open('databases/cases.dat',"at")
            if self.txt_type.get()=="" or self.txt_stat.get()=="" or self.txt_off.get()=="" or self.txt_loc.get()=="" or self.txt_vic.get()=="":
                print("every field should be filled.")
                return
            else:
                #getting and writing unique id for stations
                id_file=open('databases/ids.dat',"r")
                ids=id_file.read()
                ids=list(ids.split(","))
                file.write("[")
                c_id=str(int(ids[2])+1)+"|"
                ids[2]=str(int(ids[2])+1)
                string="{},{},{},{}".format(ids[0],ids[1],ids[2],ids[3])
                id_file=open('databases/ids.dat',"w")
                id_file.write(string)
                id_file.close()
                file.write(c_id)


                
                c_type=self.txt_type.get()+"|"
                self.txt_type.delete(0,'end')
                file.write(c_type)
                c_vic=self.txt_vic.get()+"|"
                self.txt_vic.delete(0,'end')
                file.write(c_vic)
                c_loc=self.txt_loc.get()+"|"
                self.txt_loc.delete(0,'end')
                file.write(c_loc)
                c_evid=self.txt_evidence.get()+"|"
                self.txt_evidence.delete(0,'end')
                file.write(c_evid)
                c_stat=self.txt_stat.get()+"|"
                file.write(c_stat)
                c_off=self.txt_off.get()+"],"
                self.txt_off.delete(0,'end')
                file.write(c_off)
                print("inserted.")
                file.close()
                self.counter_function()
                return
root=Tk()
root.resizable(False,False)
obj=home(root)
mainloop()
