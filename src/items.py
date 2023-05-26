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
            return round(max, 2)
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

        self.name = name
        self.quality = quality
        self.potential = potential
        self.vitality = get_value(artifact["vitality"], quality, potential)
        self.stamina_regen = get_value(artifact["stamina_regen"], quality, potential)
        self.psy_emissions = get_value(artifact["psy_emissions"], quality, potential, True)
        self.psy_emission_protection = get_value(artifact["psy_emissions_protection"], quality, potential)
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
        self.bleeding_protection = get_value(artifact["bleeding_protection"], quality, potential)
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
            self.vitality += get_value(prop_range, self.quality, self.potential, extra=True)
            self.vitality = round(self.vitality, 2)
        if property == "stamina_regen":
            self.stamina_regen += get_value(prop_range, self.quality, self.potential, extra=True)
            self.stamina_regen = round(self.stamina_regen, 2)
        if property == "psy_emissions":
            self.psy_emissions += get_value(prop_range, self.quality, self.potential, extra=True)
            self.psy_emissions = round(self.psy_emissions, 2)
        if property == "psy_emissions_protection":
            self.psy_emission_protection += get_value(prop_range, self.quality, self.potential, extra=True)
            self.psy_emission_protection = round(self.psy_emission_protection, 2)
        if property == "stamina":
            self.stamina += get_value(prop_range, self.quality, self.potential, extra=True)
            self.stamina = round(self.stamina, 2)
        if property == "movement_speed":
            self.movement_speed += get_value(prop_range, self.quality, self.potential, extra=True)
            self.movement_speed = round(self.movement_speed, 2)
        if property == "temperature":
            self.temperature += get_value(prop_range, self.quality, self.potential, extra=True)
            self.temperature = round(self.temperature, 2)
        if property == "reaction_to_electricity":
            self.reaction_to_electricity += get_value(prop_range, self.quality, self.potential, extra=True)
            self.reaction_to_electricity = round(self.reaction_to_electricity, 2)
        if property == "biological_infection":
            self.biological_infection += get_value(prop_range, self.quality, self.potential, extra=True)
            self.biological_infection = round(self.biological_infection, 2)
        if property == "thermal_protection":
            self.thermal_protection += get_value(prop_range, self.quality, self.potential, extra=True)
            self.thermal_protection = round(self.thermal_protection, 2)
        if property == "psy_emission_resistance":
            self.psy_emission_resistance += get_value(prop_range, self.quality, self.potential, extra=True)
            self.psy_emission_resistance = round(self.psy_emission_resistance, 2)
        if property == "carry_weight":
            self.carry_weight += get_value(prop_range, self.quality, self.potential, extra=True)
            self.carry_weight = round(self.carry_weight, 2)
        if property == "radiation_protection":
            self.radiation_protection += get_value(prop_range, self.quality, self.potential, extra=True)
            self.radiation_protection = round(self.radiation_protection, 2)
        if property == "healing_effectiveness":
            self.healing_effectiveness += get_value(prop_range, self.quality, self.potential, extra=True)
            self.healing_effectiveness = round(self.healing_effectiveness, 2)
        if property == "bullet_resistance":
            self.bullet_resistance += get_value(prop_range, self.quality, self.potential, extra=True)
            self.bullet_resistance = round(self.bullet_resistance, 2)
        if property == "radiation_protection":
            self.radiation_protection += get_value(prop_range, self.quality, self.potential, extra=True)
            self.radiation_protection = round(self.radiation_protection, 2)
        if property == "explosion_protection":
            self.explosion_protection += get_value(prop_range, self.quality, self.potential, extra=True)
            self.explosion_protection = round(self.explosion_protection, 2)
        if property == "radiation_resistance":
            self.radiation_resistance += get_value(prop_range, self.quality, self.potential, extra=True)
            self.radiation_resistance = round(self.radiation_resistance, 2)
        if property == "bioinfection_resistance":
            self.bioinfection_resistance += get_value(prop_range, self.quality, self.potential, extra=True)
            self.bioinfection_resistance = round(self.bioinfection_resistance, 2)
        if property == "thermal_resistance":
            self.thermal_resistance += get_value(prop_range, self.quality, self.potential, extra=True)
            self.thermal_resistance = round(self.thermal_resistance, 2)
        if property == "health_regeneration":
            self.health_regeneration += get_value(prop_range, self.quality, self.potential, extra=True)
            self.health_regeneration = round(self.health_regeneration, 2)
        if property == "bleeding":
            self.bleeding += get_value(prop_range, self.quality, self.potential, extra=True)
            self.bleeding = round(self.bleeding, 2)
        if property == "bleeding_protection":
            self.bleeding_protection += get_value(prop_range, self.quality, self.potential, extra=True)
            self.bleeding_protection = round(self.bleeding, 2)
        if property == "reaction_to_burns":
            self.reaction_to_burns += get_value(prop_range, self.quality, self.potential, extra=True)
            self.reaction_to_burns = round(self.reaction_to_burns, 2)
        if property == "frost":
            self.frost += get_value(prop_range, self.quality, self.potential, extra=True)
            self.frost = round(self.frost, 2)
        if property == "melee_protection":
            self.melee_protection += get_value(prop_range, self.quality, self.potential, extra=True)
            self.melee_protection = round(self.melee_protection, 2)
        if property == "reaction_to_melee":
            self.reaction_to_melee += get_value(prop_range, self.quality, self.potential, extra=True)
            self.reaction_to_melee = round(self.reaction_to_melee, 2)
        if property == "resistance_to_fire":
            self.resistance_to_fire += get_value(prop_range, self.quality, self.potential, extra=True)
            self.resistance_to_fire = round(self.resistance_to_fire, 2)
        if property == "resistance_to_chemicals":
            self.resistance_to_chemicals += get_value(prop_range, self.quality, self.potential, extra=True)
            self.resistance_to_chemicals = round(self.resistance_to_chemicals, 2)
        if property == "resistance_to_chemical_burns":
            self.resistance_to_chemical_burns += get_value(prop_range, self.quality, self.potential, extra=True)
            self.resistance_to_chemical_burns = round(self.resistance_to_chemical_burns, 2)
        if property == "bioinfection_protection":
            self.bioinfection_protection += get_value(prop_range, self.quality, self.potential, extra=True)
            self.bioinfection_protection = round(self.bioinfection_protection, 2)

    def set_additional_properties(self, properties):
        for property in properties:
            self.add_property(property, self.extra_properties[property])

    def to_string(self):
        res = f"Name: {self.name} {self.quality}% +{self.potential}\n"
        if self.vitality != 0:
            res += f"Vitality: {self.vitality}%\n"
        if self.stamina_regen != 0:
            res += f"Stamina Regen: {self.stamina_regen}%\n"
        if self.psy_emissions != 0:
            res += f"Psy-emissions: {self.psy_emissions}\n"
        if self.psy_emission_protection != 0:
            res += f"Psy-Emission Protection: {self.psy_emission_protection}\n"
        if self.stamina != 0:
            res += f"Stamina: {self.stamina}%\n"
        if self.movement_speed != 0:
            res += f"Movement speed: {self.movement_speed}%\n"
        if self.temperature != 0:
            res += f"Temperature: {self.temperature}\n"
        if self.reaction_to_electricity != 0:
            res += f"Reaction to electricity: {self.reaction_to_electricity}%\n"
        if self.radiation != 0:
            res += f"Radiation: {self.radiation}\n"
        if self.biological_infection != 0:
            res += f"Biological infection: {self.biological_infection}\n"
        if self.thermal_protection != 0:
            res += f"Thermal protection: {self.thermal_protection}\n"
        if self.psy_emission_resistance != 0:
            res += f"Psy-emission resistance: {self.psy_emission_resistance}%\n"
        if self.carry_weight != 0:
            res += f"Carry weight: {self.carry_weight}\n"
        if self.radiation_protection != 0:
            res += f"Radiation protection: {self.radiation_protection}\n"
        if self.healing_effectiveness != 0:
            res += f"Healing effectiveness: {self.healing_effectiveness}%\n"
        if self.bullet_resistance != 0:
            res += f"Bullet resistance: {self.bullet_resistance}\n"
        if self.explosion_protection != 0:
            res += f"Explosion protection: {self.explosion_protection}\n"
        if self.radiation_resistance != 0:
            res += f"Radiation resistance: {self.radiation_resistance}%\n"
        if self.bioinfection_resistance != 0:
            res += f"Bioinfection resistance: {self.bioinfection_resistance}%\n"
        if self.thermal_resistance != 0:
            res += f"Thermal resistance: {self.thermal_resistance}%\n"
        if self.health_regeneration != 0:
            res += f"Health regeneration: {self.health_regeneration}%\n"
        if self.bleeding != 0:
            res += f"Bleeding: {self.bleeding}\n"
        if self.bleeding_protection != 0:
            res += f"Bleeding protection: {self.bleeding_protection}%\n"
        if self.reaction_to_burns != 0:
            res += f"Reaction to burns: {self.reaction_to_burns}%\n"
        if self.frost != 0:
            res += f"Frost: {self.frost}\n"
        if self.melee_protection != 0:
            res += f"Melee protection: {self.melee_protection}\n"
        if self.reaction_to_melee != 0:
            res += f"Reaction to melee: {self.reaction_to_melee}%\n"
        if self.resistance_to_fire != 0:
            res += f"Resistance to fire: {self.resistance_to_fire}\n"
        if self.resistance_to_chemicals != 0:
            res += f"Resistance to chemicals: {self.resistance_to_chemicals}\n"
        if self.resistance_to_chemical_burns != 0:
            res += f"Resistance to chemical burns: {self.resistance_to_chemical_burns}%\n"
        if self.bioinfection_protection != 0:
            res += f"Bioinfection Protection: {self.bioinfection_protection}\n"

        return res


class Container:
    def __init__(self, name: str):
        containers = lib.load_mem("../resources/containers.json")
        container = containers[name]

        self.protection = container["protection"]
        self.cells = container["cells"]
