#!/usr/bin/env python3
from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    for allowed in light_spellbook.light_spell_allowed_ingredients():
        if allowed in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
