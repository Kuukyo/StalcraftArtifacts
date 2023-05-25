import lib


def get_value(property, quality: float, potential: int, negative=False, extra=False):
    min = property[0]
    max = property[1]
    diff = max - min

    if extra:
        if quality < 100:
            return round((min + diff * quality / 100) * (1 + potential * 0.02), 2)

        return round(max * quality / 100 * (1 + potential * 0.02), 2)

    if (negative or min < 0) and (not (negative and min < 0)):
        if quality < 100:
            return round(min + diff / 100 * quality, 2)
        if quality < 150:
            return round(min + (80 + (quality % 10) * 2) / 100 * diff, 2)
        if quality == 150:
            return max
        if quality < 170:
            return round(max + (80 + (quality - 150) * 2) / 100 * diff, 2)
        return round(min + (80 + (quality % 10) * 2) / 100 * diff, 2)

    if quality < 100:
        return round((min + diff * quality / 100) * (1 + potential * 0.02), 2)

    return round(max * quality / 100 * (1 + potential * 0.02), 2)


class Artifact:
    def __init__(self, name: str, quality: float, potential: int):
        artifacts = lib.load_mem("../resources/artifacts.json")
        artifact = artifacts[name]

        self.quality = quality
        self.potential = potential
        self.vitality = get_value(artifact["vitality"], quality, potential)
        self.stamina_regen = get_value(artifact["stamina_regen"], quality, potential)
        self.psy_emissions = get_value(artifact["psy_emissions"], quality, potential, True)
        self.psy_emissions_protection = get_value(artifact["psy_emissions_protection"], quality, potential)
        self.stamina = get_value(artifact["stamina"], quality, potential)
        self.movement_speed = get_value(artifact["movement_speed"], quality, potential)
        self.temperature = get_value(artifact["temperature"], quality, potential, True)
        self.reaction_to_electricity = get_value(artifact["reaction_to_electricity"], quality, potential)
        self.radiation = get_value(artifact["radiation"], quality, potential, True)
        self.biological_infection = get_value(artifact["biological_infection"], quality, potential, True)
        self.thermal_protection = get_value(artifact["thermal_protection"], quality, potential)
        self.psy_emission_resistance = get_value(artifact["psy_emission_resistance"], quality, potential)
        self.carry_weight = get_value(artifact["carry_weight"], quality, potential)
        self.radiation_protection = get_value(artifact["radiation_protection"], quality, potential)
        self.healing_effectiveness = get_value(artifact["healing_effectiveness"], quality, potential)
        self.bullet_resistance = get_value(artifact["bullet_resistance"], quality, potential)
        self.explosion_protection = get_value(artifact["explosion_protection"], quality, potential)
        self.radiation_resistance = get_value(artifact["radiation_resistance"], quality, potential)
        self.bioinfection_resistance = get_value(artifact["bioinfection_resistance"], quality, potential)
        self.thermal_resistance = get_value(artifact["thermal_resistance"], quality, potential)
        self.health_regeneration = get_value(artifact["health_regeneration"], quality, potential)
        self.bleeding = get_value(artifact["bleeding"], quality, potential)
        self.reaction_to_burns = get_value(artifact["reaction_to_burns"], quality, potential)
        self.frost = get_value(artifact["frost"], quality, potential, True)
        self.melee_protection = get_value(artifact["melee_protection"], quality, potential)
        self.reaction_to_melee = get_value(artifact["reaction_to_melee"], quality, potential)
        self.resistance_to_fire = get_value(artifact["resistance_to_fire"], quality, potential)
        self.resistance_to_chemicals = get_value(artifact["resistance_to_chemicals"], quality, potential)
        self.resistance_to_chemical_burns = get_value(artifact["resistance_to_chemical_burns"], quality, potential)
        self.bioinfection_protection = get_value(artifact["bioinfection_protection"], quality, potential)
        self.extra_properties = artifact["extra_properties"]

    def add_property(self, property, prop_range):
        if property == "vitality":
            self.vitality += get_value(prop_range, self.quality, self.potential)
        if property == "stamina_regen":
            self.stamina_regen += get_value(prop_range, self.quality, self.potential)
        if property == "psy_emissions":
            self.psy_emissions += get_value(prop_range, self.quality, self.potential)
        if property == "psy_emissions_protection":
            self.psy_emissions_protection += get_value(prop_range, self.quality, self.potential)
        if property == "stamina":
            self.stamina += get_value(prop_range, self.quality, self.potential)
        if property == "movement_speed":
            self.movement_speed += get_value(prop_range, self.quality, self.potential)
        if property == "temperature":
            self.temperature += get_value(prop_range, self.quality, self.potential)
        if property == "reaction_to_electricity":
            self.reaction_to_electricity += get_value(prop_range, self.quality, self.potential)
        if property == "biological_infection":
            self.biological_infection += get_value(prop_range, self.quality, self.potential)
        if property == "thermal_protection":
            self.thermal_protection += get_value(prop_range, self.quality, self.potential)
        if property == "psy_emission_resistance":
            self.psy_emission_resistance += get_value(prop_range, self.quality, self.potential)
        if property == "carry_weight":
            self.carry_weight += get_value(prop_range, self.quality, self.potential)
        if property == "radiation_protection":
            self.radiation_protection += get_value(prop_range, self.quality, self.potential)
        if property == "healing_effectiveness":
            self.healing_effectiveness += get_value(prop_range, self.quality, self.potential)
        if property == "bullet_resistance":
            self.bullet_resistance += get_value(prop_range, self.quality, self.potential)
        if property == "radiation_protection":
            self.radiation_protection += get_value(prop_range, self.quality, self.potential)
        if property == "explosion_protection":
            self.explosion_protection += get_value(prop_range, self.quality, self.potential)
        if property == "radiation_resistance":
            self.radiation_resistance += get_value(prop_range, self.quality, self.potential)
        if property == "bioinfection_resistance":
            self.bioinfection_resistance += get_value(prop_range, self.quality, self.potential)
        if property == "thermal_resistance":
            self.thermal_resistance += get_value(prop_range, self.quality, self.potential)
        if property == "health_regeneration":
            self.health_regeneration += get_value(prop_range, self.quality, self.potential)
        if property == "bleeding":
            self.bleeding += get_value(prop_range, self.quality, self.potential)
        if property == "reaction_to_burns":
            self.reaction_to_burns += get_value(prop_range, self.quality, self.potential)
        if property == "frost":
            self.frost += get_value(prop_range, self.quality, self.potential)
        if property == "melee_protection":
            self.melee_protection += get_value(prop_range, self.quality, self.potential)
        if property == "reaction_to_melee":
            self.reaction_to_melee += get_value(prop_range, self.quality, self.potential)
        if property == "resistance_to_fire":
            self.resistance_to_fire += get_value(prop_range, self.quality, self.potential)
        if property == "resistance_to_chemicals":
            self.resistance_to_chemicals += get_value(prop_range, self.quality, self.potential)
        if property == "resistance_to_chemical_burns":
            self.resistance_to_chemical_burns += get_value(prop_range, self.quality, self.potential)
        if property == "bioinfection_protection":
            self.bioinfection_protection += get_value(prop_range, self.quality, self.potential)

    def set_additional_properties(self, properties):
        if len(properties) > self.potential / 5:
            return

        for property in properties:
            self.add_property(property, properties[property])
