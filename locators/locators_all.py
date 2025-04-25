from selenium.webdriver.common.by import By

#register
First_Name = (By.XPATH, "//input[@ng-model ='FirstName']")
Last_Name = (By.XPATH,"//input[@ng-model ='LastName']")
Address = (By.XPATH,"//textarea[@rows ='3']")
Email = (By.XPATH,"//input[@type ='email']")
Phone = (By.XPATH,"//input[@type ='tel']")
Gender = (By.XPATH,"//input[@value ='Male']")
Hobbies = (By.XPATH,"//input[@value ='Cricket']")
#Languages = (By.XPATH,"//div[contains(text(),'Bulgarian')]")
Skills = (By.XPATH,"//option[contains(text(),'Android')]")
#Country = (By.XPATH,"//option[contains(text(),'Denmark')]")
Dateofbirth_year = (By.XPATH,"//option[contains(text(),'1918')]")
Dateofbirth_month = (By.XPATH,"//option[contains(text(),'August')]")
Dateofbirth_day = (By.XPATH,"//option[@value='31']")
Password = (By.XPATH,"//input[@id='firstpassword']")
Confirm_Password = (By.XPATH,"//input[@id='secondpassword']")
Submit_button = (By.XPATH,"//button[@id='submitbtn']")


#switch to
Switch_To = (By.XPATH,"//a[contains(text(),'SwitchTo')]")

#alerts
Alerts = (By.XPATH,"//a[contains(text(),'Alerts')]")
click_button_1 = (By.XPATH,"//button[@onclick='alertbox()']")
#windows
Windows = (By.XPATH,"//a[contains(text(),'Windows')]")
click_button = (By.XPATH,"//button[@class='btn btn-info']")






