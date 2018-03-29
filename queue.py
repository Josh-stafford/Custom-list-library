import listlib

class Queue:

    def __init__(this):

        this.data = False

    def push(this, data):
        if not this.data:
            this.data = listlib.list(data)
        else:
            this.data.push(data)

    def pop(this):

        temp = this.data.start.data
        this.data.remove(0)
        return temp

    def peek(this):
        return this.data.start.data
