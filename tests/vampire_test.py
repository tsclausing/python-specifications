import unittest
import tests

class VampireTest(unittest.TestCase):

    def test_can_select_any_vampire(self):
        basic_vampire_spec = (
            tests.CanBeKilledByDecapitation()
            & (~ tests.CanBeKilledByOldAge())
            & (~ tests.CanBeKilledBySilverBullet())
            & (~ tests.IsSeenDuringTheDay())
            & tests.IsSeenDuringTheNight())

        classic_vampire_spec = basic_vampire_spec & (
            tests.CanHaveRoommates()
            & tests.CanBeKilledByImmolation()
            & (~ tests.IsAlwaysMonsterous())
            & (~ tests.SparklesAtNight())
            & tests.CanBeKilledByStakeThroughTheHeart()
            & tests.CanChangeFormAtWill()
            & tests.ChangesFormByLightOfTheFullMoon())

        sparkly_vampire_spec = basic_vampire_spec & (
            tests.CanHaveRoommates()
            & tests.SparklesAtNight()
            & (~ tests.IsAlwaysMonsterous())
            & tests.CanBeKilledByImmolation()
            & tests.CanBeKilledByStakeThroughTheHeart()
            & tests.CanChangeFormAtWill()
            & tests.ChangesFormByLightOfTheFullMoon())

        zombie_vampire_spec = basic_vampire_spec & (
            tests.IsAlwaysMonsterous()
            & (~ tests.CanHaveRoommates())
            & (~ tests.SparklesAtNight())
            & (~ tests.CanBeKilledByImmolation())
            & (~ tests.CanBeKilledByStakeThroughTheHeart())
            & (~ tests.CanChangeFormAtWill())
            & (~ tests.ChangesFormByLightOfTheFullMoon()))

        any_vampire_spec = (
            classic_vampire_spec
            | sparkly_vampire_spec
            | zombie_vampire_spec)

        self.assertFalse(basic_vampire_spec.is_satisfied_by(tests.Person()))
        self.assertFalse(classic_vampire_spec.is_satisfied_by(tests.Person()))
        self.assertFalse(sparkly_vampire_spec.is_satisfied_by(tests.Person()))
        self.assertFalse(zombie_vampire_spec.is_satisfied_by(tests.Person()))
        self.assertFalse(any_vampire_spec.is_satisfied_by(tests.Person()))

        self.assertTrue(basic_vampire_spec.is_satisfied_by(tests.Vampire()))
        self.assertTrue(classic_vampire_spec.is_satisfied_by(tests.Vampire()))
        self.assertFalse(sparkly_vampire_spec.is_satisfied_by(tests.Vampire()))
        self.assertFalse(zombie_vampire_spec.is_satisfied_by(tests.Vampire()))
        self.assertTrue(any_vampire_spec.is_satisfied_by(tests.Vampire()))

        self.assertTrue(basic_vampire_spec.is_satisfied_by(tests.SillyVampire()))
        self.assertFalse(classic_vampire_spec.is_satisfied_by(tests.SillyVampire()))
        self.assertTrue(sparkly_vampire_spec.is_satisfied_by(tests.SillyVampire()))
        self.assertFalse(zombie_vampire_spec.is_satisfied_by(tests.SillyVampire()))
        self.assertTrue(any_vampire_spec.is_satisfied_by(tests.SillyVampire()))

        self.assertTrue(basic_vampire_spec.is_satisfied_by(tests.Zompire()))
        self.assertFalse(classic_vampire_spec.is_satisfied_by(tests.Zompire()))
        self.assertFalse(sparkly_vampire_spec.is_satisfied_by(tests.Zompire()))
        self.assertTrue(zombie_vampire_spec.is_satisfied_by(tests.Zompire()))
        self.assertTrue(any_vampire_spec.is_satisfied_by(tests.Zompire()))

        self.assertFalse(basic_vampire_spec.is_satisfied_by(tests.Werewolf()))
        self.assertFalse(classic_vampire_spec.is_satisfied_by(tests.Werewolf()))
        self.assertFalse(sparkly_vampire_spec.is_satisfied_by(tests.Werewolf()))
        self.assertFalse(zombie_vampire_spec.is_satisfied_by(tests.Werewolf()))
        self.assertFalse(any_vampire_spec.is_satisfied_by(tests.Werewolf()))

        self.assertFalse(basic_vampire_spec.is_satisfied_by(tests.Zombie()))
        self.assertFalse(classic_vampire_spec.is_satisfied_by(tests.Zombie()))
        self.assertFalse(sparkly_vampire_spec.is_satisfied_by(tests.Zombie()))
        self.assertFalse(zombie_vampire_spec.is_satisfied_by(tests.Zombie()))
        self.assertFalse(any_vampire_spec.is_satisfied_by(tests.Zombie()))

        self.assertFalse(basic_vampire_spec.is_satisfied_by(tests.JasonVoorhees()))
        self.assertFalse(classic_vampire_spec.is_satisfied_by(tests.JasonVoorhees()))
        self.assertFalse(sparkly_vampire_spec.is_satisfied_by(tests.JasonVoorhees()))
        self.assertFalse(zombie_vampire_spec.is_satisfied_by(tests.JasonVoorhees()))
        self.assertFalse(any_vampire_spec.is_satisfied_by(tests.JasonVoorhees()))
