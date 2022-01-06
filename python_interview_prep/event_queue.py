class Queue_handler:
    def __init__(self):
        self.list = []
        self.status_list = []

    def push(self, item):
        self.list.append(item)

    def __len__(self):
        return len(self.list)

    def pop(self):
        x = self.list.pop(0)
        # print(x.return_object().event_type)
        # this handles status request
        if x.return_object().event_type == 'S':
            self.status_list.append(x.return_object().status_type)
            self.handle_status_event(x)

        # This handles the Event Request
        if x.return_object().event_type == 'R':
            # print(x.return_object().event_type,x.return_object().retry_count)
            if len(self.status_list) >= 1:
                if self.status_list.pop() == 'C' or self.status_list.pop() == 'T':
                    print(f"EventRequest: {x.return_object().event_type}, {x.return_object().retry_count}")
                else:
                    x.return_object().retry_count = x.return_object().retry_count + 1
                    self.push(Process(x.return_object().event_type, x.return_object().retry_count))

    def handle_status_event(self, x):
        if x.return_object().status_type == 'C' or x.return_object().status_type == 'T':
            if x.return_object().retry_count < 2:
                x.return_object().retry_count += 1
                self.push(
                    Process(x.return_object().event_type, x.return_object().status_type, x.return_object().retry_count))
        print(f"Event Status: {x.return_object().event_type}, {x.return_object().status_type}, {x.return_object().retry_count}")


class EventRequest:
    def __init__(self, event_type, retry_count):
        self.event_type = event_type
        self.retry_count = retry_count


class EventStatus:
    def __init__(self, event_type, status_type, retry_count):
        self.event_type = event_type
        self.status_type = status_type
        self.retry_count = retry_count


class Process:
    def __init__(self, *args):
        if len(args) == 2:
            self.e1 = EventRequest(args[0], args[1])
        else:
            self.e1 = EventStatus(args[0], args[1], args[2])

    def return_object(self):
        return self.e1

# here is pushed data to event queue.


q1 = Queue_handler()
q1.push(Process("S", "M", 0))
q1.push(Process("S", "C", 0))
q1.push(Process("R", 0))
q1.pop()
q1.pop()
q1.pop()



# print(p1)
