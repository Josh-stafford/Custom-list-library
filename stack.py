import listlib

class Stack:

    def __init__(this):

        this.data = False

    def push(this, data):

        if not this.data:
            this.data = listlib.list(data)
        else:
            this.data.push(data)

    def pop(this):

        temp = this.data.find(this.data.length-1)
        this.data.remove(this.data.length-1)

        return temp.data

    def peek(this):
        return this.data.find(this.data.length-1).data
