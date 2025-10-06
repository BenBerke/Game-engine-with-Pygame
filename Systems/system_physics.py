class PhysicsSystem:
    rigidbodies = []
    colliders = []

    @classmethod
    def register_rigidbody(cls, rigidbody):
        cls.rigidbodies.append(rigidbody)

    @classmethod
    def unregister_rigidbody(cls, rigidbody):
        if rigidbody in cls.rigidbodies:
            cls.rigidbodies.remove(rigidbody)

    @classmethod
    def register_collider(cls, collider):
        cls.colliders.append(collider)

    @classmethod
    def unregister_collider(cls, collider):
        if collider in cls.colliders:
            cls.colliders.remove(collider)

    @classmethod
    def update(cls):
        for rb in cls.rigidbodies:
            rb.update()
        for i in range(len(cls.colliders)):
            a = cls.colliders[i]
            if not a:
                continue
            for j in range(i + 1, len(cls.colliders)):
                b = cls.colliders[j]
                if not b:
                    continue
                cls.check_collision(a, b)



    @classmethod
    def check_collision(cls, collision_a, collision_b):
        from Components.component_rigidbody import Rigidbody
        from Components.component_transform import Transform

        ax, ay, aw, ah = collision_a.rect()
        bx, by, bw, bh = collision_b.rect()

        dx = (ax + aw / 2) - (bx + bw / 2)
        dy = (ay + ah / 2) - (by + bh / 2)

        overlap_x = (aw + bw) / 2 - abs(dx)
        overlap_y = (ah + bh) / 2 - abs(dy)

        rb_a = collision_a.owner.get_component(Rigidbody)
        rb_b = collision_b.owner.get_component(Rigidbody)

        if overlap_x > 0 and overlap_y > 0:
            if overlap_x < overlap_y:
                # Resolve X
                if dx > 0:
                    collision_a.owner.get_component(Transform).world_position.x += overlap_x
                else:
                    collision_a.owner.get_component(Transform).world_position.x -= overlap_x
                # Stop horizontal velocity if moving into collider
                if rb_a and ((dx > 0 and rb_a.velocity.x < 0) or (dx < 0 and rb_a.velocity.x > 0)):
                    rb_a.velocity.x = 0
            else:
                if overlap_y > 0:
                    if dy > 0:
                        collision_a.owner.get_component(Transform).world_position.y += overlap_y
                    else:
                        collision_a.owner.get_component(Transform).world_position.y -= overlap_y
                    if rb_a:
                        rb_a.velocity.y = 0

