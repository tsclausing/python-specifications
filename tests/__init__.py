from specs.specs import Composite


class Person(object):
    def __init__(self):
        self.can_have_roommates = True
        self.is_seen_during_the_day = True
        self.is_seen_during_the_night = True
        self.is_always_monsterous = False
        self.can_change_form_at_will = False
        self.changes_form_by_light_of_the_full_moon = False
        self.sparkles_at_night = False
        self.can_be_killed_by_decapitation = True
        self.can_be_killed_by_immolation = True
        self.can_be_killed_by_old_age = True
        self.can_be_killed_by_silver_bullet = True
        self.can_be_killed_by_stake_through_the_heart = True


class Vampire(Person):
    def __init__(self):
        super(Vampire, self).__init__()
        self.is_seen_during_the_day = False
        self.can_change_form_at_will = True
        self.can_be_killed_by_old_age = False
        self.can_be_killed_by_silver_bullet = False
        self.changes_form_by_light_of_the_full_moon = True


class SillyVampire(Vampire):
    def __init__(self):
        super(SillyVampire, self).__init__()
        self.sparkles_at_night = True
        self.can_be_killed_by_silver_bullet = False


class Zompire(Vampire):
    def __init__(self):
        super(Zompire, self).__init__()
        self.is_always_monsterous = True
        self.can_have_roommates = False
        self.can_change_form_at_will = False
        self.changes_form_by_light_of_the_full_moon = False
        self.can_be_killed_by_immolation = False
        self.can_be_killed_by_stake_through_the_heart = False


class Werewolf(Person):
    def __init__(self):
        super(Werewolf, self).__init__()
        self.changes_form_by_light_of_the_full_moon = True
        self.can_be_killed_by_stake_through_the_heart = False


class CanHaveRoommates(Composite):
    def is_satisfied_by(self, person):
        return person.can_have_roommates


class CanBeKilledByDecapitation(Composite):
    def is_satisfied_by(self, person):
        return person.can_be_killed_by_decapitation


class CanBeKilledByOldAge(Composite):
    def is_satisfied_by(self, person):
        return person.can_be_killed_by_old_age


class CanBeKilledByStakeThroughTheHeart(Composite):
    def is_satisfied_by(self, person):
        return person.can_be_killed_by_stake_through_the_heart


class CanBeKilledBySilverBullet(Composite):
    def is_satisfied_by(self, person):
        return person.can_be_killed_by_silver_bullet


class CanBeKilledByImmolation(Composite):
    def is_satisfied_by(self, person):
        return person.can_be_killed_by_immolation


class CanChangeFormAtWill(Composite):
    def is_satisfied_by(self, person):
        return person.can_change_form_at_will


class ChangesFormByLightOfTheFullMoon(Composite):
    def is_satisfied_by(self, person):
        return person.changes_form_by_light_of_the_full_moon


class IsAlwaysMonsterous(Composite):
    def is_satisfied_by(self, person):
        return person.is_always_monsterous


class IsSeenDuringTheNight(Composite):
    def is_satisfied_by(self, person):
        return person.is_seen_during_the_night


class IsSeenDuringTheDay(Composite):
    def is_satisfied_by(self, person):
        return person.is_seen_during_the_day


class SparklesAtNight(Composite):
    def is_satisfied_by(self, person):
        return person.sparkles_at_night