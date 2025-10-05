# Components/__init__.py

# Core components
from .component_rigidbody import Rigidbody
from .component_transform import Transform
from .component_box_collider import BoxCollider
from .component_sprite_renderer import SpriteRenderer

# Test_Behaviours subpackage
from .Test_Behaviours.test_behaviour import TestBehaviour

#list of all components for dynamic access
ALL_COMPONENTS = {
    "Rigidbody": Rigidbody,
    "Transform": Transform,
    "BoxCollider": BoxCollider,
    "SpriteRenderer": SpriteRenderer,
}

