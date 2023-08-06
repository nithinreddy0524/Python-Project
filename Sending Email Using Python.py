import smtplib
def validation(Email):
    k,j,d=0,0,0
    if len(Email)>=6:
      if Email[0].isalpha():
        if ('@' in Email) and (Email.count('@')==1):
          if (Email[-3]=='.') ^ (Email[-4]=='.') :
            for i in Email:
              if i==i.isspace():
                k=1
                
              elif i.isalpha():
                if i==i.upper():
                  j=1
              elif i.isdigit():
                continue
              elif i=='_' or i=='@' or i=='.' :
                continue
              else:
                d=1
            if k==1 or j==1 or k==1 :
              print("Please Enter Correct Email...")
              return False
          else:
            print("Please Enter Correct Email...")
            return False
            
        else:
          print("Please Enter Correct Email...")
          return False
      else:
        print("Please Enter Correct Email...")
        return False
    else:
      print("Please Enter Correct Email...")
      return False
    return True
semail=input("Enter the Sender Email : ")
K = validation(semail)
while not K:
    semail=input("Enter the Sender Email : ")
    K = validation(semail)
print("Note:please enter App password only (less secure apps) for gmail users")
password=input("Enter the Password : ")
smtobj=smtplib.SMTP("smtp.gmail.com",587)
smtobj.ehlo()
smtobj.starttls()
smtobj.login(semail,password)
print("Login successful")
remail=input("Enter the Recipient Email : ")
K=validation(remail)
while not K:
    remail=input("Enter the Recipient Email : ")
    K = validation(remail)
message=input("Enter the Message : ")
smtobj.sendmail(semail,remail,message)
print("Mail Sent successfully")
smtobj.quit()
input("Please Press Enter to Exit")