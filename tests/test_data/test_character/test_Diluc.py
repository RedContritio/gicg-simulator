from game_init import prepare_game

from gicg_sim.basic.event.operation import PlayerOpUseSkill
from gicg_sim.basic.subtypes import CharacterID, PlayerID, SkillID
from gicg_sim.game.manager import GameManager


def test_Diluc_attack() -> None:
    game: GameManager = prepare_game()

    game.take_operation(PlayerOpUseSkill(
        skill_id=SkillID('Tempered Sword'),
        player_id=PlayerID(1), character_id=CharacterID(1)
    ))

    assert game.game_state.side2.characters[0].hp == 8
