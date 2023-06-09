import unittest
from unittest.mock import patch

from gicg_sim.die import DieState, _create_die_state_by_array
from gicg_sim.state import PlayerID, State
from gicg_sim.userboard import UserBoard


def roll_n_dies_patch(die_count: int) -> DieState:
    if die_count == 8:
        return _create_die_state_by_array([1, 1, 1, 1, 1, 1, 1, 1])
    else:
        return _create_die_state_by_array(
            [(die_count if i == 0 else 0) for i in range(8)]
        )


class TestReroll(unittest.TestCase):
    def setUp(self) -> None:
        self.state = State()
        self.player_1 = PlayerID.Player_1
        self.player_2 = PlayerID.Player_2
        self.userboard_1 = UserBoard(self.state, self.player_1)
        self.userboard_2 = UserBoard(self.state, self.player_2)

        self.userboard_1.add_character("Diluc")
        self.userboard_2.add_character("Diluc")

        with patch("gicg_sim.state.roll_n_dies", side_effect=roll_n_dies_patch):
            self.state.new_turn()
            keepdies_1 = _create_die_state_by_array([1, 1, 0, 0, 0, 0, 0, 0])
            keepdies_2 = _create_die_state_by_array([1, 0, 0, 0, 0, 0, 0, 0])

            self.userboard_1.reroll_dies(keepdies_1)
            self.userboard_2.reroll_dies(keepdies_2)

        return super().setUp()


if __name__ == "__main__":
    unittest.main()
