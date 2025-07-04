"""This is a standalone file for create a task in libero."""

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

    scene_name = "living_room_scene6"
    language = "arrange chocolate pudding, red coffee mug and porcelain mug in a straight line on the plate with the pudding in the center"
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=[
            "chocolate_pudding_1",
            "plate_1",
            "red_coffee_mug_1",
            "porcelain_mug_1",
        ],
        goal_states=[
            ("RelaxedOn", "chocolate_pudding_1", "plate_1"),
            ("RelaxedOn", "red_coffee_mug_1", "plate_1"),
            ("RelaxedOn", "porcelain_mug_1", "plate_1"),
            (
                "Linear",
                "red_coffee_mug_1",
                "chocolate_pudding_1",
                "porcelain_mug_1",
                0.005,
            ),
            (
                "Or",
                (
                    "Ordering",
                    "red_coffee_mug_1",
                    "chocolate_pudding_1",
                    "porcelain_mug_1",
                ),
                (
                    "Ordering",
                    "porcelain_mug_1",
                    "chocolate_pudding_1",
                    "red_coffee_mug_1",
                ),
            ),
            ("Not", ("RelaxedOn", "red_coffee_mug_1", "chocolate_pudding_1")),
            ("Not", ("RelaxedOn", "porcelain_mug_1", "chocolate_pudding_1")),
            ("Not", ("RelaxedOn", "red_coffee_mug_1", "porcelain_mug_1")),
        ],
    )

    bddl_file_names, failures = generate_bddl_from_task_info()
    print(bddl_file_names)


if __name__ == "__main__":
    main()
