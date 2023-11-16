from kivymd.app import MDApp
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import os

from kivymd.uix.dialog import MDDialog
import sqlite3
from kivy.core.window import Window
from kivymd.uix.button import MDFillRoundFlatButton, MDFlatButton

from kivy.core.clipboard import Clipboard

from kivymd.toast import toast

from kivymd.theming import ThemeManager
from kivymd.uix.picker import MDThemePicker

from kivymd.uix.snackbar import Snackbar
from kivy.loader import Loader

kv = '''
#:import Snackbar kivymd.uix.snackbar.Snackbar
ScreenManager:
	HomeScreen:
	Coder:
	AuthorScreen:
	Donation:
	Usage:
	Change:
	Updates:
	Donors:
	YouTube:
	More:
	History:
	Python:

<HomeScreen>:
    name: 'home'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDBoxLayout:
                    orientation: 'vertical'
                    MDBottomAppBar:
                        MDToolbar:
                            title: "MATEX Convertor "
                            left_action_items: [["menu", lambda x: nav.set_state("open")]]
                            icon: 'equal'
                            mode: 'end'
                            type: 'bottom'
                            on_action_button:app.matex(express)
                                                               	
                    MDTextField:
                    	id: express
                    	hint_text: "Enter Expression"
                    	helper_text:"press round button down below to get answer"
                    	helper_text_mode: "on_focus"
                    	font_size: 100
                    	pos_hint: {'center_x':0.5}
                    	size_hint:(0.8,0.4)
                    	width:100
                    
                    MDLabel:
                    	id:answer
                    	text:""
                    
                              
                MDNavigationDrawer:
                    id: nav
                    radius: (0,0,100,0)
                    MDBoxLayout:
                        orientation: "vertical"
                        
                        Image:
                            source:"assets/images/matex.jpg"
                            
                        
                        MDLabel:
                            text: "     Version 3.1.2"
                            size_hint_y: None
                            height: self.texture_size[1]
                        
                        ScrollView:
                        	MDList:
                                TwoLineListItem:
                                    text: "App By Truly"
                                    secondary_text:"Created by Utkarsh Naman"
                                    font_style:"Subtitle2"
                                OneLineIconListItem:
                                	text: "truly.away@gmail.com"
                                	on_press: app.email()
                                    font_style:"Caption"
                                    IconLeftWidget:
                                    	icon: "gmail"
                                    	on_press: app.email()
                                OneLineIconListItem:
                                    text:"Coder Section"
                                	on_press: 
                                	    root.manager.current="home"
                                	    root.manager.current="code"
                                	IconLeftWidget:
                                    	icon: "xml"
                                    	on_press: 
                                    	    root.manager.current="home"
                                    	    root.manager.current="code"	   	
                                OneLineIconListItem:
                                    text:"About"
                                	on_press: 
                                	    root.manager.current="home"
                                	    root.manager.current="about"
                                	IconLeftWidget:
                                    	icon: "information"
                                    	on_press: 
                                    	    root.manager.current="home"
                                    	    root.manager.current="about"
                                
                                OneLineIconListItem:
                                    text:"Info"
                                    on_press: 
                                        root.manager.current="home"
                                        root.manager.current="use"
                                    IconLeftWidget:
                                    	icon: "magnify"
                                    	on_press:
                                    	    root.manager.current="home" 
                                    	    root.manager.current="use"
                                OneLineIconListItem:
                                	text:"Theme"
                                    on_press: 
                                        app.show_theme()
                                	IconLeftWidget:
                                    	icon: "pencil"
                                    	on_press: 
                                    	    app.show_theme()
                                OneLineIconListItem:
                                	text:"History"
                                	on_press: 
                                	    root.manager.current="home"
                                	    root.manager.current="history"
                                	IconLeftWidget:
                                    	icon: "clock"
                                    	on_press: 
                                    	    root.manager.current="home"
                                    	    root.manager.current="history"
                                    	
                                OneLineIconListItem:
                                	text:"Donate"
                                	on_press: 
                                	    root.manager.current="home"
                                	    root.manager.current="donate"
                                	IconLeftWidget:
                                    	icon: "hand-heart"
                                    	on_press: 
                                    	    root.manager.current="home"
                                    	    root.manager.current="donate"
                                    	
                                OneLineIconListItem:
                                	text:"Changelog"
                                	on_press: 
                                	    root.manager.current="home"
                                	    root.manager.current="changes"
                                	IconLeftWidget:
                                    	icon: "file-document-edit"
                                    	on_press: 
                                    	    root.manager.current="home"
                                    	    root.manager.current="changes"
                                    	
                                OneLineIconListItem:
                                	text:"Updates"
                                	on_press: 
                                	    root.manager.current="home"
                                	    root.manager.current="update"
                                	IconLeftWidget:
                                    	icon: "history"
                                    	on_press: 
                                    	    root.manager.current="home"
                                    	    root.manager.current="update"
                                    	
                                OneLineIconListItem:
                                	text:"Earlier Donors"
                                	on_press: 
                                	    root.manager.current="home"
                                	    root.manager.current="donor"
                                	IconLeftWidget:
                                    	icon: "currency-inr"
                                    	on_press: 
                                    	    root.manager.current="home"
                                    	    root.manager.current="donor"
                                    	
                                OneLineIconListItem:
                                	text:"YouTube"
                                	on_press: 
                                	    root.manager.current="home"
                                	    root.manager.current="yt"
                                	IconLeftWidget:
                                    	icon: "youtube"
                                    	on_press: 
                                    	    root.manager.current="home"
                                    	    root.manager.current="yt"
                                 
                                OneLineIconListItem:
                                    text: "GitHub"
                                	on_press: app.github()
                                    IconLeftWidget:
                                    	icon: "github"
                                    	on_press: app.github()
                                OneLineIconListItem:
                                	text:"More Apps"
                                	on_press: 
                                	    root.manager.current="home"
                                	    root.manager.current="apps"
                                	IconLeftWidget:
                                    	icon: "android"
                                    	on_press: 
                                    	    root.manager.current="home"
                                    	    root.manager.current="apps"
                                    	
                                	
                                	
                                	                                                      	
<AuthorScreen>:
	name: 'about'    
    MDLabel:
    	text:"MATEX is an application capable of taking general text expression as input and convert it into both python expression(see coder section) and actual mathematical expression fastly and give out result approximately.                                                                                                                                                                           It has:                                                                                                                                                                                                                                       1) Logarithmic function                                                                                                                                                                                       2) Base and exponent                                                                                                                                                                                          3) Greatest integer function                                                                                                                                                                               4) Modulus function                                                                                                                                                                                             5) trigonometric function                                                                                                                                                                                    6) Remainder                                                                                                                                                                                                         7) Famous Euler's identity                                                                                                                                                                                  8) Square root                                                                                                                                                                                                       9) Symbols like m and e                                                                                                                                                                                     10) Basic arithmetic operations.                                                                                                                                                                                                                                                  This app is written using Python programming language and KivyMD GUI framework and was built by me (Utkarsh Naman). MATEX is a product by TRULY (owned by Utkarsh Naman) which for now is into developing softwares and desktop and mobile applications only)"
        pos_hint: {'center_x': 0.5, 'center_y' : 0.5}
    MDFillRoundFlatButton:
        text:"Close"
        pos_hint: {'center_x': 0.87, 'center_y' : 0.06}
        on_press: root.manager.current='home'
        
    MDFillRoundFlatButton:
        text:"How to use"
        
        pos_hint: {'center_x': 0.13, 'center_y' : 0.06}
        on_press:
        	app.mtuse(root)
        	
	
		
<Donation>:
	name:"donate"
	MDFlatButton:
		text:"utkarshnaman8852774@sbi"
		pos_hint: {'center_x': 0.5, 'center_y' : 0.96}
		on_press:
			app.copyupi()
	Image:
		source: "assets/images/payun.jpg"
		allow_stretch: True
							
	MDFillRoundFlatButton:
		text:"Close"
		halign: 'center'
		
		pos_hint: {'center_x': 0.5, 'center_y' : 0.03}
		on_press:			
			root.manager.current='home'


<Usage>:
	name:"use"
	MDFillRoundFlatButton:
		text:"TIPS"
		
		pos_hint: {'center_x': 0.075, 'center_y' : 0.895}
	Image:
		source: "assets/images/help.jpg"
	MDFillRoundFlatButton:
		text:"Close"
		
		pos_hint: {'center_x': 0.5, 'center_y' : 0.04}
		on_press: root.manager.current='home'




<Change>:
	name: "changes"
	ScrollView:
	    MDBoxLayout:
            md_bg_color: 0,0,0,0
            radius: [40, 40, 40, 40]
            ScrollView:
            	MDList:
            		OneLineListItem:
            			text:"Replaced '?' button with '=' button"
            		TwoLineListItem:
            			text:"Added copy feature"
            			secondary_text: "tap to view them"
            			on_press:app.copy_view()
            		
            		TwoLineListItem:
            			text:"Added UI features"
            			secondary_text: "tap to view them"
            			on_press:app.ui_view()
            			
            		TwoLineListItem:
            			text:"Changes made in App Drawer"
            			secondary_text:"tap to view them"
            			on_press:app.section_changes()
            			         			
            		TwoLineListItem:
            			text:"Added update section"
            			secondary_text:"with link to the latest apk"
            			on_press:
            			    root.manager.current="update"
            				app.mtupt()
            			
            		TwoLineListItem:
            			text:"Rectified math errors"
            			secondary_text:"tap to view them"
            			on_press:
            				app.errorupt()
            			
            			
            		OneLineListItem:
            			text:"Added sounds on pop-ups"
            			
    MDFillRoundFlatButton:
    	text:"Close"
    	
		pos_hint: {'center_x':0.5, 'center_y' : 0.1}
		on_press: root.manager.current='home'

		
						
<Updates>:
	name: "update"	
	ScrollView:
		MDList:
		    OneLineListItem:
		    	text:"Check my version"
		    	on_press:app.myver()
		    ThreeLineIconListItem:
			    text:"New Release"
    	    	secondary_text: "Visit link for the newly released apk."
		    	tertiary_text: "<Tap to copy link>"
		    	on_press:app.copylinkL()
	    		IconLeftWidget:
			    	icon: "history"
			    	on_press:app.copylinkL()
				
	MDFillRoundFlatButton:
		text:"Close"
		
		pos_hint: {'center_x': 0.5, 'center_y' : 0.06}
		on_press: root.manager.current='home'



<Donors>:
	name:"donor"	
	ScrollView:
		MDList:
			OneLineListItem:
			    text:"AKSHUN KUMAR"
		    OneLineListItem:
			    text:"VINIT KUMAR"
			    
	MDLabel:
		text:"Donor list shows donors of previous versions"
		pos_hint: {'center_x': 0.6, 'center_y' : 0.3}		
	MDFillRoundFlatButton:
		text:"Donate"
		
		pos_hint: {'center_x': 0.5, 'center_y' : 0.18}
		on_press: app.mtdonate(root)
		
	MDFillRoundFlatButton:
		text:"Close"
		
		pos_hint: {'center_x': 0.5, 'center_y' : 0.06}
		on_press: root.manager.current='home'	



<YouTube>:
	name:'yt'
	
	ScrollView:
		MDList:
			OneLineIconListItem:
			    text:"YouTube Channel"
			    on_press: app.yt_channel()
			    IconLeftWidget:
			        icon: "youtube"
                    on_press: app.yt_channel()
		    OneLineIconListItem:
			    text:"YouTube Tutorial"
			    on_press: app.yt_tutorial()
			    IconLeftWidget:
			        icon: "youtube"
                    on_press: app.yt_tutorial()
		
	
	MDFillRoundFlatButton:
		text:"Close"
		
		pos_hint: {'center_x': 0.5, 'center_y' : 0.06}
		on_press: root.manager.current='home'
		
		
<More>:
	name:'apps'	
	ScrollView:
		MDList:
			TwoLineIconListItem:
			    text:"More Apps by Truly"
			    secondary_text: "tap to copy link"
			    on_press: app.more_apps()
			    IconLeftWidget:
			        icon: "android"
                    on_press: app.more_apps()
		
	
	MDFillRoundFlatButton:
		text:"Close"
		
		pos_hint: {'center_x': 0.5, 'center_y' : 0.06}
		on_press: root.manager.current='home'

	
									
																									
<History>:	
	name: "history"
	MDTextFieldRound:
		id:s_history
		text:"No Data"
		font_size: 100
        size_hint:(0.8,0.8)
		pos_hint: {'center_x': 0.5, 'center_y' : 0.9}
	MDFillRoundFlatButton:
		text:"Reload"
		
		pos_hint: {'center_x': 0.2, 'center_y' : 0.12}
		on_press: app.show_history(root)
		
	MDFillRoundFlatIconButton:
		icon:"delete"
		text:"Clear History"
		
		pos_hint: {'center_x': 0.8, 'center_y' : 0.12}
		on_press: app.trash_history(root)
			
	MDFillRoundFlatButton:
		text:"Close"
		
		pos_hint: {'center_x': 0.5, 'center_y' : 0.06}
		on_press: root.manager.current='home'

			
						
<Coder>:
	name:"code"
	ScrollView:
	    MDList:
            OneLineIconListItem:
                text:"Convert to Python Expression"
                on_press:                     
                    root.manager.current="ttp"

                IconLeftWidget:
			        icon: "language-python"
                    on_press: 
                        root.manager.current="ttp"
                
		
	
	MDFillRoundFlatButton:
		text:"Close"
		
		pos_hint: {'center_x': 0.5, 'center_y' : 0.06}
		on_press:
		    root.manager.current='home'

		
<Python>:
	name:"ttp"
	MDNavigationLayout:
        ScreenManager:
            Screen:
                MDBoxLayout:
                    orientation: 'vertical'
                    MDBottomAppBar:
                        MDToolbar:
                            title: "MATEX Python Convertor"
                            icon: 'language-python'                                  
                            mode: 'end'
                            type: 'bottom'
                            on_action_button:
                            	root.manager.current="ttp"
                            	app.conpy(express)
                    
	                	
                    MDTextField:
                    	id: express
                    	hint_text: "Enter Expression"
                    	helper_text:"press on python button down below to convert"
                    	helper_text_mode: "on_focus"
                    	font_size: 100
                    	pos_hint: {'center_x':0.5}
                    	size_hint:(0.8,0.4)
                    	width:100
                    
                    MDLabel:
                    	id:answer
                    	text:""
                MDFillRoundFlatButton:
		            text:"Back"
	                pos_hint: {'center_x': 0.3, 'center_y' : 0.2}
	                on_press: root.manager.current='code'
	                	
	            MDFillRoundFlatButton:
		            text:"Home"
	                pos_hint: {'center_x': 0.7, 'center_y' : 0.2}
	                on_press: 	                    
	                    root.manager.current='home'
	                    
                    	
                    		
										
'''

class HomeScreen(Screen):
	pass
class AuthorScreen(Screen):
	pass
class Donation(Screen):
	pass
class Usage(Screen):
	pass
class Change(Screen):
	pass
class Updates(Screen):
	pass
class Donors(Screen):
	pass
class YouTube(Screen):
	pass
class More(Screen):
	pass
class History(Screen):
	pass
class Coder(Screen):
	pass
class Python(Screen):
	pass


sm= ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(AuthorScreen(name='about'))
sm.add_widget(Donation(name='donate'))
sm.add_widget(Usage(name='use'))
sm.add_widget(Change(name='changes'))
sm.add_widget(Updates(name='update'))
sm.add_widget(Donors(name='donor'))
sm.add_widget(YouTube(name='yt'))
sm.add_widget(More(name='apps'))
sm.add_widget(History(name='history'))
sm.add_widget(Coder(name='code'))
sm.add_widget(Python(name='ttp'))

class Demo(ScreenManager):
    pass

class TTE(MDApp):
    
    def build(self):
        Window.bind(on_keyboard=self.key_input)
        self.theme_cls=ThemeManager()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        conn = sqlite3.connect('repos/database/history_database.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists history(expression text)""")
        conn.commit()
        conn.close()
        return Builder.load_string(kv)
	 
    def dialgclose(self,root):
    	 sound2= SoundLoader.load("assets/audio/pop6.wav")
    	 if sound2:
        	sound2.loop= False
        	sound2.play()
    	 self.dialg.dismiss()
    	 
    def closeapppop(self):	    
#1        
        if self.theme_cls.primary_palette=="Blue":
            
            end_button = MDFillRoundFlatButton(text='[color=#5A7B95]YES', md_bg_color=(226/255.0, 236/255.0, 245/255.0, 1), on_release=self.closeapp)
        
            no_button = MDFillRoundFlatButton(text="[color=#ffffff]NO",md_bg_color=(11/255.0, 150/255.0, 1, 1), on_release=self.dialgclose)
        
#2
        elif self.theme_cls.primary_palette=="Orange":
        	end_button = MDFillRoundFlatButton(text='[color=#C1632A]YES', md_bg_color=(252/255.0, 235/255.0, 224/255.0, 1), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#ffffff]NO",md_bg_color=(233/255.0, 120/255.0, 52/255.0, 1), on_release=self.dialgclose)

#3                
        elif self.theme_cls.primary_palette=="Red":
        	end_button = MDFillRoundFlatButton(text='[color=#CB0320]YES', md_bg_color=(255/255.0, 236/255.0, 241/255.0, 1), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#ffffff]NO",md_bg_color=(244/255.0, 66/255.0, 54/255.0, 1), on_release=self.dialgclose)

#4	
        
        elif self.theme_cls.primary_palette=="Pink":
        	end_button = MDFillRoundFlatButton(text='[color=#D51B5A]YES', md_bg_color=(253/255.0, 221/255.0, 244/255.0, 0.8), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#ffffff]NO",md_bg_color=(234/255.0, 30/255.0, 99/255.0, 1), on_release=self.dialgclose)
        	
#5	
        
        elif self.theme_cls.primary_palette=="Purple":
        	end_button = MDFillRoundFlatButton(text='[color=#7D208E]YES', md_bg_color=(230/255.0, 211/255.0, 255/255.0, 1), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#ffffff]NO",md_bg_color=(156/255.0, 40/255.0, 177/255.0, 1), on_release=self.dialgclose)


#6        
        elif self.theme_cls.primary_palette=="DeepPurple":
        	end_button = MDFillRoundFlatButton(text='[color=#543095]YES', md_bg_color=(187/255.0, 169/255.0, 254/255.0, 0.5), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#ffffff]NO",md_bg_color=(103/255.0, 59/255.0, 183/255.0, 1), on_release=self.dialgclose)        	
        
        
#7	
        
        elif self.theme_cls.primary_palette=="Indigo":
        	end_button = MDFillRoundFlatButton(text='[color=#2E3C85]YES', md_bg_color=(191/255.0, 199/255.0, 255/255.0, 0.7), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#ffffff]NO",md_bg_color=(63/255.0, 81/255.0, 181/255.0, 1), on_release=self.dialgclose)
        	
#8	
        
        elif self.theme_cls.primary_palette=="LightBlue":
        	end_button = MDFillRoundFlatButton(text='[color=#027AB2]YES', md_bg_color=(192/255.0, 223/255.0, 254/255.0, 1), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#ffffff]NO",md_bg_color=(3/255.0, 169/255.0, 245/255.0, 1), on_release=self.dialgclose)        	          
        	              
        	                
#9	
        
        elif self.theme_cls.primary_palette=="Cyan":
        	end_button = MDFillRoundFlatButton(text='[color=#00798A]YES', md_bg_color=(207/255.0, 240/255.0, 254/255.0, 1), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#ffffff]NO",md_bg_color=(0/255.0, 188/255.0, 213/255.0, 1), on_release=self.dialgclose)     
        	
        	 	                    
#10	
        
        elif self.theme_cls.primary_palette=="Teal":
        	end_button = MDFillRoundFlatButton(text='[color=#00786C]YES', md_bg_color=(213/255.0, 253/255.0, 255/255.0, 1), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#ffffff]NO",md_bg_color=(0/255.0, 151/255.0, 136/255.0, 1), on_release=self.dialgclose)        	 	                     	                     	              
        	
#11	
        
        elif self.theme_cls.primary_palette=="Green":
        	end_button = MDFillRoundFlatButton(text='[color=#39843C]YES', md_bg_color=(209/255.0, 254/255.0, 210/255.0, 1), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#ffffff]NO",md_bg_color=(76/255.0, 176/255.0, 80/255.0, 1), on_release=self.dialgclose)   
        	
        	     	            
#12	
        
        elif self.theme_cls.primary_palette=="LightGreen":
        	end_button = MDFillRoundFlatButton(text='[color=#618734]YES', md_bg_color=(238/255.0, 255/255.0, 227/255.0, 1), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#ffffff]NO",md_bg_color=(139/255.0, 194/255.0, 74/255.0, 1), on_release=self.dialgclose)        	     	                 	                 	            
        	
#13
        
        elif self.theme_cls.primary_palette=="Lime":
        	end_button = MDFillRoundFlatButton(text='[color=#879125]YES', md_bg_color=(243/255.0, 255/255.0, 207/255.0, 1), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#000000]NO",md_bg_color=(205/255.0, 220/255.0, 57/255.0, 1), on_release=self.dialgclose)
        	
        	        	
#14	
        
        elif self.theme_cls.primary_palette=="Yellow":
        	end_button = MDFillRoundFlatButton(text='[color=#B4A62A]YES', md_bg_color=(255/255.0, 245/255.0, 193/255.0, 1), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#000000]NO",md_bg_color=(255/255.0, 235/255.0, 60/255.0, 1), on_release=self.dialgclose)        	        	              	

        	
#15	
        
        elif self.theme_cls.primary_palette=="Amber":
        	end_button = MDFillRoundFlatButton(text='[color=#B28705]YES', md_bg_color=(254/255.0, 236/255.0, 186/255.0, 1), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#ffffff]NO",md_bg_color=(254/255.0, 193/255.0, 7/255.0, 1), on_release=self.dialgclose)        	        	
        	        	        	        	

#16	
        
        elif self.theme_cls.primary_palette=="DeepOrange":
        	end_button = MDFillRoundFlatButton(text='[color=#AA3A17]YES', md_bg_color=(254/255.0, 190/255.0, 189/255.0, 1), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#ffffff]NO",md_bg_color=(254/255.0, 87/255.0, 34/255.0, 1), on_release=self.dialgclose)     
        	
        	   	                               	                     #17	
        
        elif self.theme_cls.primary_palette=="Brown":
        	end_button = MDFillRoundFlatButton(text='[color=#67483C]YES', md_bg_color=(255/255.0, 220/255.0, 213/255.0, 1), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#ffffff]NO",md_bg_color=(121/255.0, 85/255.0, 71/255.0, 1), on_release=self.dialgclose)
 
        	                                    	                       #18	
        
        elif self.theme_cls.primary_palette=="Gray":
        	end_button = MDFillRoundFlatButton(text='[color=#747474]YES', md_bg_color=(236/255.0, 236/255.0, 236/255.0, 1), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#000000]NO",md_bg_color=(158/255.0, 158/255.0, 158/255.0, 1), on_release=self.dialgclose)             	                            
        	                                    	                       #19	
        
        elif self.theme_cls.primary_palette=="BlueGray":
        	end_button = MDFillRoundFlatButton(text='[color=#445862]YES', md_bg_color=(214/255.0, 240/255.0, 255/255.0, 1), on_release=self.closeapp)
        	no_button = MDFillRoundFlatButton(text="[color=#ffffff]No",md_bg_color=(96/255.0, 125/255.0, 139/255.0, 1), on_release=self.dialgclose)
        
        sound1= SoundLoader.load("assets/audio/pop.wav")
        if sound1:
        	sound1.loop= False
        	sound1.play()
        
        self.dialg=MDDialog(title="Close App?", md_bg_color= (226/255.0, 236/255.0, 245/255.0, 0.1), radius=(50,50,50,50), text="Do you want to exit?", size_hint=(0.8, 0.5), buttons=[end_button, no_button])
        
        self.dialg.open()
	    
    def closeapp(self,root):
        sound2= SoundLoader.load("assets/audio/pop6.wav")
        if sound2:
            sound2.loop= False
            
            sound2.play()
        
        Window.close()
	            
    def  key_input(self, window, key, scancode, codepoint, modifier):
    	if key==27:
    		self.closeapppop()
    		return True
    	else:
    		return False
    		
    def  donatepopup(self):
    	sound1= SoundLoader.load("assets/audio/pop.wav")
    	if sound1:
        	sound1.loop= False
        	sound1.play()
    	close_button = MDFillRoundFlatButton(text='Okay', md_bg_color=(1,0.3,0.2,1), on_release=self.close_dialog1)    	
    	self.dialog1 = MDDialog(title="Internet Access Required", text="In order to avoid misuse of the app and forcefully changing of the upi qr code to something else, I made the qr code to be loaded from internet so that jpg files cannot be changed. If qr code is not loaded, please turn on your Mobile/WiFi data and open app again.                                                                                                                                                            You can also copy my UPI id by tapping on it.                                                                                                                                                                                                                                                                                             The UPI id should be 'utkarshnaman8852774@sbi'                                                                                                                                                     Sorry for the inconvenience caused.", size_hint=[0.8, 0.3], buttons=[close_button])
    	self.dialog1.open()
    	
    	
    def trash_history(self, root):
    	if os.path.exists("repos/database/history_database.db"):
    		os.remove("repos/database/history_database.db")
    	snack=Snackbar(text="History Cleared")
    	snack.buttons = [MDFlatButton(text="[color=#ddbb34]Okay", on_press=snack.dismiss)]
    	snack.open()
    	self.show_history(root)
    		    		
    def mtuse(self,root):
    	root.manager.current='use'
    	snack=Snackbar(text="Moved to info section")
    	snack.buttons = [MDFlatButton(text="[color=#ddbb34]Okay", on_press=snack.dismiss)]
    	snack.open()
    	
    def mtupt(self):
    	snack=Snackbar(text="Rectified logic and text read errors")
    	snack.buttons = [MDFlatButton(text="[color=#ddbb34]Okay", on_press=snack.dismiss)]
    	snack.open()
    		
    def errorupt(self):
    	snack=Snackbar(text="Rectified logic and text read errors")
    	snack.buttons = [MDFlatButton(text="[color=#ddbb34]Okay", on_press=snack.dismiss)]
    	snack.open()
    		
    def copyupi(self):
    	Clipboard.copy("utkarshnaman8852774@sbi")
    	snack=Snackbar(text="UPI ID copied! ")
    	snack.buttons = [MDFlatButton(text="[color=#ddbb34]Okay", on_press=snack.dismiss)]
    	snack.open()
    	    	    		
    def mtdonate(self,root):
    	root.manager.current='donate'
    	snack=Snackbar(text="Moved to Donation section")
    	snack.buttons = [MDFlatButton(text="[color=#ddbb34]Okay", on_press=snack.dismiss)]
    	snack.open()
    		       		       	
    def copy_view(self):
    	sound1= SoundLoader.load("assets/audio/pop.wav")
    	if sound1:
        	sound1.loop= False
        	sound1.play()
    	close_button = MDFillRoundFlatButton(text='Close', md_bg_color=(1,0.3,0.2,1), on_release=self.close_dialog1)
    	
    	self.dialog1 = MDDialog(title="Copy Features", text="•Added copy result feature                                                                                            •Added copy email feature                                                                                            •Added copy link of latest apk                                                                                       •Added copy link of YouTube channel feature                                                                                                                                       •Added copy links in YouTube section feature                                                                                                                                                                   ", size_hint=[0.8, 0.3], buttons=[close_button])
    	self.dialog1.open()
    	
    def ui_view(self):
    	sound1= SoundLoader.load("assets/audio/pop.wav")
    	
    	if sound1:
        	sound1.loop= False
        	sound1.play()
    	close_button = MDFillRoundFlatButton(text='Close', md_bg_color=(1,0.3,0.2,1), on_release=self.close_dialog1)
    	
    	self.dialog1 = MDDialog(title="UI CHANGELOG", text="•Press back button to exit                                                                                                                                                                                           •Added confirmation box on exit                                                                                                                                                                                         •Added colored buttons                                                                                                                                                                                      •Customized buttons in sync with Theme                                                                                                                                                                                                                   •Changed Result Box colour                                                                                                             •Added earlier donor section                                                                                                                                                        ", size_hint=[0.8, 0.3], buttons=[close_button])    	
    	self.dialog1.open()
    		
    def section_changes(self):
    	sound1= SoundLoader.load("assets/audio/pop.wav")
    	
    	if sound1:
        	sound1.loop= False
        	sound1.play()
    	close_button = MDFillRoundFlatButton(text='Close', md_bg_color=(1,0.3,0.2,1), on_release=self.close_dialog1)
    	
    	self.dialog1 = MDDialog(title="DRAWER CHANGELOG", text="•Added copy email feature                                                                                                                                                                                                •Added Coder Section                                                                                                                                                                                         •Added History Section                                                                                                                                                                                       •Added Changelog Section                                                                                                                                                                                                                   •Added update section                                                                                                             •Added earlier donor section                                                                                                   •Added social sites                                                                                                                   •Added tutorial links in YouTube section                                                                                                                                           •Added more apps section                            ", size_hint=[0.8, 0.3], buttons=[close_button])    	
    	self.dialog1.open()
    	
    def close_dialog1(self,obj):
    	sound2= SoundLoader.load("assets/audio/pop6.wav")
    	
    	if sound2:
        	sound2.loop= False
        	sound2.play()        	
    	self.dialog1.dismiss()
    
    	
    		
    def myver(self):
    	toast("version 3.1.2")
    
    def github(self):
    	Clipboard.copy("https://github.com/utkarsh-naman")
    	toast("Link copied")
    	
    def more_apps(self):
    	Clipboard.copy("https://drive.google.com/drive/folders/13cYcX7xFQ0mK62HaWar1yvWninEGRO7e")
    	toast("Link copied")
    	
    def yt_channel(self):
    	Clipboard.copy("https://m.youtube.com/channel/UCTuRkJwD91Yj_8zbtL3uwPQ")
    	toast("Link copied")
    	
    def yt_tutorial(self):
    	Clipboard.copy("https://youtube.com/playlist?list=PLZchMekN22Un3scfWu74NctnwKjmTN5M4")
    	toast("Tutorial link copied")
    		
    def copylinkL(self):
    	link_latest="https://drive.google.com/drive/folders/13NEsclz1rMhXaleFpfHcjPhmgV5ac7Gf"
    	Clipboard.copy(link_latest)
    	toast("Link copied")
    
    def email(self):
    	Clipboard.copy("truly.away@gmail.com")
    	toast("email address copied")
    	
    def show_theme(self):
    	picker=MDThemePicker()
    	picker.open()
    	
    def copy_data(self,obj):
    	sound3= SoundLoader.load("assets/audio/pop.wav")
    	if sound3:
        	sound3.loop= False
        	sound3.play()
    	Clipboard.copy(self.dialog.text)
    	toast("Result copied")
    	
    def aboutpy(self, exp):
        #1
        if self.theme_cls.primary_palette=="Blue":
            close_button = MDFillRoundFlatButton(text='[color=#5A7B95]X', md_bg_color=(226/255.0, 236/255.0, 245/255.0, 1), on_release=self.close_dialog)
        
            copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(11/255.0, 150/255.0, 1, 1), on_release=self.copy_data)
        
#2        
        elif self.theme_cls.primary_palette=="Orange":
        	close_button = MDFillRoundFlatButton(text='[color=#C1632A]X', md_bg_color=(252/255.0, 235/255.0, 224/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(233/255.0, 120/255.0, 52/255.0, 1), on_release=self.copy_data)

#3                
        elif self.theme_cls.primary_palette=="Red":
        	close_button = MDFillRoundFlatButton(text='[color=#CB0320]X', md_bg_color=(255/255.0, 236/255.0, 241/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(244/255.0, 66/255.0, 54/255.0, 1), on_release=self.copy_data)

#4	
        
        elif self.theme_cls.primary_palette=="Pink":
        	close_button = MDFillRoundFlatButton(text='[color=#D51B5A]X', md_bg_color=(253/255.0, 221/255.0, 244/255.0, 0.8), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(234/255.0, 30/255.0, 99/255.0, 1), on_release=self.copy_data)
        	
#5	
        
        elif self.theme_cls.primary_palette=="Purple":
        	close_button = MDFillRoundFlatButton(text='[color=#7D208E]X', md_bg_color=(230/255.0, 211/255.0, 255/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(156/255.0, 40/255.0, 177/255.0, 1), on_release=self.copy_data)


#6        
        elif self.theme_cls.primary_palette=="DeepPurple":
        	close_button = MDFillRoundFlatButton(text='[color=#543095]X', md_bg_color=(187/255.0, 169/255.0, 254/255.0, 0.5), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(103/255.0, 59/255.0, 183/255.0, 1), on_release=self.copy_data)        	
        
        
#7	
        
        elif self.theme_cls.primary_palette=="Indigo":
        	close_button = MDFillRoundFlatButton(text='[color=#2E3C85]X', md_bg_color=(191/255.0, 199/255.0, 255/255.0, 0.7), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(63/255.0, 81/255.0, 181/255.0, 1), on_release=self.copy_data)
        	
#8	
        
        elif self.theme_cls.primary_palette=="LightBlue":
        	close_button = MDFillRoundFlatButton(text='[color=#027AB2]X', md_bg_color=(192/255.0, 223/255.0, 254/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(3/255.0, 169/255.0, 245/255.0, 1), on_release=self.copy_data)        	          
        	              
        	                
#9	
        
        elif self.theme_cls.primary_palette=="Cyan":
        	close_button = MDFillRoundFlatButton(text='[color=#00798A]X', md_bg_color=(207/255.0, 240/255.0, 254/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(0/255.0, 188/255.0, 213/255.0, 1), on_release=self.copy_data)     
        	
        	 	                    
#10	
        
        elif self.theme_cls.primary_palette=="Teal":
        	close_button = MDFillRoundFlatButton(text='[color=#00786C]X', md_bg_color=(213/255.0, 253/255.0, 255/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(0/255.0, 151/255.0, 136/255.0, 1), on_release=self.copy_data)        	 	                     	                     	              
        	
#11	
        
        elif self.theme_cls.primary_palette=="Green":
        	close_button = MDFillRoundFlatButton(text='[color=#39843C]X', md_bg_color=(209/255.0, 254/255.0, 210/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(76/255.0, 176/255.0, 80/255.0, 1), on_release=self.copy_data)   
        	
        	     	            
#12	
        
        elif self.theme_cls.primary_palette=="LightGreen":
        	close_button = MDFillRoundFlatButton(text='[color=#618734]X', md_bg_color=(238/255.0, 255/255.0, 227/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(139/255.0, 194/255.0, 74/255.0, 1), on_release=self.copy_data)        	     	                 	                 	            
        	
#13
        
        elif self.theme_cls.primary_palette=="Lime":
        	close_button = MDFillRoundFlatButton(text='[color=#879125]X', md_bg_color=(243/255.0, 255/255.0, 207/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#000000]copy",md_bg_color=(205/255.0, 220/255.0, 57/255.0, 1), on_release=self.copy_data)
        	
        	        	
#14	
        
        elif self.theme_cls.primary_palette=="Yellow":
        	close_button = MDFillRoundFlatButton(text='[color=#B4A62A]X', md_bg_color=(255/255.0, 245/255.0, 193/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#000000]copy",md_bg_color=(255/255.0, 235/255.0, 60/255.0, 1), on_release=self.copy_data)        	        	              	

        	
#15	
        
        elif self.theme_cls.primary_palette=="Amber":
        	close_button = MDFillRoundFlatButton(text='[color=#B28705]X', md_bg_color=(254/255.0, 236/255.0, 186/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(254/255.0, 193/255.0, 7/255.0, 1), on_release=self.copy_data)        	        	
        	        	        	        	

#16	
        
        elif self.theme_cls.primary_palette=="DeepOrange":
        	close_button = MDFillRoundFlatButton(text='[color=#AA3A17]X', md_bg_color=(254/255.0, 190/255.0, 189/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(254/255.0, 87/255.0, 34/255.0, 1), on_release=self.copy_data)     
        	
        	   	                               	                     #17	
        
        elif self.theme_cls.primary_palette=="Brown":
        	close_button = MDFillRoundFlatButton(text='[color=#67483C]X', md_bg_color=(255/255.0, 220/255.0, 213/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(121/255.0, 85/255.0, 71/255.0, 1), on_release=self.copy_data)
 
        	                                    	                       #18	
        
        elif self.theme_cls.primary_palette=="Gray":
        	close_button = MDFillRoundFlatButton(text='[color=#747474]X', md_bg_color=(236/255.0, 236/255.0, 236/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#000000]copy",md_bg_color=(158/255.0, 158/255.0, 158/255.0, 1), on_release=self.copy_data)             	                            
        	                                    	                       #19	
        
        elif self.theme_cls.primary_palette=="BlueGray":
        	close_button = MDFillRoundFlatButton(text='[color=#445862]X', md_bg_color=(214/255.0, 240/255.0, 255/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(96/255.0, 125/255.0, 139/255.0, 1), on_release=self.copy_data)
        
        sound1= SoundLoader.load("assets/audio/pop.wav")
        if sound1:
        	sound1.loop= False
        	sound1.play()
        self.dialog=MDDialog(title="Python Expression", md_bg_color= (226/255.0, 236/255.0, 245/255.0, 0.1), radius=(50,50,50,50), text="", size_hint=(0.8, 0.5), buttons=[close_button, copy_button])
        
        self.dialog.open()
        if exp == "":        	
        	self.dialog.text="Not an expression. Enter one."
        else:
            self.dialog.text=f"{exp}"
            
       	
        	
    def close_dialog(self,obj):
        sound= SoundLoader.load("assets/audio/pop6.wav")
        if sound:
        	sound.loop= False
        	sound.play()
        self.dialog.dismiss()
        
    def about(self, exp):
        import math

#1
        if self.theme_cls.primary_palette=="Blue":
            close_button = MDFillRoundFlatButton(text='[color=#5A7B95]X', md_bg_color=(226/255.0, 236/255.0, 245/255.0, 1), on_release=self.close_dialog)
        
            copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(11/255.0, 150/255.0, 1, 1), on_release=self.copy_data)
        
#2        
        elif self.theme_cls.primary_palette=="Orange":
        	close_button = MDFillRoundFlatButton(text='[color=#C1632A]X', md_bg_color=(252/255.0, 235/255.0, 224/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(233/255.0, 120/255.0, 52/255.0, 1), on_release=self.copy_data)

#3                
        elif self.theme_cls.primary_palette=="Red":
        	close_button = MDFillRoundFlatButton(text='[color=#CB0320]X', md_bg_color=(255/255.0, 236/255.0, 241/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(244/255.0, 66/255.0, 54/255.0, 1), on_release=self.copy_data)

#4	
        
        elif self.theme_cls.primary_palette=="Pink":
        	close_button = MDFillRoundFlatButton(text='[color=#D51B5A]X', md_bg_color=(253/255.0, 221/255.0, 244/255.0, 0.8), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(234/255.0, 30/255.0, 99/255.0, 1), on_release=self.copy_data)
        	
#5	
        
        elif self.theme_cls.primary_palette=="Purple":
        	close_button = MDFillRoundFlatButton(text='[color=#7D208E]X', md_bg_color=(230/255.0, 211/255.0, 255/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(156/255.0, 40/255.0, 177/255.0, 1), on_release=self.copy_data)


#6        
        elif self.theme_cls.primary_palette=="DeepPurple":
        	close_button = MDFillRoundFlatButton(text='[color=#543095]X', md_bg_color=(187/255.0, 169/255.0, 254/255.0, 0.5), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(103/255.0, 59/255.0, 183/255.0, 1), on_release=self.copy_data)        	
        
        
#7	
        
        elif self.theme_cls.primary_palette=="Indigo":
        	close_button = MDFillRoundFlatButton(text='[color=#2E3C85]X', md_bg_color=(191/255.0, 199/255.0, 255/255.0, 0.7), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(63/255.0, 81/255.0, 181/255.0, 1), on_release=self.copy_data)
        	
#8	
        
        elif self.theme_cls.primary_palette=="LightBlue":
        	close_button = MDFillRoundFlatButton(text='[color=#027AB2]X', md_bg_color=(192/255.0, 223/255.0, 254/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(3/255.0, 169/255.0, 245/255.0, 1), on_release=self.copy_data)        	          
        	              
        	                
#9	
        
        elif self.theme_cls.primary_palette=="Cyan":
        	close_button = MDFillRoundFlatButton(text='[color=#00798A]X', md_bg_color=(207/255.0, 240/255.0, 254/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(0/255.0, 188/255.0, 213/255.0, 1), on_release=self.copy_data)     
        	
        	 	                    
#10	
        
        elif self.theme_cls.primary_palette=="Teal":
        	close_button = MDFillRoundFlatButton(text='[color=#00786C]X', md_bg_color=(213/255.0, 253/255.0, 255/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(0/255.0, 151/255.0, 136/255.0, 1), on_release=self.copy_data)        	 	                     	                     	              
        	
#11	
        
        elif self.theme_cls.primary_palette=="Green":
        	close_button = MDFillRoundFlatButton(text='[color=#39843C]X', md_bg_color=(209/255.0, 254/255.0, 210/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(76/255.0, 176/255.0, 80/255.0, 1), on_release=self.copy_data)   
        	
        	     	            
#12	
        
        elif self.theme_cls.primary_palette=="LightGreen":
        	close_button = MDFillRoundFlatButton(text='[color=#618734]X', md_bg_color=(238/255.0, 255/255.0, 227/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(139/255.0, 194/255.0, 74/255.0, 1), on_release=self.copy_data)        	     	                 	                 	            
        	
#13
        
        elif self.theme_cls.primary_palette=="Lime":
        	close_button = MDFillRoundFlatButton(text='[color=#879125]X', md_bg_color=(243/255.0, 255/255.0, 207/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#000000]copy",md_bg_color=(205/255.0, 220/255.0, 57/255.0, 1), on_release=self.copy_data)
        	
        	        	
#14	
        
        elif self.theme_cls.primary_palette=="Yellow":
        	close_button = MDFillRoundFlatButton(text='[color=#B4A62A]X', md_bg_color=(255/255.0, 245/255.0, 193/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#000000]copy",md_bg_color=(255/255.0, 235/255.0, 60/255.0, 1), on_release=self.copy_data)        	        	              	

        	
#15	
        
        elif self.theme_cls.primary_palette=="Amber":
        	close_button = MDFillRoundFlatButton(text='[color=#B28705]X', md_bg_color=(254/255.0, 236/255.0, 186/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(254/255.0, 193/255.0, 7/255.0, 1), on_release=self.copy_data)        	        	
        	        	        	        	

#16	
        
        elif self.theme_cls.primary_palette=="DeepOrange":
        	close_button = MDFillRoundFlatButton(text='[color=#AA3A17]X', md_bg_color=(254/255.0, 190/255.0, 189/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(254/255.0, 87/255.0, 34/255.0, 1), on_release=self.copy_data)     
        	
        	   	                               	                     #17	
        
        elif self.theme_cls.primary_palette=="Brown":
        	close_button = MDFillRoundFlatButton(text='[color=#67483C]X', md_bg_color=(255/255.0, 220/255.0, 213/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(121/255.0, 85/255.0, 71/255.0, 1), on_release=self.copy_data)
 
        	                                    	                       #18	
        
        elif self.theme_cls.primary_palette=="Gray":
        	close_button = MDFillRoundFlatButton(text='[color=#747474]X', md_bg_color=(236/255.0, 236/255.0, 236/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#000000]copy",md_bg_color=(158/255.0, 158/255.0, 158/255.0, 1), on_release=self.copy_data)             	                            
        	                                    	                       #19	
        
        elif self.theme_cls.primary_palette=="BlueGray":
        	close_button = MDFillRoundFlatButton(text='[color=#445862]X', md_bg_color=(214/255.0, 240/255.0, 255/255.0, 1), on_release=self.close_dialog)
        	copy_button = MDFillRoundFlatButton(text="[color=#ffffff]copy",md_bg_color=(96/255.0, 125/255.0, 139/255.0, 1), on_release=self.copy_data)             	                                   	                                    	                                    	                                   	                                    	                                    	                            
        sound1= SoundLoader.load("assets/audio/pop.wav")
        if sound1:
        	sound1.loop= False
        	sound1.play()
        self.dialog=MDDialog(title="Approximate Result", md_bg_color= (226/255.0, 236/255.0, 245/255.0, 0.1), radius=(50,50,50,50), text="", size_hint=(0.8, 0.5), buttons=[close_button, copy_button])
        
        self.dialog.open()
        if exp == "":        	
        	self.dialog.text="Not an expression. Enter one."
        elif exp=="()":
        	self.dialog.text="0"
        else:
            try:
        	    self.dialog.text=f"{eval(exp)}"
            except NameError:
            	self.dialog.text="Check your expression again"        	
            except ValueError:
        	    self.dialog.text="Entered expression has no solution."
            except SyntaxError:
        	    self.dialog.text="Invalid Expression!"
            except TypeError:
                self.dialog.text="Can't use that operators here"
            except MemoryError:
            	self.dialog.text="App memory reached it's limit"
            except OverflowError:
            	self.dialog.text="Result is too large to display"
            except ZeroDivisionError:
            	self.dialog.text="Not defined"
            except RuntimeError:
            	self.dialog.text="Operation took too long"
            except SystemError:
            	self.dialog.text="Got some issues"
            except KeyError:
            	self.dialog.text="Failed to execute"
            except AttributeError:
        	    self.dialog.text="use brackets or proper functions"
            except FloatingPointError:
                self.dialog.text="Decimal error"
            except ArithmeticError:
                self.dialog.text="Use correct format"
            except IndexError:
            	self.dialog.text="Improper syntax"
       	
        
    def conpy(self, expd):
        if os.path.exists("repos/database/history_database.db"):
            conn = sqlite3.connect('repos/database/history_database.db')
            c = conn.cursor()
            c.execute("INSERT INTO history VALUES (:first)",{'first': expd.text})
            conn.commit()
            conn.close()
            
        else:
        	conn = sqlite3.connect('repos/database/history_database.db')      
	        c = conn.cursor()
	        c.execute("""CREATE TABLE if not exists history(expression text)""")
	        c.execute("INSERT INTO history VALUES (:first)",{'first': expd.text})
	        conn.commit()
	        conn.close()
        	
        	
        import math
        exp = str(expd.text)
        exp = exp.lower()
        exp = exp.replace(" ", "")
        exp = exp.replace("÷", "/")
        exp = exp.replace("×", "*")
        exp = exp.replace("math.pi", "π")
        exp = exp.replace("math.e", "e")
        exp = exp.replace("pi", "π")
        exp = exp.replace("{", "(")
        exp = exp.replace("}", ")")
        exp = exp.replace("sqrt", "√")
        exp = exp.replace("math.sqrt", "√")
        
        exp = exp.replace("log", "math.log")
        exp = exp.replace("ln", "math.log")
        exp = exp.replace("math.math.log", "math.log")
        exp = exp.replace("antimath.log(", "math.pow(")
        exp = exp.replace("plus", "+")
        exp = exp.replace("minus", "-")
        exp = exp.replace("into", "*")
        exp = exp.replace("times", "*")
        exp = exp.replace("multiply", "*")
        exp = exp.replace("multipliedby", "*")
        exp = exp.replace("divide", "/")
        exp = exp.replace("dividedby", "/")
        exp = exp.replace("%", "%")
        exp = exp.replace("⁽", "^(")
        exp = exp.replace("⁺", "+")
        exp = exp.replace("⁻", "-")
        exp = exp.replace("⁾", ")")
        exp = exp.replace("⁽¹⁾", "^(1)")
        exp = exp.replace("⁽½⁾", "^(1)")
        exp = exp.replace("⁽⅓⁾","^(1/3)")
        exp = exp.replace("⁽¼⁾","^(1/4)")
        exp = exp.replace("⁽⅛⁾","^(1/8)")   
        exp = exp.replace("⁽²⁾","^2")
        exp = exp.replace("⁽⅔⁾","^(2/3)")
        exp = exp.replace("⁽³⁾","^(3)")
        exp = exp.replace("⁽¾⁾","^(3/4)")
        exp = exp.replace("⁽⅜⁾","^(3/8)")
        exp = exp.replace("⁽⁴⁾","^4")
        exp = exp.replace("⁽⅝⁾","^(5/8)")
        exp = exp.replace("⁽⅞⁾","^(7/8)")
       
        exp = exp.replace("¹","^1")       
        exp = exp.replace("½","^(1/2)")
        exp = exp.replace("⅓","^(1/3)")
        exp = exp.replace("¼","^(1/4)")
        exp = exp.replace("⅛","^(1/8)")   
        exp = exp.replace("²","^2")
        exp = exp.replace("⅔","^(2/3)")
        exp = exp.replace("³","^(3)")
        exp = exp.replace("¾","^(3/4)")
        exp = exp.replace("⅜","^(3/8)")
        exp = exp.replace("⁴","^4")
        exp = exp.replace("⅝","^(5/8)")
        exp = exp.replace("⅞","^(7/8)")
                
        exp = exp.replace("raisedtothepowerof", "^")
        exp = exp.replace("raisedtothepower", "^")
        exp = exp.replace("tothepowerof", "^")
        exp = exp.replace("tothepower", "^")
        exp = exp.replace("squarerootof", "√")
        exp = exp.replace("squareroot", "√")
        
        exp = exp.replace("squared", "^2")
        exp = exp.replace("square", "^2")
        exp = exp.replace("e^(iπ)", "(-1)")
        exp = exp.replace("e^(i*π)", "(-1)")
        
        openmod = 0
        closemod = 0        
        ptpk = 0
        while ptpk < len(exp):
            if exp[ptpk] == '|':
                openmod += 1
            ptpk+=1    
            if  ptpk<len(exp):
                 if exp[ptpk] =='|':
                     closemod += 1
            ptpk=ptpk+1
        if openmod-closemod!=0:
        	exp=exp+"|"

        # completing left brackets
        openbrac = 0
        closebrac = 0
        ptp = 0
        while ptp < len(exp):
            if exp[ptp] == '(':
                openbrac += 1
            if exp[ptp] == ')':
                closebrac += 1
            ptp += 1
        if openbrac-closebrac!=0:
           if openbrac>closebrac:
           	diff=openbrac-closebrac
           	while diff >0:
           		exp=exp+")"
           		diff-=1
           elif openbrac<closebrac:
           	diff=closebrac-openbrac
           	while diff >0:
           		exp="("+exp
           		diff-=1
        #wrong input in log   	
        starr=0
        while starr<len(exp):
             if exp[starr] == 'g' and starr+1<len(exp) and exp[starr+1] in ('+','-', '/', '*'):
             	exp="ln(-1)"
             starr+=1
       #wrong input in √  	
        starr2=0
        while starr2<len(exp):
             if exp[starr2] in('√', 't') and starr2+1<len(exp) and exp[starr2+1] in ('-', '/', '*'):
             	exp="ln(-1)"
             starr2+=1 
        if 'log()' in exp:
        	exp="log(0)"
        if '√()' in exp:
        	exp="log(0)"
        if len(exp)>0 and exp[len(exp)-1] in ('√', 'g', 't', '+', '-', '/', '%'):
        	exp=""
        # adding mod function
        bruno = 0
        while bruno < len(exp):
            bho = 1
            bhc = 0
            bcc = len(exp)
            if exp[bruno] == "|":
                inmodinc = exp[bruno:len(exp)]
                looper = 1
                while looper<len(exp) and bho != bhc:
                    if inmodinc[looper] == "|":
                        bhc = 1
                        bcc = looper
                    exp2 = exp[0:bruno] + f"(abs({inmodinc[1:bcc]}))" + inmodinc[bcc + 1:len(inmodinc)]
                    exp = exp2
                    looper += 1
            bruno += 1
        
        solo=0
        while solo<len(exp):
        	# to add a * before √
            if exp[solo] == "√":
                if solo > 0 and exp[solo - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", ")", "]", "|"):
                    exp2 = exp[0:solo] + "*" + exp[solo:len(exp)]
                    exp = exp2
            solo+=1
        # for adding a * before [
        kep = 0
        for kep in range(0, len(exp)):
            if exp[kep] == "[":
                if kep > 0 and exp[kep - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", ")", "]"):
                    exp = exp[0: kep] + "*" + exp[kep:len(exp)]
        # for gif function directly after √
        xg = 0
        while xg < len(exp):
            bopen2 = 1
            bclose2 = 0
            bcp2 = 0
            exp3 = exp
            if exp[xg] == "√" and exp[xg + 1] == "[":
                val2 = exp[exp.index("√") + 1:len(exp)]
                b2 = 1
                while bopen2 != bclose2:
                    if val2[b2] == "[":
                        bopen2 = bopen2 + 1
                    if val2[b2] == "]":
                        bclose2 = bclose2 + 1
                        bcp2 = val2.index("]")
                    b2 = b2 + 1
                exp3 = exp3[0:exp3.index("√")] + f"(math.sqrt{val2[0:bcp2 + 1]})" + val2[bcp2 + 1:len(val2)]
            xg = xg + 1
            exp = exp3

        # to separate log from numbers in root
        nom = 0
        while nom < len(exp):
            if exp[nom] == "m":
                if nom - 1 >= 0 and exp[nom - 1] in (
                        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")", "π", "e", "]", "|"):
                    exp2 = exp[0:nom] + "*" + exp[nom:len(exp)]
                    exp = exp2
            nom += 1

        # for adding * sign nefore and after π
        xc = 0
        while xc < len(exp):
            # to add a * before π
            if exp[xc] == "π":
                if xc > 0 and exp[xc - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")", "e", "]"):
                    exp2 = exp[0:xc] + "*" + exp[xc:len(exp)]
                    exp = exp2
            # to add a * after π
            if exp[xc] == "π":
                if xc + 1 != len(exp):
                    if exp[xc + 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", "(", "m", "√", "["):
                        exp2 = exp[0:xc + 1] + "*" + exp[xc + 1:len(exp)]
                        exp = exp2
            # to add  a * before e
            if exp[xc] == "e":
                if xc > 0 and exp[xc - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", ")", "]"):
                    exp2 = exp[0:xc] + "*" + exp[xc:len(exp)]
                    exp = exp2
            # to add a * after e
            if exp[xc] == "e":
                if xc + 1 != len(exp):
                    if exp[xc + 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", "(", "m", "√", "["):
                        exp2 = exp[0:xc + 1] + "*" + exp[xc + 1:len(exp)]
                        exp = exp2
            xc = xc + 1
        gz = 0
        while gz < len(exp):
            # for numbers directly written after √
            pss = 0
            sqbase = ""
            if exp[gz] == "√":
                pss = exp.index("√")
                if exp[gz + 1] not in ("(", "["):
                    # strcb string containing base
                    strcb = exp[gz + 1:len(exp)]
                    j = 0
                    while j < len(strcb) and strcb[j] not in ("+", "-", "/", "*", ")", "^"):
                        sqbase = strcb[0:j + 1]
                        j = j + 1
                    exp2 = exp[0:pss] + f"(math.sqrt({sqbase}))" + strcb[j:len(strcb)]
                    exp = exp2
                if exp[gz + 1] in ("["):
                    rest = exp[gz:len(exp)]
                    jd = 1
                    boz = 1
                    bcz = 0
                    posi = len(rest)
                    while boz != bcz:
                        if rest[jd] == "[":
                            boz += 1
                        if rest[jd] == "]":
                            bcz += 1
                            posi = jd
                        jd += 1
                    exp2 = exp[0:posi] + f"(math.sqrt({rest[0:posi + 1]}))" + rest[posi:len(rest)]
                    exp = exp2
            # for elements in brackets in √
            bopen = 1
            bclose = 0
            bcp = 0
            exp2 = exp
            if exp[gz] == "√" and exp[gz + 1] == "(":
                val = exp[exp.index("√") + 1:len(exp)]
                b = 1
                while bopen != bclose:
                    if val[b] == "(":
                        bopen = bopen + 1
                    if val[b] == ")":
                        bclose = bclose + 1
                        bcp = val.index(")")
                    b = b + 1
                exp2 = exp2[0:exp2.index("√")] + f"(math.sqrt{val[0:bcp + 1]})" + val[bcp + 1:len(val)]
                exp = exp2
            gz = gz + 1

        z1 = 0
        while z1 < len(exp):
            # to add  a * before (
            if exp[z1] == "(":
                if z1 > 0 and exp[z1 - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", ")", "]"):
                    exp2 = exp[0:z1] + "*" + exp[z1:len(exp)]
                    exp = exp2
            # to add a * after )
            if exp[z1] == ")":
                if z1 + 1 != len(exp):
                    if exp[z1 + 1] in (
                            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", "(", "m", "√", "[", "l"):
                        exp2 = exp[0:z1 + 1] + "*" + exp[z1 + 1:len(exp)]
                        exp = exp2
            z1 = z1 + 1

        # for greatest integer function
        xm = 0
        exp5 = ""
        while xm < len(exp):
            if exp[xm] == "[":
                posgifs = exp.index("[")
                stat = exp[posgifs:len(exp)]
                go = 1
                gc = 0
                xv = 1
                exp4=""
                glast = len(stat)
                while xv<len(exp) and go != gc:
                    if stat[xv] == "[":
                        go = go + 1
                    if stat[xv] == "]":
                        gc = gc + 1
                        glast = xv
                    xv = xv + 1
                if len(exp)>1:
                    exp4 = stat[1:glast]
                exp5 = exp.replace(exp[posgifs:posgifs + glast + 1], f"(math.floor({exp4}))")
                exp = exp5
            xm = xm + 1
        

        # for log with brackets
        ead = "".join(reversed(exp))
        shuru = 0
        while shuru < len(ead):
            if ead[shuru] == "g":
                if shuru > 0 and ead[shuru - 1] == "(":
                    tedit = ead[0:shuru]
                    beo = 1
                    bec = 0
                    becpos = 0
                    star = len(tedit) - 2
                    while beo != bec:
                        if tedit[star] == "(":
                            beo = beo + 1
                        if tedit[star] == ")":
                            bec = bec + 1
                            becpos = star
                        star -= 1
                        exp2 = ead[0:becpos] + ")" + ead[becpos:shuru] + "nl.htam" + "(" + ead[shuru + 8:len(ead)]
                    ead = exp2
            shuru += 1
        ead = ead.replace("nl", "gol")
        exp = "".join(reversed(ead))
        

        # for log without ( ) brackets
        x4 = 0
        while x4 < len(exp):
            if exp[x4] == "g":
                if exp[x4 + 1] != "(":
                    posg = exp.index("g")
                    strcl = exp[x4 + 1:len(exp)]
                    x5 = 0
                    while x5 < len(strcl) and strcl[x5] not in ("*", "/", "+", "-", "^"):
                        x5 = x5 + 1
                    if strcl[0] != "(":
                        exp2 = exp[0:posg - 7] + "(math.ln" + strcl[0:x5] + ")" + strcl[x5:len(
                            strcl)]  # changing log into ln to hide the letter g of used log and proceed
                        exp = exp2
            x4 = x4 + 1
        exp = exp.replace("ln", "log")
        

        # apna apna jugaad hai
        utk = 0
        while utk < len(exp):
            if utk > 0:
                if exp[utk] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", "m"):
                    if exp[utk - 1] == "g":
                        if utk + 1 < len(exp):
                            ext = exp[utk:len(exp)]
                            stop = len(exp)
                            tp = utk
                            while tp < len(exp):
                                if ext[0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                                    if exp[tp] in ("π", "e", "m", "(", "+", "-", "*", "/", "^", "√"):
                                        stop = tp
                                        tp = len(exp)
                                if ext[0] in ("π", "e"):
                                    if exp[tp] in (
                                            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", "+", "-", "*", "/",
                                            "^", "√"):
                                        stop = tp
                                        tp = len(exp)
                                if ext[0] == "m":
                                    if exp[tp] in ("+", "-", "*", "/", "^"):
                                        stop = tp
                                        tp = len(exp)

                                tp = tp + 1
                            exp2 = exp[0:utk] + "(" + exp[utk:stop] + ")" + exp[stop:len(exp)]
                            exp = exp2
                        else:
                            exp2 = exp[0:utk] + "(" + exp[utk:utk + 1] + ")"
                            exp = exp2
            utk = utk + 1

        x = 0
        while x < len(exp):
            # to add a * before √
            if exp[x] == "√":
                if x > 0 and exp[x - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", ")", "]", "|"):
                    exp2 = exp[0:x] + "*" + exp[x:len(exp)]
                    exp = exp2

            x = x + 1
        # combining elements of denominator after / sign in ( )
        x2 = 0
        while x2 < len(exp):
            if exp[x2] == "/":
                if exp[x2 + 1] == "(":
                    x2 = len(exp)
                else:
                    posdiv = exp.index("/")
                    strcd = exp[x2 + 1:len(exp)]
                    x3 = 0
                    while x3 < len(strcd) and strcd[x3] not in (",","*", "/", "+", "-"):
                        x3 = x3 + 1
                    if strcd[0] != "(":
                        exp2 = exp[0:posdiv] + "÷(" + strcd[0:x3] + ")" + strcd[x3:len(strcd)]
                        exp = exp2
            x2 = x2 + 1
        exp = exp.replace("÷", "/")
        exp = exp.replace("π", "math.pi")
        exp = exp.replace("e", "math.e")
        exp = exp.replace("cos", "math.cos")
        exp = exp.replace("sin", "math.sin")
        exp = exp.replace("tan", "math.tan")
        exp = exp.replace("math.smath.ec", "math.sec")
        exp = exp.replace("math.cosmath.ec", "math.cosec")
        exp = exp.replace("cot", "cot")
        exp = exp.replace("^", "**")
        
        forzero=0
        while forzero<len(exp):
        	if exp[0]=='0' and 1<len(exp) and exp[1] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
        		
        		exp=exp[1:len(exp)]
        		forzero=0
        		
        	forzero=forzero+1
        
        annihilatezero=0
        while annihilatezero<len(exp):
        	if exp[annihilatezero]=='0' and exp[annihilatezero-1] in ('+', '-', '/' , '*', '%', '√', '(', ')', '[', ']', '|') and annihilatezero+1<len(exp) and exp[annihilatezero+1] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
        		
        		
        		exp=exp[0:annihilatezero]+exp[annihilatezero+1:len(exp)]
        		annihilatezero=0
        	annihilatezero=annihilatezero+1
        
        self.aboutpy(exp)
        
        
        
        
        
    def show_history(self,root):
    	if os.path.exists("repos/database/history_database.db"):
    		conn = sqlite3.connect('repos/database/history_database.db')
    		c = conn.cursor()
    		c.execute("SELECT * FROM history")
    	else:
    		conn = sqlite3.connect('repos/database/history_database.db')
    		
    		c = conn.cursor()
    		c.execute("""CREATE TABLE if not exists history(expression text)""")
    		root.ids.s_history.text = 'No Data'
    	records = c.fetchall()
    	word = ""
    	for record in records:
    		word = f'{word}\n{record[0]}'
    		root.ids.s_history.text = f'{word}'
	
	
		
				
				
    def matex(self, expd):
        if os.path.exists("repos/database/history_database.db"):
            conn = sqlite3.connect('repos/database/history_database.db')
            c = conn.cursor()
            c.execute("INSERT INTO history VALUES (:first)",{'first': expd.text})
            conn.commit()
            conn.close()
            
        else:
        	conn = sqlite3.connect('repos/database/history_database.db')      
	        c = conn.cursor()
	        c.execute("""CREATE TABLE if not exists history(expression text)""")
	        c.execute("INSERT INTO history VALUES (:first)",{'first': expd.text})
	        conn.commit()
	        conn.close()
	        
	    
        
        import math
        exp = str(expd.text)
        exp = exp.lower()
        exp = exp.replace(" ", "")
        exp = exp.replace("÷", "/")
        exp = exp.replace("×", "*")
        exp = exp.replace("math.pi", "π")
        exp = exp.replace("math.e", "e")
        exp = exp.replace("pi", "π")
        exp = exp.replace("{", "(")
        exp = exp.replace("}", ")")
        exp = exp.replace("sqrt", "√")
        exp = exp.replace("math.sqrt", "√")
        
        exp = exp.replace("log", "math.log")
        exp = exp.replace("ln", "math.log")
        exp = exp.replace("math.math.log", "math.log")
        exp = exp.replace("antimath.log(", "math.pow(")
        exp = exp.replace("plus", "+")
        exp = exp.replace("minus", "-")
        exp = exp.replace("into", "*")
        exp = exp.replace("times", "*")
        exp = exp.replace("x", "*")
        exp = exp.replace("multiply", "*")
        exp = exp.replace("multipliedby", "*")
        exp = exp.replace("divide", "/")
        exp = exp.replace("dividedby", "/")
        exp = exp.replace("%", "%")
        exp = exp.replace("⁽", "^(")
        exp = exp.replace("⁺", "+")
        exp = exp.replace("⁻", "-")
        exp = exp.replace("⁾", ")")
        exp = exp.replace("⁽¹⁾", "^(1)")
        exp = exp.replace("⁽½⁾", "^(1)")
        exp = exp.replace("⁽⅓⁾","^(1/3)")
        exp = exp.replace("⁽¼⁾","^(1/4)")
        exp = exp.replace("⁽⅛⁾","^(1/8)")   
        exp = exp.replace("⁽²⁾","^2")
        exp = exp.replace("⁽⅔⁾","^(2/3)")
        exp = exp.replace("⁽³⁾","^(3)")
        exp = exp.replace("⁽¾⁾","^(3/4)")
        exp = exp.replace("⁽⅜⁾","^(3/8)")
        exp = exp.replace("⁽⁴⁾","^4")
        exp = exp.replace("⁽⅝⁾","^(5/8)")
        exp = exp.replace("⁽⅞⁾","^(7/8)")
       
        exp = exp.replace("¹","^1")       
        exp = exp.replace("½","^(1/2)")
        exp = exp.replace("⅓","^(1/3)")
        exp = exp.replace("¼","^(1/4)")
        exp = exp.replace("⅛","^(1/8)")   
        exp = exp.replace("²","^2")
        exp = exp.replace("⅔","^(2/3)")
        exp = exp.replace("³","^(3)")
        exp = exp.replace("¾","^(3/4)")
        exp = exp.replace("⅜","^(3/8)")
        exp = exp.replace("⁴","^4")
        exp = exp.replace("⅝","^(5/8)")
        exp = exp.replace("⅞","^(7/8)")        
        
        exp = exp.replace("raisedtothepowerof", "^")
        exp = exp.replace("raisedtothepower", "^")
        exp = exp.replace("tothepowerof", "^")
        exp = exp.replace("tothepower", "^")
        exp = exp.replace("squarerootof", "√")
        exp = exp.replace("squareroot", "√")
        
        exp = exp.replace("squared", "^2")
        exp = exp.replace("square", "^2")
        exp = exp.replace("e^(iπ)", "(-1)")
        exp = exp.replace("e^(i*π)", "(-1)")
        openmod = 0
        closemod = 0
        ptpk = 0
        while ptpk < len(exp):
            if exp[ptpk] == '|':
                openmod += 1
            ptpk+=1    
            if  ptpk<len(exp):
                 if exp[ptpk] =='|':
                     closemod += 1
            ptpk=ptpk+1
        if openmod-closemod!=0:
        	exp=exp+"|"

        # completing left brackets
        openbrac = 0
        closebrac = 0
        ptp = 0
        while ptp < len(exp):
            if exp[ptp] == '(':
                openbrac += 1
            if exp[ptp] == ')':
                closebrac += 1
            ptp += 1
        if openbrac-closebrac!=0:
           if openbrac>closebrac:
           	diff=openbrac-closebrac
           	while diff >0:
           		exp=exp+")"
           		diff-=1
           elif openbrac<closebrac:
           	diff=closebrac-openbrac
           	while diff >0:
           		exp="("+exp
           		diff-=1
        #wrong input in log   	
        starr=0
        while starr<len(exp):
             if exp[starr] == 'g' and starr+1<len(exp) and exp[starr+1] in ('+','-', '/', '*'):
             	exp="ln(-1)"
             starr+=1
       #wrong input in √  	
        starr2=0
        while starr2<len(exp):
             if exp[starr2] in('√', 't') and starr2+1<len(exp) and exp[starr2+1] in ('-', '/', '*'):
             	exp="ln(-1)"
             starr2+=1 
        if 'log()' in exp:
        	exp="log(0)"
        if '√()' in exp:
        	exp="log(0)"
        if len(exp)>0 and exp[len(exp)-1] in ('√', 'g', 't', '+', '-', '/', '%'):
        	exp=""
        # adding mod function
        bruno = 0
        while bruno < len(exp):
            bho = 1
            bhc = 0
            bcc = len(exp)
            if exp[bruno] == "|":
                inmodinc = exp[bruno:len(exp)]
                looper = 1
                while looper<len(exp) and bho != bhc:
                    if inmodinc[looper] == "|":
                        bhc = 1
                        bcc = looper
                    exp2 = exp[0:bruno] + f"(abs({inmodinc[1:bcc]}))" + inmodinc[bcc + 1:len(inmodinc)]
                    exp = exp2
                    looper += 1
            bruno += 1
        
        solo=0
        while solo<len(exp):
        	# to add a * before √
            if exp[solo] == "√":
                if solo > 0 and exp[solo - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", ")", "]", "|"):
                    exp2 = exp[0:solo] + "*" + exp[solo:len(exp)]
                    exp = exp2
            solo+=1
        # for adding a * before [
        kep = 0
        for kep in range(0, len(exp)):
            if exp[kep] == "[":
                if kep > 0 and exp[kep - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", ")", "]"):
                    exp = exp[0: kep] + "*" + exp[kep:len(exp)]
        # for gif function directly after √
        xg = 0
        while xg < len(exp):
            bopen2 = 1
            bclose2 = 0
            bcp2 = 0
            exp3 = exp
            if exp[xg] == "√" and exp[xg + 1] == "[":
                val2 = exp[exp.index("√") + 1:len(exp)]
                b2 = 1
                while bopen2 != bclose2:
                    if val2[b2] == "[":
                        bopen2 = bopen2 + 1
                    if val2[b2] == "]":
                        bclose2 = bclose2 + 1
                        bcp2 = val2.index("]")
                    b2 = b2 + 1
                exp3 = exp3[0:exp3.index("√")] + f"(math.sqrt{val2[0:bcp2 + 1]})" + val2[bcp2 + 1:len(val2)]
            xg = xg + 1
            exp = exp3

        # to separate log from numbers in root
        nom = 0
        while nom < len(exp):
            if exp[nom] == "m":
                if nom - 1 >= 0 and exp[nom - 1] in (
                        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")", "π", "e", "]", "|"):
                    exp2 = exp[0:nom] + "*" + exp[nom:len(exp)]
                    exp = exp2
            nom += 1

        # for adding * sign nefore and after π
        xc = 0
        while xc < len(exp):
            # to add a * before π
            if exp[xc] == "π":
                if xc > 0 and exp[xc - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")", "e", "]"):
                    exp2 = exp[0:xc] + "*" + exp[xc:len(exp)]
                    exp = exp2
            # to add a * after π
            if exp[xc] == "π":
                if xc + 1 != len(exp):
                    if exp[xc + 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", "(", "m", "√", "["):
                        exp2 = exp[0:xc + 1] + "*" + exp[xc + 1:len(exp)]
                        exp = exp2
            # to add  a * before e
            if exp[xc] == "e":
                if xc > 0 and exp[xc - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", ")", "]"):
                    exp2 = exp[0:xc] + "*" + exp[xc:len(exp)]
                    exp = exp2
            # to add a * after e
            if exp[xc] == "e":
                if xc + 1 != len(exp):
                    if exp[xc + 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", "(", "m", "√", "["):
                        exp2 = exp[0:xc + 1] + "*" + exp[xc + 1:len(exp)]
                        exp = exp2
            xc = xc + 1
        gz = 0
        while gz < len(exp):
            # for numbers directly written after √
            pss = 0
            sqbase = ""
            if exp[gz] == "√":
                pss = exp.index("√")
                if exp[gz + 1] not in ("(", "["):
                    # strcb string containing base
                    strcb = exp[gz + 1:len(exp)]
                    j = 0
                    while j < len(strcb) and strcb[j] not in ("+", "-", "/", "*", ")", "^"):
                        sqbase = strcb[0:j + 1]
                        j = j + 1
                    exp2 = exp[0:pss] + f"(math.sqrt({sqbase}))" + strcb[j:len(strcb)]
                    exp = exp2
                if exp[gz + 1] in ("["):
                    rest = exp[gz:len(exp)]
                    jd = 1
                    boz = 1
                    bcz = 0
                    posi = len(rest)
                    while boz != bcz:
                        if rest[jd] == "[":
                            boz += 1
                        if rest[jd] == "]":
                            bcz += 1
                            posi = jd
                        jd += 1
                    exp2 = exp[0:posi] + f"(math.sqrt({rest[0:posi + 1]}))" + rest[posi:len(rest)]
                    exp = exp2
            # for elements in brackets in √
            bopen = 1
            bclose = 0
            bcp = 0
            exp2 = exp
            if exp[gz] == "√" and exp[gz + 1] == "(":
                val = exp[exp.index("√") + 1:len(exp)]
                b = 1
                while bopen != bclose:
                    if val[b] == "(":
                        bopen = bopen + 1
                    if val[b] == ")":
                        bclose = bclose + 1
                        bcp = val.index(")")
                    b = b + 1
                exp2 = exp2[0:exp2.index("√")] + f"(math.sqrt{val[0:bcp + 1]})" + val[bcp + 1:len(val)]
                exp = exp2
            gz = gz + 1

        z1 = 0
        while z1 < len(exp):
            # to add  a * before (
            if exp[z1] == "(":
                if z1 > 0 and exp[z1 - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", ")", "]"):
                    exp2 = exp[0:z1] + "*" + exp[z1:len(exp)]
                    exp = exp2
            # to add a * after )
            if exp[z1] == ")":
                if z1 + 1 != len(exp):
                    if exp[z1 + 1] in (
                            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", "(", "m", "√", "[", "l"):
                        exp2 = exp[0:z1 + 1] + "*" + exp[z1 + 1:len(exp)]
                        exp = exp2
            z1 = z1 + 1

        # for greatest integer function
        xm = 0
        exp5 = ""
        while xm < len(exp):
            if exp[xm] == "[":
                posgifs = exp.index("[")
                stat = exp[posgifs:len(exp)]
                go = 1
                gc = 0
                xv = 1
                exp4=""
                glast = len(stat)
                while xv<len(exp) and go != gc:
                    if stat[xv] == "[":
                        go = go + 1
                    if stat[xv] == "]":
                        gc = gc + 1
                        glast = xv
                    xv = xv + 1
                if len(exp)>1:
                    exp4 = stat[1:glast]
                exp5 = exp.replace(exp[posgifs:posgifs + glast + 1], f"(math.floor({exp4}))")
                exp = exp5
            xm = xm + 1
        

        # for log with brackets
        ead = "".join(reversed(exp))
        shuru = 0
        while shuru < len(ead):
            if ead[shuru] == "g":
                if shuru > 0 and ead[shuru - 1] == "(":
                    tedit = ead[0:shuru]
                    beo = 1
                    bec = 0
                    becpos = 0
                    star = len(tedit) - 2
                    while beo != bec:
                        if tedit[star] == "(":
                            beo = beo + 1
                        if tedit[star] == ")":
                            bec = bec + 1
                            becpos = star
                        star -= 1
                        exp2 = ead[0:becpos] + ")" + ead[becpos:shuru] + "nl.htam" + "(" + ead[shuru + 8:len(ead)]
                    ead = exp2
            shuru += 1
        ead = ead.replace("nl", "gol")
        exp = "".join(reversed(ead))
        

        # for log without ( ) brackets
        x4 = 0
        while x4 < len(exp):
            if exp[x4] == "g":
                if exp[x4 + 1] != "(":
                    posg = exp.index("g")
                    strcl = exp[x4 + 1:len(exp)]
                    x5 = 0
                    while x5 < len(strcl) and strcl[x5] not in ("*", "/", "+", "-", "^"):
                        x5 = x5 + 1
                    if strcl[0] != "(":
                        exp2 = exp[0:posg - 7] + "(math.ln" + strcl[0:x5] + ")" + strcl[x5:len(
                            strcl)]  # changing log into ln to hide the letter g of used log and proceed
                        exp = exp2
            x4 = x4 + 1
        exp = exp.replace("ln", "log")
        

        # apna apna jugaad hai
        utk = 0
        while utk < len(exp):
            if utk > 0:
                if exp[utk] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", "m"):
                    if exp[utk - 1] == "g":
                        if utk + 1 < len(exp):
                            ext = exp[utk:len(exp)]
                            stop = len(exp)
                            tp = utk
                            while tp < len(exp):
                                if ext[0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                                    if exp[tp] in ("π", "e", "m", "(", "+", "-", "*", "/", "^", "√"):
                                        stop = tp
                                        tp = len(exp)
                                if ext[0] in ("π", "e"):
                                    if exp[tp] in (
                                            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", "+", "-", "*", "/",
                                            "^", "√"):
                                        stop = tp
                                        tp = len(exp)
                                if ext[0] == "m":
                                    if exp[tp] in ("+", "-", "*", "/", "^"):
                                        stop = tp
                                        tp = len(exp)

                                tp = tp + 1
                            exp2 = exp[0:utk] + "(" + exp[utk:stop] + ")" + exp[stop:len(exp)]
                            exp = exp2
                        else:
                            exp2 = exp[0:utk] + "(" + exp[utk:utk + 1] + ")"
                            exp = exp2
            utk = utk + 1

        x = 0
        while x < len(exp):
            # to add a * before √
            if exp[x] == "√":
                if x > 0 and exp[x - 1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "π", "e", ")", "]", "|"):
                    exp2 = exp[0:x] + "*" + exp[x:len(exp)]
                    exp = exp2

            x = x + 1
        # combining elements of denominator after / sign in ( )
        x2 = 0
        while x2 < len(exp):
            if exp[x2] == "/":
                if exp[x2 + 1] == "(":
                    x2 = len(exp)
                else:
                    posdiv = exp.index("/")
                    strcd = exp[x2 + 1:len(exp)]
                    x3 = 0
                    while x3 < len(strcd) and strcd[x3] not in (",","*", "/", "+", "-"):
                        x3 = x3 + 1
                    if strcd[0] != "(":
                        exp2 = exp[0:posdiv] + "÷(" + strcd[0:x3] + ")" + strcd[x3:len(strcd)]
                        exp = exp2
            x2 = x2 + 1
        exp = exp.replace("÷", "/")
        exp = exp.replace("π", "math.pi")
        exp = exp.replace("e", "math.e")
        exp = exp.replace("cos", "math.cos")
        exp = exp.replace("sin", "math.sin")
        exp = exp.replace("tan", "math.tan")
        exp = exp.replace("math.smath.ec", "math.sec")
        exp = exp.replace("math.cosmath.ec", "math.cosec")
        exp = exp.replace("cot", "cot")
        exp = exp.replace("^", "**")
        
        forzero=0
        while forzero<len(exp):
        	if exp[0]=='0' and 1<len(exp) and exp[1] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
        		
        		exp=exp[1:len(exp)]
        		forzero=0
        		
        	forzero=forzero+1
        
        annihilatezero=0
        while annihilatezero<len(exp):
        	if exp[annihilatezero]=='0' and exp[annihilatezero-1] in ('+', '-', '/' , '*', '%', '√', '(', ')', '[', ']', '|') and annihilatezero+1<len(exp) and exp[annihilatezero+1] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
        		
        		
        		exp=exp[0:annihilatezero]+exp[annihilatezero+1:len(exp)]
        		annihilatezero=0
        	annihilatezero=annihilatezero+1
     
        
        self.about(exp)
    
    
        
        
        	  
        

TTE().run()