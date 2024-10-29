class Course:
    def __init__(self, title, schedule, description):
        self.title = title
        self.schedule = schedule
        self.description = description

    def get_title(self):
        return self.title

    def get_schedule(self):
        return self.schedule

    def get_description(self):
        return self.description

    def __str__(self):
        output = ''
        output += f'Title: {self.title}\nSchedule: {self.schedule}\nDescription: {self.description}\n'
        output += '------------------'
        return output