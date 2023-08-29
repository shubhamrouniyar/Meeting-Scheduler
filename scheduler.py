from meeting import Meeting
from catalog import Catalog

class Scheduler:
    def __init__(self, organizer):
        self.organizer = organizer
    def schedulemeeting(self, duration, participant):
        meeting1 = Meeting(12987, 30, participant, "Quick discussion on Q1 Results")
        catalog = Catalog(self.organizer, meeting1)
        catalog.savemeeting()
        print("listing all meetings")
        catalog.listallmeetings()

    def cancelmeeting(self):
        pass
    
    def checkavailability(self,duration, participant):
        pass

