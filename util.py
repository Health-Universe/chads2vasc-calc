ischemic_stroke_risk_dict = {
    0: 0.2,
    1: 0.6,
    2: 2.2,
    3: 3.2,
    4: 4.8,
    5: 7.2,
    6: 9.7,
    7: 11.2,
    8: 10.8,
    9: 12.2,
}

stroke_tia_se_risk_dict = {
    0: 0.3,
    1: 0.9,
    2: 2.9,
    3: 4.6,
    4: 6.7,
    5: 10.0,
    6: 13.6,
    7: 15.7,
    8: 15.2,
    9: 17.4,
}


def calculate_chads2vasc_score(
    age: int,
    is_male: bool,
    chf_history: bool,
    htn_history: bool,
    stroke_tia_vte_history: bool,
    cvd_history: bool,
    dm_history: bool,
):
    """Calculates the CHA₂DS₂-VASc score for atrial fibrillation stroke risk.
    Returns the CHA₂DS₂-VASc score, risk of ischemic stroke, and risk of stroke/TIA/systemic embolism.
    """

    chads2vasc_score = 0
    if age >= 65 and age < 75:
        chads2vasc_score += 1
    elif age >= 75:
        chads2vasc_score += 2

    if is_male:
        chads2vasc_score += 0
    else:
        chads2vasc_score += 1

    if chf_history:
        chads2vasc_score += 1

    if htn_history:
        chads2vasc_score += 1

    if stroke_tia_vte_history:
        chads2vasc_score += 2

    if cvd_history:
        chads2vasc_score += 1

    if dm_history:
        chads2vasc_score += 1

    return chads2vasc_score
