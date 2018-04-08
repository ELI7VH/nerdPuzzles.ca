logo =[
"",
"",
"  _______________________________.____",
"  \______   \_   _____/\______   \    |",
"   |       _/|    __)_  |     ___/    |",
"   |    |   \|        \ |    |   |    |___",
"   |____|_  /_______  / |____|   |_______ \\",
"          \/        \/                   \/",
"  __________ ___________________._._._._._.",
"  \______   \\\\_____  \__    ___/| | | | | |",
"   |    |  _/ /   |   \|    |   | | | | | |",
"   |    |   \/    |    \    |    \|\|\|\|\|",
"   |______  /\_______  /____|    __________",
"          \/         \/          \/\/\/\/\/",
"",
"     The hall monitor that nobody likes.",
""
]

import urllib.request
import urllib.parse
import json
import os
import time
import sys

challenges = []
weeks = 6
students = {}
# classroom_list = ['eli7vh','shylocliffe','cheneil','georgewong','Cytokinesis']
site = "https://repl.it/@"

class Student:

    site = "https://repl.it/@"
    completed_weeks = []
    progress = ""

    def __init__(self, name):
        self.name = name
        self.site = self.site + name + "/"

    def __str__(self):
        return self.name

    def finished_week(self, week_number):
        self.completed_weeks.append(week_number)

    def check_student_progress(self,last_known_week,challenges,betas):

        # print(last_known_week)
        self.progress = last_known_week
        msg(["checking progress for", self.name])
        url = ""
        url_beta = ""

        for week,beta in zip(challenges, betas):
            url = self.site + week
            url_beta = self.site + beta

            msg(["searching",url,str(last_known_week)])

            try:
                x = urllib.request.Request(url)
                res = urllib.request.urlopen(url)

                self.progress += 1

            except urllib.error.HTTPError as e:

                try:
                    msg(["searching",url_beta])
                    x = urllib.request.Request(url_beta)
                    res = urllib.request.urlopen(url_beta)
                    msg([url_beta[-6:],"found"])

                    return self.progress, True

                except urllib.error.HTTPError as e:

                    return self.progress, False

                code = json.loads(e.read().decode("utf-8"))
                # try:


                if code["status"] == 404:
                    msg(["url not found by", self.name, "for", week])
                    msg(["REPLBOT ANGRY"])
                    msg(["sending dikpik to the slacker"])
                    return self.progress, False

        return(self.progress, False)
# progress_bar / percent_completed
# add persistence - export json or something else for django to use

def msg(message_list, slow=False, message_type='text'): # ELI7VH's magical message method v1.2
    # input ['some','list'] to continue. can also be a ['single element list']

    print()

    sleep = 0.005 if slow == False else 0.03

    for element in message_list:
        for letter in element:
            print(letter, end='', flush='True')

            if slow==True:
                time.sleep(sleep)

        if message_type == 'logo':
            print(' ', flush='True')
        else:
            print(' ', end='', flush='True')

        time.sleep(sleep*20)

    print()

def main(username, last_known_week = 1, classroom_total_weeks = 6):

    # msg(logo,slow=False,message_type="logo")
    # check if username is in the list of registered users
    # add argument to start at the last checked week.
    # if username not in classroom_list:
    #     return "That user is not in the class!"

    beta = False

    challenges = []
    betas = []
    le_input = username
    start = last_known_week
    print(start,"<<<ASDFDSAF")

    for challenge in range(start + 1, classroom_total_weeks + 1):
        week_double_digit_check = "%02d" % challenge
        challenges.append("week" + week_double_digit_check)
        betas.append("beta" + week_double_digit_check)

    print(betas)
    print(challenges)

    le_student = Student(le_input)

    progress, beta = le_student.check_student_progress(start,challenges,betas)

    return progress, beta

if __name__ == '__main__':
    main()

# Shit to consider
# migrations.CreateModel(
#     name='Question',
#     fields=[
#         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
#         ('question_text', models.CharField(max_length=200)),
#         ('pub_date', models.DateTimeField(verbose_name='date published')),
#     ],
# ),
