from Systems import InputSystem

class EditorGUIManager():
    def __init__(self):
        self.elements = []
        self.windows = []

    @classmethod
    def is_mouse_hovering_gui(self, obj):
        if not (hasattr(obj, "width") or hasattr(obj, "height") or hasattr(obj, "x") or hasattr(obj, "y")): return
        x, y = obj.get_screen_position()
        left_x, right_x, top_y, bottom_y = self.get_screen_measurements(x=x, y=y, width=obj.width, height=obj.height)
        return self.is_mouse_inside(left_x, right_x, top_y, bottom_y)

    @classmethod
    def click_on_gui(self, obj):
        return InputSystem.was_mouse_pressed() and self.is_mouse_hovering_gui(obj)

    @classmethod
    def is_mouse_inside(self, left_x, right_x, top_y, bottom_y):
        mx, my = InputSystem.get_mouse_pos()
        return left_x <= mx <= right_x and top_y <= my <= bottom_y

    @classmethod
    def get_screen_measurements(self, x, y, width, height):
        left_x = int(x - width / 2)
        right_x = int(x + width / 2)
        top_y = int(y - height / 2)
        bottom_y = int(y + height / 2)
        return left_x, right_x, top_y, bottom_y

    @classmethod
    def add_element(self, element):
        self.elements.append(element)

    def update(self):
        pass


