# -*- coding: utf-8 -*-

import datetime
import os
import time

from PQTs.Selenium.Base import BaseAcciones
from PQTs.Utilizar import urlSpotifysinginUS

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PQTs.Paths import pathImg
import pyautogui
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Acciones(BaseAcciones):
    def ingresarSpotify(self):
        try:
            self.maximizar()
            self.ir(urlSpotifysinginUS)
            self.sleep(2)
            return True
        except:
            self.salir()
            return False


    def loginSpotify(self,cuenta,password):
        try:
            xpathInputEmail = (By.ID,"login-username")
            xpathInputPassword = (By.ID,"login-password")        
            xpathBotonLogin= (By.ID,"login-button")
            xpathfailemailorpass= (By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[1]/span') 
            
            visibleInputEmail = self.explicitWaitElementoVisibility(15,xpathInputEmail)
            if visibleInputEmail:
                self.escribir(xpathInputEmail,cuenta)
                
                visibleInputPassword = self.explicitWaitElementoVisibility(15,xpathInputPassword)
                if visibleInputPassword:
                    self.escribir(xpathInputPassword,password)
                    visibleBotonLogin = self.explicitWaitElementoVisibility(15,xpathBotonLogin)
                    if visibleBotonLogin:
                        self.click(xpathBotonLogin)
                        self.explicitWaitElementoInvisibility(11,xpathBotonLogin)
                                                                                             
                    else:
                        print(f"visibleBotonLogin {xpathBotonLogin}")
                        return False
                else:
                    print(f"visibleInputPassword {visibleInputPassword}")
                    return False
            else:
                print(f"visibleInputEmail {visibleInputEmail}")
                return False
        except:
            self.refreshweb()
            time.sleep(4)
            return False
    
    def abrirlistareproduccion(self):
        xpathlistadereproduccion= (By.XPATH,'//*[@id="main"]/div/div[2]/nav/div[1]/div[2]/div/div[4]/div[4]/div/div/ul/div/div[2]/div/li') 
        try:
            self.click(xpathlistadereproduccion)
        except:
            self.refreshweb()
            time.sleep(10)
            self.click(xpathlistadereproduccion)

    def reproducir(self):
        xpathbotonplay= (By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[2]/div[4]/div/div/div/div/div/button') 
        try:                        
            self.click(xpathbotonplay)
        except:
            self.refreshweb()
            time.sleep(10)
            self.click(xpathbotonplay)
        pass

        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"3min.png"))
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"6min.png"))
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"9min.png"))
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"12min.png"))    
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"15min.png"))
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"18min.png"))    
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"21min.png"))    
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"24min.png"))    
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"27min.png"))    

    def enviardatos(self,email):
        remitente = 'mayfeljonas1229@gmail.com'
        destinatarios = ['azuresilkmain@gmail.com']
        asunto = f'Lista de reproduccion : {email}'
        cuerpo = f"{str(datetime.datetime.now().strftime('%H-%M-%S'))}"
        ruta_adjunto = (os.path.join(pathImg,f"{email}.png"))
        nombre_adjunto = f'{email}.png'

        # Creamos el objeto mensaje
        mensaje = MIMEMultipart()
        
        # Establecemos los atributos del mensaje
        mensaje['From'] = remitente
        mensaje['To'] = ", ".join(destinatarios)
        mensaje['Subject'] = asunto
        
        # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
        mensaje.attach(MIMEText(cuerpo, 'plain'))
        
        # Abrimos el archivo que vamos a adjuntar
        archivo_adjunto = open(ruta_adjunto, 'rb')
        
        # Creamos un objeto MIME base
        adjunto_MIME = MIMEBase('application', 'octet-stream')
        # Y le cargamos el archivo adjunto
        adjunto_MIME.set_payload((archivo_adjunto).read())
        # Codificamos el objeto en BASE64
        encoders.encode_base64(adjunto_MIME)
        # Agregamos una cabecera al objeto
        adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
        # Y finalmente lo agregamos al mensaje
        mensaje.attach(adjunto_MIME)
        
        # Creamos la conexi??n con el servidor
        sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        
        # Ciframos la conexi??n
        sesion_smtp.starttls()

        # Iniciamos sesi??n en el servidor
        sesion_smtp.login('mayfeljonas1229@gmail.com','dudwvopyazvtxtun')

        # Convertimos el objeto mensaje a texto
        texto = mensaje.as_string()

        # Enviamos el mensaje
        sesion_smtp.sendmail(remitente, destinatarios, texto)

        # Cerramos la conexi??n
        sesion_smtp.quit()





