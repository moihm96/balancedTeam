from unittest import TestCase

from BalancedTeams import player_split

ids = ["Alice", "Bob", "Coral", "David"]
scores = [4.5, 6.1, 5.2, 4.7]

ids1 = ["Felipe", "Joao", "Thiago", "Leao", "Veronica", "Luisa", "Marta", "Cynthia"]
scores1 = [7.1, 7.9, 10, 7.5, 6.5, 5.7, 1.2, 6.9]


class TestPlayer_split(TestCase):
    def test_player_split(self):
        self.assertEqual(player_split(ids, scores), (["Bob", "Alice"], ["Coral", "David"]))
        self.assertEquals(player_split(ids1, scores1), (['Thiago', 'Felipe', 'Cynthia', 'Marta'], ['Joao', 'Leao',
                                                                                                   'Veronica', 'Luisa']))

    def test_player_split_wrong(self):
        self.assertFalse(player_split(ids, scores) == (["Coral", "Bob"], ["Alice", "David"]))
        self.assertFalse(player_split(ids1, scores1) == (['Thiago', 'Felipe', 'Cynthia', 'Marta'], ['Joao', 'Leao',
                                                                                                   'Veronica', 'Luisa']))