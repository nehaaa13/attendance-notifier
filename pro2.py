import pandas as pd
import pywhatkit as kit
from datetime import datetime


current_date = datetime.now().strftime("%d-%m-%Y")


df = pd.read_excel('Attendance2.xlsx') 

for index, row in df.iterrows():
    student_name = row['Student Name']
    Theory = row['Theory (%)']
    Practical = row['Practical (%)']
    phone_number = row['Parent Phone Number'] 
    

   
    message = (
          f"Subject: Attendance Notification for {student_name}\n\n"
            f"Dear Parent,\n\n"
            f"I am writing to inform you that your child, {student_name}, has an attendance percentage of {Theory}% in Theory classes and {Practical}% in Practical classes till 14/11/2024. "
            f"Please note that our policy requires a minimum attendance of 75% for academic success in both theory and practical classes.\n\n"
            f"We encourage you to discuss the importance of regular attendance with your child. If you have any questions, feel free to reach out.\n\n"
            f"Best regards,\n\n"
            
          f"HOD, Dept. of Applied Chemistry\n"
          f"Shri G.S. Inst. of Tech. and Sc. Indore(MP)\n"
          f"{current_date}"
    )
        
       
    kit.sendwhatmsg_instantly(f"+{phone_number}", message)
        
    print(f"Message sent to {student_name}'s parent")
    