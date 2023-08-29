from user import User
from meeting import Meeting
from scheduler import Scheduler

if __name__ == "__main__":
    print("start meeting scheduler")
    user1 = User("shubham", "shubham@vmware.com")
    user2 = User("dinesh", "dinesh@vmware.com")
    user3 = User("mitali", "mitali@vmware.com")


    participant = []
    participant.append(user2)
    participant.append(user3)

    scheduler = Scheduler(user1)
    scheduler.schedulemeeting(30, participant)
    

