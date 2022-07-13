# note
# ~increase 변수는 나중에 추가 능력치의 종류(성유물, 무기 등)에 따라 세부적으로 변수를 분류할 것


class GenshinDMGCalculator:
    def __init__(self):
        pass

    # 최종 HP 계산
    def set_HP(self, hp, plus_hp, percent_hp):
        hp = float((hp + plus_hp) * (1 + percent_hp))
        return hp

    # 최종 공격력 계산
    def set_Attack(self, attack, plus_attack, percent_attack):
        attack = float(attack + plus_attack) * (1 + percent_attack)
        return attack

    # 최종 방어력 계산
    def set_Defense(self, defense, plus_defense, percent_defense):
        defense = float(defense + plus_defense) * (1 + percent_defense)
        return defense

    # 원소 반응 계수 계산
    def Elemental_Reaction(self, type, mastery):
        if type == "vaporize" or type == "melt":
            element_reaction = float((((1301 * mastery) / (mastery + 2001)) / 100)) # 추후 인게임 실험을 통해 계산 식 도출 후 변경할 것
        else:
            element_reaction = float((((1601 * mastery) / (mastery + 2001)) / 100))
        return element_reaction

    # 방어 계수 계산
    def Defense(self, level, enemy_level, target_def_reduction):
        defense = float(((level + 100) / (((1 - target_def_reduction) * (enemy_level + 100)) + (level + 100))))
        return defense

    # 스킬 계수 세팅
    def set_skillDMG(self, skilldmg):
        return skilldmg

    # 내성 계수 계산
    def Resist(self, enemy_resist):
        if enemy_resist < 0:
            resist = 1 - (enemy_resist / 2)
        elif 0 <= enemy_resist < 0.75:
            resist = 1 - enemy_resist
        elif enemy_resist >= 0.75:
            resist = 1 / (4 * enemy_resist + 1)
        return resist

    # 기본 데미지[= (최종 공격력 x 스킬 계수) + (최종 체력 x 체비례 데미지 보너스) + (최종 방어력 x 방비례 데미지 보너스)] 계산
    def base_DMG(self, finalattack, skilldmg, finalhp, hpdmgbonus, finaldefense, defdmgbonus):
        basedmg = (finalattack * skilldmg) + (finalhp * hpdmgbonus) + (finaldefense * defdmgbonus)
        return basedmg

    # 최종 데미지[기본 데미지 x 피해 증가 x 치명타 x 원소 반응 계수 x 방어 계수 x 내성 계수] 계산
    def Final_DMG(self, basedmg, dmgincrease, criticaldmg, elementalreaction, defense, resist):
        finaldmg = basedmg * dmgincrease * criticaldmg * elementalreaction * defense * resist
        return finaldmg

def main():
    # 클래스 선언
    g = GenshinDMGCalculator()

    # 원소 반응 계수 계산 변수 입력
    reaction_type_input = input("원소 반응 타입을 선택하세요(amplify, reduce): ")
    mastery_input = int(input("원소 마스터리를 입력하세요: "))
    elemental_calculate = g.Elemental_Reaction(reaction_type_input, mastery_input)
    print("원소 반응 계수: ", elemental_calculate)

    # 방어 계수 계산 변수 입력
    level_input = float(input("캐릭터 레벨을 입력하세요: "))
    enemy_level_input = float(input("적 레벨을 입력하세요: "))
    target_def_reduction_input = float(input("방어력 감소량(방깎)을 입력하세요: "))
    defense_calculate = g.Defense(level_input, enemy_level_input, target_def_reduction_input)
    print("방어 계수: ", defense_calculate)

    # 체력 입력
    hp_input = int(input("캐릭터 체력을 입력하세요: "))
    plus_hp_input = int(input("캐릭터 체력 증가량을 입력하세요: "))
    percent_hp_input = float(input("캐릭터 체력 증가량(%)을 입력하세요: "))
    hp_calculate = g.set_HP(hp_input, plus_hp_input, percent_hp_input)
    print("최종 체력: ", hp_calculate)

    # 공격력 입력
    attack_input = int(input("기초 공격력을 입력하세요: "))
    plus_attack_input = int(input("공격력 증가량(깡공)을 입력하세요: "))
    percent_attack_input = float(input("공격력 증가량(%)을 입력하세요: "))
    attack_calculate = g.set_Attack(attack_input, plus_attack_input, percent_attack_input)
    print("최종 공격력: ", attack_calculate)

    base_defense_input = int(input("기초 방어력을 입력하세요: "))
    plus_defense_input = int(input("방어력 증가량(깡방)을 입력하세요: "))
    percent_defense_input = float(input("방어력 증가량(%)을 입력하세요: "))
    finaldefense_calculate = g.set_Defense(base_defense_input, plus_defense_input, percent_defense_input)
    print("최종 방어력: ", finaldefense_calculate)

    skill_input = float(input("스킬 계수를 입력하세요: "))
    print("스킬 계수: ", skill_input)

    critical_input = float(input("치명타 계수를 입력하세요: "))
    print("치명타 데미지: ", critical_input)

    dmgincrease_input = float(input("피해 증가를 입력하세요: "))
    print("피해 증가: ", dmgincrease_input)

    resist_input = float(input("적 내성 수치를 입력하세요: "))
    Resist_calculate = g.Resist(resist_input)
    print("내성 계수: ", Resist_calculate)

    hpdmgbonus_input = float(input("체력 데미지 보너스를 입력하세요: ")) # 없으면 1 입력
    print("체력 데미지 보너스: ", hpdmgbonus_input)

    defdmgbonus_input = float(input("방어력 데미지 보너스를 입력하세요: ")) # 없으면 1 입력
    print("방어력 데미지 보너스: ", defdmgbonus_input)





if __name__ == "__main__":
    main()