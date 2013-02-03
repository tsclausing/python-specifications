import unittest
import tests

class VampireTest(unittest.TestCase):
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

    def test_satisfaction(self):
        self.assertFalse(VampireTest.basic_vampire_spec.is_satisfied_by(tests.Person()))
        self.assertFalse(VampireTest.classic_vampire_spec.is_satisfied_by(tests.Person()))
        self.assertFalse(VampireTest.sparkly_vampire_spec.is_satisfied_by(tests.Person()))
        self.assertFalse(VampireTest.zombie_vampire_spec.is_satisfied_by(tests.Person()))
        self.assertFalse(VampireTest.any_vampire_spec.is_satisfied_by(tests.Person()))

        self.assertTrue(VampireTest.basic_vampire_spec.is_satisfied_by(tests.Vampire()))
        self.assertTrue(VampireTest.classic_vampire_spec.is_satisfied_by(tests.Vampire()))
        self.assertFalse(VampireTest.sparkly_vampire_spec.is_satisfied_by(tests.Vampire()))
        self.assertFalse(VampireTest.zombie_vampire_spec.is_satisfied_by(tests.Vampire()))
        self.assertTrue(VampireTest.any_vampire_spec.is_satisfied_by(tests.Vampire()))

        self.assertTrue(VampireTest.basic_vampire_spec.is_satisfied_by(tests.SillyVampire()))
        self.assertFalse(VampireTest.classic_vampire_spec.is_satisfied_by(tests.SillyVampire()))
        self.assertTrue(VampireTest.sparkly_vampire_spec.is_satisfied_by(tests.SillyVampire()))
        self.assertFalse(VampireTest.zombie_vampire_spec.is_satisfied_by(tests.SillyVampire()))
        self.assertTrue(VampireTest.any_vampire_spec.is_satisfied_by(tests.SillyVampire()))

        self.assertTrue(VampireTest.basic_vampire_spec.is_satisfied_by(tests.Zompire()))
        self.assertFalse(VampireTest.classic_vampire_spec.is_satisfied_by(tests.Zompire()))
        self.assertFalse(VampireTest.sparkly_vampire_spec.is_satisfied_by(tests.Zompire()))
        self.assertTrue(VampireTest.zombie_vampire_spec.is_satisfied_by(tests.Zompire()))
        self.assertTrue(VampireTest.any_vampire_spec.is_satisfied_by(tests.Zompire()))

        self.assertFalse(VampireTest.basic_vampire_spec.is_satisfied_by(tests.Werewolf()))
        self.assertFalse(VampireTest.classic_vampire_spec.is_satisfied_by(tests.Werewolf()))
        self.assertFalse(VampireTest.sparkly_vampire_spec.is_satisfied_by(tests.Werewolf()))
        self.assertFalse(VampireTest.zombie_vampire_spec.is_satisfied_by(tests.Werewolf()))
        self.assertFalse(VampireTest.any_vampire_spec.is_satisfied_by(tests.Werewolf()))

