from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(cafe: Cafe, friends: list):
    masks_to_buy = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    else:
        if masks_to_buy == 0:
            return f"Friends can go to {cafe.name}"
        return f"Friends should buy {masks_to_buy} masks"
