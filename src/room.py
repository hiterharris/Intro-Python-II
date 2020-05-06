# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name="default name", description="default description", n_to=None, e_to=None, s_to=None, w_to=None, inventory=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to

    def __str__(self):
        return (self.name + ": " + self.description)
        
    def get_next_room_for_direction(self, direction):
        if hasattr(self, f'{direction}_to'):
            return getattr(self, f'{direction}_to')
        return None