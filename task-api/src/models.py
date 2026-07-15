class Task:
    def __init__(self, title, description='', priority='medium'):
        self.id = None
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'completed': self.completed
        }
