from tkinter import*
from dota_hero_scrape import *


class Stats:
    def __init__(self, stats):
        self.intel = stats[0].text
        self.agi = stats[1].text
        self.stren = stats[2].text
        self.atk = stats[3].text
        self.ms = stats[4].text
        self.armor = stats[5].text

    def getAttributes(self):
        global int_stat, agi_stat, str_stat
        int_stat.config(text="Intelligence: "+ self.intel)
        agi_stat.config(text="Agility: " + self.agi)
        str_stat.config(text="Strength: "+self.stren)

class Spells:
    def __init__(self,spells):
        self.spell_1 = spells[0].h2.text
        self.spell_2 = spells[1].h2.text
        self.spell_3 = spells[2].h2.text
        self.ultimate_ = spells[3].h2.text
        try:
            self.spell_4 = spells[4].h2.text
        except:
            pass

    def get_spells(self):
        spell1.config(text=self.spell_1)
        spell2.config(text=self.spell_2)
        spell3.config(text=self.spell_3)
        ultimate.config(text=self.ultimate_)
        try:
            spell4.config(text=self.spell_4)
        except:
            pass







root = Tk()
root.title("Hero Collector")
var = StringVar(root)
var.set("Select a Hero")
o = OptionMenu(root, var, *hero_list.keys())
o.pack(side=LEFT)

hero_name = Label(root, text="None", font='BOLD')
int_stat = Label(root, text="")
agi_stat = Label(root, text="")
str_stat = Label(root, text="")

hero_spells_header = Label(root, text="Spells", font='BOLD')
spell1 = Label(root, text="")
spell2 = Label(root, text="")
spell3 = Label(root, text="")
ultimate = Label(root, text="")
spell4 = Label(root, text="")

hero_name.pack()
int_stat.pack()
agi_stat.pack()
str_stat.pack()
hero_spells_header.pack()
spell1.pack()
spell2.pack()
spell3.pack()
ultimate.pack()
spell4.pack()

def display_hero():
    curr_url = hero_list[var.get()]

    uClient2 = uReq(curr_url)
    page_html = uClient2.read()
    uClient2.close()

    # html parser
    page_soup2 = soup(page_html, "html.parser")

    # page_soup.p.text || gets the hero capabilities "melee, carry etc.."

    # grabs all hero stats
    stats = page_soup2.findAll("div", {"class": "overview_StatVal"})
    spells = page_soup2.findAll("div", {"class": "overviewAbilityRowDescription"})

    global hero_name
    global spell1, spell2, spell3, ultimate, spell4

    hero_name.config(text=page_soup2.h1.text)
    hero_stats = Stats(stats)
    hero_spells = Spells(spells)

    spell1.config(text="")
    spell2.config(text="")
    spell3.config(text="")
    ultimate.config(text="")
    try:
        spell4.config(text="")
    except:
        pass


    hero_stats.getAttributes()
    hero_spells.get_spells()


select_hero_button = Button(text="Show Overview", command=display_hero)
select_hero_button.pack(side=LEFT)



root.mainloop()
