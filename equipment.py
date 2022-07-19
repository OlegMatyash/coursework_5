import json

from dataclasses import dataclass
from random import uniform
from typing import List, Optional

import marshmallow_dataclass


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class EquipmentData:
    # TODO содержит 2 списка - с оружием и с броней
    weapons: List[Weapon]
    armors: List[Armor]


@dataclass
class Player:
    name: str
    armor_name: str
    weapon_name: str
    unit_class: str


class Equipment:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, name: str) -> Optional[Weapon]:
        # TODO возвращает объект оружия по имени
        for weapon in self.equipment.weapons:
            if weapon.name == name:
                return weapon
        return None

    def get_armor(self, name: str) -> Optional[Armor]:
        # TODO возвращает объект брони по имени
        for armor in self.equipment.armors:
            if armor.name == name:
                return armor
        return None

    def get_weapons_names(self) -> List[str]:
        # TODO возвращаем список с оружием
        return [
            weapon.name
            for weapon in self.equipment.weapons
        ]

    def get_armors_names(self) -> List[str]:
        # TODO возвращаем список с броней
        return [
            armor.name
            for armor in self.equipment.armors
        ]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        # TODO этот метод загружает json в переменную EquipmentData

        with open("./data/equipment.json", encoding='utf8') as equipment_file:
            data = json.load(equipment_file)
            equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)

            return equipment_schema().load(data)
