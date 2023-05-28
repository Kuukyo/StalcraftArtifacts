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

        properties = artifacts[name].keys()
        spcl_properties = ["psy_emissions", "temperature", "radiation", "biological_infection", "frost"]

        self.name = name
        self.quality = quality
        self.potential = potential
        self.extra_properties = artifact["extra_properties"]

        for prop in properties:
            if prop == "extra_properties":
                continue

            value = artifact[prop]
            is_spcl = False

            if prop in spcl_properties:
                is_spcl = True

            value_ = get_value(value, quality, potential, is_spcl)
            setattr(self, prop, value_)

    def add_property(self, property, prop_range):
        attr = getattr(self, property)
        attr += get_value(prop_range, self.quality, self.potential, extra=True)
        attr = round(attr, 2)
        setattr(self, property, attr)

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
        if self.psy_emissions_protection != 0:
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

        self.name = container["name"]
        self.protection = container["protection"]
        self.cells = container["cells"]
