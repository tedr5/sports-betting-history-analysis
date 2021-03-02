from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import pandas

"""
PATH = "/home/thomas/Documents/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.unibet.fr/pari-sportif-poker")
driver.maximize_window()
#Fill username to connect
try:
    pseudo_tag_name = 'username'
    pseudo = WebDriverWait(driver,10).until(
     EC.presence_of_element_located((By.NAME,pseudo_tag_name))
    )
    pseudo_char = ''
    pseudo.send_keys(pseudo_char)
except:
    print('Fail pseudo')

#Fill password to connect
try:
    pswd_tag_name = 'password'
    pswd = WebDriverWait(driver,10).until(
     EC.presence_of_element_located((By.NAME,pswd_tag_name))
    )
    pswd_char = ''
    pswd.send_keys(pswd_char)
except:
    print('Fail password')

#Fill date of birth to connect
try:
    dob_tag_name = 'form-dob'
    dob = WebDriverWait(driver,10).until(
     EC.presence_of_element_located((By.NAME,dob_tag_name))
    )
    date_of_birth = ''
    dob.send_keys(date_of_birth)
except:
    print('Fail date of birth')

#Send command to press submit button
try:
    submit_class_name = 'submitbtn'
    submit = WebDriverWait(driver,10).until(
     EC.presence_of_element_located((By.CLASS_NAME,submit_class_name))
    )
    submit.click()
except:
    print('Not connected!')

#Go to betting history
try:
    history_locator = 'Mes paris sportifs'
    history = WebDriverWait(driver,10).until(
          EC.presence_of_element_located((By.LINK_TEXT,history_locator))
    )
    history.click()
except:
    print('Fail to get to history')

#Go to finished bet in betting history
try:
    xpath_finished_bet = '//*[@id="view-main"]/div/div/div/div/div/div/section[2]/div/div[1]/div/a[4]'
    finished = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH,xpath_finished_bet))
    )
    finished.click()
except:
    print('Fail to get to closed bet')

#//*[@id="view-main"]/div[48]/div/div[2]/div/div/div/div
##view-main > div.view.view-myaccount-bettinghistory.view-account.effeckt-page-active > div > div.scroller > div > div > div > div
#Extract all li which contains all bet in the main div
time_duration = 10
time_end = time.time() + 60 * time_duration
counter = 0
while time.time() < time_end:
    counter += 1
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="view-main"]/div/div/div/div/div/div/div/div/section/ul/div/div/div[1]/a')))
        element.click()
    except NoSuchElementException:
        break
    print(counter)
#Show all bet loaded

wrap_bets = driver.find_element_by_class_name('history-container')
driver.implicitly_wait(10)
bet_list = wrap_bets.find_elements_by_tag_name('li')
size_bet_list = len(bet_list)
for child in bet_list:
    print('################################################\n'+child.text+'\n################################################\n')
    
print('Bet list Size = '+ str(size_bet_list))
#xpath last bet: //*[@id="view-main"]/div/div/div/div/div/div/div/div/section/ul/li[27]

#Decomment if new bet and want to create a new csv
with open('/home/thomas/Bureau/unibet.csv', mode='w', encoding='utf8') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"')
    writer.writerow(['Date/heure','Reference','Mise totale','Gains'])
    for i in range(1,size_bet_list):
        #take all xpath for datetime / reference / totalstake
        #take css-selector for totalreturn
        s1 = '//*[@id="view-main"]/div/div/div/div/div/div/div/div/section/ul/li['+str(i)+']/div[1]/div[1]'
        s2 = '//*[@id="view-main"]/div/div/div/div/div/div/div/div/section/ul/li['+str(i)+']/div[1]/div[2]'    
        s3 = '//*[@id="view-main"]/div/div/div/div/div/div/div/div/section/ul/li['+str(i)+']/div[3]/div[1]/div/span[2]/strong'
        s4 = '#view-main > div > div > div > div > div > div > div > div > section > ul > li:nth-child('+str(i)+') > div.cell-footer.clearfix > div.totalreturns'
        datetime = driver.find_element_by_xpath(s1).text
        reference = driver.find_element_by_xpath(s2).text
        totalstake = driver.find_element_by_xpath(s3).text
        totalstake = totalstake[0:len(totalstake)-2]
        totalreturn = driver.find_element_by_css_selector(s4).text
        if 'Gains' in totalreturn:
            totalreturn = totalreturn[7:len(totalreturn)-2]
            print('Gains!')
        elif 'Cashout' in totalreturn:
            totalreturn = totalreturn[9:len(totalreturn)-2]
            print('Cashout!')
        #print( type(datetime), type(reference), type(totalstake), type(totalreturn) )
        
        writer.writerow([datetime,reference,totalstake,totalreturn])



driver.implicitly_wait(30)
#quit window and kill session
driver.quit()
"""
df = pandas.read_csv('/home/thomas/Bureau/unibet.csv')
print(df)
mean1 = df['Mise totale'].mean()
mean2 = df['Gains'].mean()
sumstake = df['Mise totale'].sum()
sumearned = df['Gains'].sum()
bettaken = df['Reference'].count()
balance =  sumearned - sumstake

print ('Nombre de paris effectues depuis inscription: ' + str(bettaken))
print ('Mise en moyenne: ' + str(mean1))
print ('Moyenne gains: ' + str(mean2))
print ('Total mise: ' + str(sumstake))
print ('Total gains: ' + str(sumearned))
print ('Balance gains-mise: '+str(balance))

