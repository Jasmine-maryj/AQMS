import numpy as nm  
import matplotlib.pyplot as mtp  
import pandas as pd
from tkinter import *
from tkinter import messagebox
import seaborn as sns
import PIL.Image
import sqlite3
import warnings

warnings.filterwarnings("ignore")


# %matplotlib inline
# plt.rcParadcdms.update({'figure.figsize':(7,5), 'figure.dpi':100})
def main():
    R1=Tk()
    R1.geometry('900x600')
    R1.title('SigUp Now')

    
    la=Label(R1,text="Air Quality Monitoring System",font=('algerian',15,'bold'))
    la.place(x=200,y=100)
    
    Registerbt = Button(R1,text = "REGISTER",width=17,height=2,font=('algerian',15,'bold'),justify='center',bg="light blue",relief=SUNKEN,command=sigup)
    loginbt = Button(R1,text = "LOGIN",width=17,height=2,font=('algerian',15,'bold'),justify='center',bg="light blue",relief=SUNKEN,command=login)
    Registerbt.place(x =300 ,y=200)
    loginbt.place( x =300,y=300)
    R1.mainloop()
    

def sigup():
    
    def Sigups():
        usernames = username.get()
        passwords = password.get()
        phonenos = phoneno.get()
        Address = address.get()
        conn = sqlite3.connect('w.db')
        with conn:
            cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS w1 (Username TEXT,Password TEXT,Phoneno TEXT,Address TEXT)')
        cursor.execute('INSERT INTO w1 (Username,Password ,Phoneno,Address) VALUES(?,?,?,?)',
                  (usernames,passwords,phonenos,Address,))
        conn.commit()
        if username.get() == "" or password.get() == "":
           messagebox.showinfo("sorry", "Pease fill the required information")
           login()
        else:
           messagebox.showinfo("Welcome to %s" % usernames, "Let Login")
           return
           
      
           
    
    R2=Toplevel()
    R2.geometry('900x600')
    R2.title('SigUp Now')
   
   
    lblInfo=Label(R2,text="Username",fg="black",font=("bold",15))
    lblInfo.place(x=200,y=140)

    lblInfo=Label(R2,text="Password",fg="black",font=("bold",15))
    lblInfo.place(x=200,y=190)

    lblInfo=Label(R2,text="phoneno",fg="black",font=("bold",15))
    lblInfo.place(x=200,y=240)

    lblInfo=Label(R2,text="Adress",fg="black",font=("bold",15))
    lblInfo.place(x=200,y=290)

    

    username=Entry(R2,width=20,font=("bold",15),highlightthickness=2)
    username.place(x=300,y= 140 )
    
    password=Entry(R2,show="**",width=20,font=("bold",15),highlightthickness=2)
    password.place(x=300,y=190 )
    
    phoneno=Entry(R2,width=20,font=("bold",15),highlightthickness=2)
    phoneno.place(x=300,y= 240 )
    
    address=Entry(R2,width=20,font=("bold",15),highlightthickness=2)
    address.place(x=300,y= 290 )

    

    signUpbt = Button(R2,text = "SignUp",width=10,height=2,fg="black",font=('algerian',15,'bold'),justify='center',bg="light blue",command=Sigups)
    signUpbt.place( x =350,y=490)
    
      
    R2.mainloop()



def login():
    def logininto():
        usernames = e1.get()
        passwords = e2.get()
        conn = sqlite3.connect('w.db')
        with conn:
          cursor=conn.cursor()
        ('CREATE TABLE IF NOT EXISTS w1 (Username TEXT,Password TEXT,Phoneno TEXT)')
        conn.commit()
        if usernames == "" and passwords == "" :
            messagebox.showinfo("sorry", "Please complete the required field")
        else:
            cursor.execute('SELECT * FROM w1 WHERE Username = "%s" and Password = "%s"'%(usernames,passwords))
            for i in usernames:
                if cursor.fetchall():
                    messagebox.showinfo("Welcome %s" % usernames, "Logged in successfully")
                    svm()
        
                else:
                    messagebox.showinfo("Sorry", "Wrong Password")
                    return
  
    
    R3 =Toplevel()
    R3.geometry('900x600')
    R3.title("LOGIN NOW")
    
   
    

    lblInfo=Label(R3,text="username",fg="black",font=("bold",15))
    lblInfo.place(x=230,y=200)
   
    lblInfo=Label(R3,text="Password",fg="black",font=("bold",15))
    lblInfo.place(x=230,y=250)

    e1= Entry(R3,width=15,font=("bold",17),highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e1.place(x=330, y=190)

    e2= Entry(R3,width=15,font=("bold",17),show="*",highlightthickness=2,bg="WHITE",relief=SUNKEN)
    e2.place(x=330, y=240)

    btn = Button(R3, text="LOGIN", width=10, height=2,fg="black",font=('algerian',15,'bold'),justify='center',bg="light blue",command=logininto)
    btn.place(x=380, y=400)
    
    R3.mainloop()



def svm():
    def svm1():
        import pickle
        NH3=E.get()
        CO=E1.get()


        result = classifier.predict([[NH3,CO]])
        print(result)
        message.configure(text= acc)
        message1.configure(text=result)

    df= pd.read_csv('./DATA.csv')
    #print(df)
    res=""
    x= df.iloc[:, [3,4]].values
    y= df.iloc[:, -1].values
    print(x)
    print("\n")
    print(y)
    # Splitting the dataset into training and test set.  
    from sklearn.model_selection import train_test_split  
    x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.20, random_state=0)



    from sklearn.svm import SVC # "Support vector classifier"  
    classifier = SVC()  
    classifier.fit(x_train, y_train)


    y_pred= classifier.predict(x_test)  
    x_pred= classifier.predict(x_train)
    #Y_pred=y_pred.astype(int)

    print('Train Score: ', classifier.score(x_train, y_train))  
    print('Test Score: ', classifier.score(x_test, y_test))

    #Creating the Confusion matrix  
    from sklearn.metrics import confusion_matrix  
    cm= confusion_matrix(y_test, y_pred)
    print("Printing Confusion matrix","\n",cm)
    from sklearn.metrics import accuracy_score
    acc=accuracy_score(y_test,y_pred)
    print("Printing Accuracy","\n",acc)


    #x_train=x_train.reshape(-1,1)
    x_train=nm.arange(0,len(x_train),1)
    x_test=nm.arange(0,len(x_test),1)
    #y_train=y_train.reshape(-1,1)
    #print(x_train.shape)
    #print(y_train.shape)

    #print(y_pred.shape)
    from sklearn.metrics import confusion_matrix
    import seaborn as sns
    cm= confusion_matrix(y_test, y_pred)
    ax = sns.heatmap(cm/nm.sum(cm), annot=True, 
                fmt='.2%', cmap='Blues')

    ax.set_title('Seaborn Confusion Matrix with labels\n\n');
    ax.set_xlabel('\nPredicted Values')
    ax.set_ylabel('Actual Values ')
    ## Display the visualization of the Confusion Matrix.

        
    R4 =Toplevel()
    R4.geometry('900x600')
    R4.title("LOGIN NOW")
    




    lblIn=Label(R4,text="NH3",fg="black",font=("bold",15))
    lblIn.place(x=200,y=150)

    lblIn=Label(R4,text="CO",fg="black",font=("bold",15))
    lblIn.place(x=200,y=200)


    
    lblIn=Label(R4,text="Accuracy",fg="black",font=("bold",15))
    lblIn.place(x=150,y=480)

    lblIn=Label(R4,text="Status",fg="black",font=("bold",15))
    lblIn.place(x=540,y=480)
    
    message =Label(R4, text="" ,bg="yellow"  ,fg="red"  ,width=30  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
    message.place(x=100, y=520)
    
    message1 =Label(R4, text="" ,bg="yellow"  ,fg="red"  ,width=30  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
    message1.place(x=400, y=520)

    
    E=DoubleVar()
    e1=Entry(R4,width=20,textvariable=E,font=("bold",15),highlightthickness=2)
    e1.place(x=300,y= 150)
    E1=DoubleVar()
    e2=Entry(R4,textvariable=E1,width=20,font=("bold",15),highlightthickness=2)
    e2.place(x=300,y=200)

    bt = Button(R4,text = "Get",width=17,height=2,font=('algerian',15,'bold'),justify='center',bg="light blue",relief=SUNKEN,command=svm1)
    bt.place(x =300 ,y=440)
    bt = Button(R4,text = "<--",width=10,height=2,font=('algerian',15,'bold'),justify='center',bg="light blue",relief=SUNKEN,command=main)
    bt.place(x =0 ,y=0)
    #message1.configure(text= res)
    R4.mainloop()

main()
