import numpy as np

from libero.libero.utils.bddl_generation_utils import (
    get_xy_region_kwargs_list_from_regions_info,
)
from libero.libero.utils.mu_utils import register_mu, InitialSceneTemplates
from libero.libero.utils.task_generation_utils import (
    register_task_info,
    get_task_info,
    generate_bddl_from_task_info,
)
from libero.libero.benchmark.mu_creation import *

def main():
    scene_name = "living_room_scene2"
    language = "Stand the ketchup bottle upside down on top of the tomato sauce can."
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["tomato_sauce_1","ketchup_1"],
        goal_states=[
            ("AxisAlignedWithin", "ketchup_1", "y", 170, 180),
            ("On", "ketchup_1", "tomato_sauce_1")
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()