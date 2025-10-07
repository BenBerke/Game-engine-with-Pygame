from .component_rigidbody import Rigidbody
from .component_transform import Transform
from .component_box_collider import BoxCollider
from .component_sprite_renderer import SpriteRenderer
from .component_text_renderer import TextRenderer
from .component_debugger import Debugger
from .component_camera import Camera


ALL_COMPONENTS = {
    "Rigidbody": Rigidbody,
    "Transform": Transform,
    "BoxCollider": BoxCollider,
    "SpriteRenderer": SpriteRenderer,
    "TextRenderer": TextRenderer,
    "Debugger": Debugger,
    "Camera": Camera,

}

