import lib


def get_value(property, quality: float, potential: int, negative=False, extra=False):
    min = property[0]
    max = property[1]
    if min < 0 and max < 0:
        temp = min
        min = max
        max = temp

    diff = abs(max - min)

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
        spcl_properties = ["Psy-emissions", "Temperature", "Radiation", "Biological infection", "Frost"]

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

    def get_attr(self, attr):
        if not hasattr(self, attr):
            return 0.0
        return getattr(self, attr)

    def add_property(self, property, prop_range):
        attr = self.get_attr(property)
        attr += get_value(prop_range, self.quality, self.potential, extra=True)
        attr = round(attr, 2)
        setattr(self, property, attr)

    def set_additional_properties(self, properties):
        for property in properties:
            self.add_property(property, self.extra_properties[property])

    def to_string(self):
        res = f"Name: {self.name} {self.quality}% +{self.potential}\n"
        if self.get_attr('Vitality') != 0:
            res += f"Vitality: {self.get_attr('Vitality')}%\n"
        if self.get_attr('Stamina regeneration') != 0:
            res += f"Stamina regeneration: {self.get_attr('Stamina regeneration')}%\n"
        if self.get_attr('Psy-emissions') != 0:
            res += f"Psy-emissions: {self.get_attr('Psy-emissions')}\n"
        if self.get_attr('Psy-emission resistance') != 0:
            res += f"Psy-Emission Protection: {self.get_attr('Psy-emission resistance')}\n"
        if self.get_attr('Stamina') != 0:
            res += f"Stamina: {self.get_attr('Stamina')}%\n"
        if self.get_attr('Movement speed') != 0:
            res += f"Movement speed: {self.get_attr('Movement speed')}%\n"
        if self.get_attr('Temperature') != 0:
            res += f"Temperature: {self.get_attr('Temperature')}\n"
        if self.get_attr('Reaction to electricity') != 0:
            res += f"Reaction to electricity: {self.get_attr('Reaction to electricity')}%\n"
        if self.get_attr('Radiation') != 0:
            res += f"Radiation: {self.get_attr('Radiation')}\n"
        if self.get_attr('Biological infection') != 0:
            res += f"Biological infection: {self.get_attr('Biological infection')}\n"
        if self.get_attr('Thermal resistance') != 0:
            res += f"Thermal protection: {self.get_attr('Thermal resistance')}\n"
        if self.get_attr('Psy-emission resistance') != 0:
            res += f"Psy-emission resistance: {self.get_attr('Psy-emission resistance')}%\n"
        if self.get_attr('Carry weight') != 0:
            res += f"Carry weight: {self.get_attr('Carry weight')}\n"
        if self.get_attr('Radiation resistance') != 0:
            res += f"Radiation protection: {self.get_attr('Radiation resistance')}\n"
        if self.get_attr('Healing effectiveness') != 0:
            res += f"Healing effectiveness: {self.get_attr('Healing effectiveness')}%\n"
        if self.get_attr('Bullet resistance') != 0:
            res += f"Bullet resistance: {self.get_attr('Bullet resistance')}\n"
        if self.get_attr('Explosion protection') != 0:
            res += f"Explosion protection: {self.get_attr('Explosion protection')}\n"
        if self.get_attr('Radiation resistance') != 0:
            res += f"Radiation resistance: {self.get_attr('Radiation resistance')}%\n"
        if self.get_attr('Bioinfection resistance') != 0:
            res += f"Bioinfection resistance: {self.get_attr('Bioinfection resistance')}%\n"
        if self.get_attr('Thermal resistance') != 0:
            res += f"Thermal resistance: {self.get_attr('Thermal resistance')}%\n"
        if self.get_attr('Health regeneration') != 0:
            res += f"Health regeneration: {self.get_attr('Health regeneration')}%\n"
        if self.get_attr('Bleeding') != 0:
            res += f"Bleeding: {self.get_attr('Bleeding')}\n"
        if self.get_attr('Bleeding protection') != 0:
            res += f"Bleeding protection: {self.get_attr('Bleeding protection')}%\n"
        if self.get_attr('Reaction to burns') != 0:
            res += f"Reaction to burns: {self.get_attr('Reaction to burns')}%\n"
        if self.get_attr('Frost') != 0:
            res += f"Frost: {self.get_attr('Frost')}\n"
        if self.get_attr('Laceration protection') != 0:
            res += f"Melee protection: {self.get_attr('Laceration protection')}\n"
        if self.get_attr('Reaction to laceration') != 0:
            res += f"Reaction to melee: {self.get_attr('Reaction to laceration')}%\n"
        if self.get_attr('Reaction to chemical burns') != 0:
            res += f"Resistance to chemical burns: {self.get_attr('Reaction to chemical burns')}%\n"
        if self.get_attr('Bioinfection protection') != 0:
            res += f"Bioinfection Protection: {self.get_attr('Bioinfection protection')}\n"

        return res


class Container:
    def __init__(self, name: str):
        containers = lib.load_mem("../resources/containers.json")
        container = containers[name]

        self.name = container["name"]
        self.protection = container["protection"]
        self.cells = container["cells"]
