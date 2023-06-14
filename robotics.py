from RPA.Browser.Selenium import Selenium
from selenium.common.exceptions import NoSuchElementException
import re
from datetime import datetime

class Robot:
    def __init__(self, name):
        self.name = name
        self.scientistsdefault = ["Albert Einstein", "Marie Curie", "Isaac Newton"]
        self.scientistlist = list()
        self.browser = Selenium()

    def run(self):
        try:
            self.introduce()
            self.get_scientists(self.scientistsdefault)
            self.retrieve_scientist_information()
            self.display_information()
        except Exception as e:
            print(f"An error occurred during execution: {str(e)}")
        finally:
            self.say_goodbye()
            self.browser.close_all_browsers()

    def introduce(self):
        print("Hello! My name is "+self.name+" , your trusty Python software robot designed to unravel the secrets of famous scientists. My main goal is to retrieve valuable information about these celebrated physicians and present it to you in an easily digestible format. Lets embark on a journey through time and knowledge together! \n\nEquipped with advanced web-scraping capabilities and the power of Python, Ill navigate the vast realm of the internet to visit Wikipedia. There, I'll unearth the birth and death dates of renowned scientists and even calculate their ages for you. Also, I will extract the first paragraph from their Wikipedia pages, so that you get an idea of their main contributions.\n")

    def get_scientists(self,scientists):
        self.scientists = scientists
        print("Before we start, know that today we will be getting to know better the following scientists: " + ", ".join(scientists)+ ". If you're interested to add any other that you might be curious about, now it's your time. If you don´t want to add any, or you already added all the ones you are interested in, just say \"start\" and we will start immediately.\n")
        added = input("Add new scientist or start if you're ready: ")
        while added != "start":
            self.scientists.append(added)
            added = input("Add new scientist or start if you're ready: ")
        
    def say_goodbye(self):
        print("\n\nGoodbye, Thank you for entrusting me with the task of retrieving information from famous scientists. It has been an honor to serve you. Should you ever seek more knowledge or have any other inquiries, I'll be here, ready to assist you on your intellectual quests.\nUntil we meet again, stay curious, keep exploring, and let the wonders of science continue to inspire you.\n \nFarewell for now,\n "+ self.name+ ", Your Scientific Knowledge Robot")
        
        
    def retrieve_scientist_information(self):
        for scientist in self.scientists:
            try:
                self.navigate_to_wikipedia_page(scientist)
                print("Retrieving the desired information...\n")
                birth_date, death_date = self.retrieve_birth_and_death_dates()
                age = self.calculate_age(birth_date, death_date)
                intro_paragraph = self.retrieve_intro_paragraph()
                

                scientist_data = {
                    "scientist": scientist,
                    "birth_date": birth_date,
                    "death_date": death_date,
                    "age": age,
                    "intro_paragraph": intro_paragraph,
                }
                self.scientistlist.append(scientist_data)
                
            except NoSuchElementException:
                print(f"Failed to retrieve information for scientist: {scientist}")
            except Exception as e:
                print(f"An error occurred while processing {scientist}: {str(e)}")
                

    def navigate_to_wikipedia_page(self, scientist):
        print("Opening the wikipedia page for "+scientist+"\n")
        self.browser.open_available_browser(f"https://en.wikipedia.org/wiki/{scientist.replace(' ', '_')}")
        

    def retrieve_birth_and_death_dates(self):
        birth_date_element = self.browser.driver.find_element("xpath", "//span[@class='bday']")
        birth_date = datetime.strptime(birth_date_element.get_attribute("innerHTML"), "%Y-%m-%d").strftime("%eth of %B %Y") if birth_date_element else "Unknown"
        try:
            death_date_element = self.browser.driver.find_element("xpath", "//th[text()='Died']/following-sibling::td/span")
            death_date = datetime.strptime(death_date_element.get_attribute("innerHTML"), "(%Y-%m-%d)").strftime("%eth of %B %Y")
        except Exception:
            death_date = "Present"
        return birth_date, death_date

    def calculate_age(self,birth_date, death_date):
        today = datetime.now()
        death_date_d = datetime.strptime(death_date, "%dth of %B %Y") if death_date != "Present" else today
        if birth_date == "Unknown":
            age = "Unknown"
        else:
            birth_date_d = datetime.strptime(birth_date, "%dth of %B %Y")
            age = death_date_d.year - birth_date_d.year - ((death_date_d.month, death_date_d.day) < (birth_date_d.month, birth_date_d.day))
        return age

    def retrieve_intro_paragraph(self):
        try:
            intro_paragraph_element = self.browser.driver.find_element("xpath", "//p[b]")
            intro_paragraph = intro_paragraph_element.text if intro_paragraph_element else "No information available"
            intro_paragraph_clean = re.sub(r'\[.*?\]|\(.*?\)|\;.*?\)', '', intro_paragraph)
            return intro_paragraph_clean
        except NoSuchElementException:
            return "No information available"

    def display_information(self):
        for scientist, data in self.scientistdict.items():
            print(f"\nScientist: {data['scientist']}")
            print(f"Birth date: {data['birth_date']}")
            print(f"Death date: {data['death_date']}")
            print(f"Age: {data['age']}")
            print(f"Introduction: {data['intro_paragraph']}")


