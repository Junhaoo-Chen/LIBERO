"""This is a standalone file for creating a task in libero."""
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

    # Write your reward code here
    scene_name = "kitchen_scene5"
    language = "Push the bowl until it touches the ketchup"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["ketchup_1", "akita_black_bowl_1"],
        goal_states=[
            ("InContact", "akita_black_bowl_1", "ketchup_1"),
            ("PositionWithin", "akita_black_bowl_1", 0.02, -0.05, 0.89, 1, 1, 0.01),
            ("PositionWithin", "ketchup_1", -0.09, -0.09, 0.97, 1, 1, 0.01),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
