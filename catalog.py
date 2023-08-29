from meeting import Meeting

class Catalog:
    def __init__(self, organizer, meeting):
        self.database = {}
        self.organizer = organizer
        self.meeting = meeting
 
    def savemeeting(self):
        self.database[self.organizer.name] = self.meeting

    def listallmeetings(self):
        for key,value in self.database.items():
            print("oragnizer is ", key)
            print("\n --------------------------- meeting info ----------------------- ")
            print("\nmeeting id --", value.id)
            print("\nmeeting interval --- ", value.duration)
            print("\nmeeting attendes --- ", )
            for user in value.participant:
                print(user.name, user.email)
            print("\nmeeting description --- ", value.subject)



