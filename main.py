# note
# ~increase 변수는 나중에 추가 능력치의 종류에 따라 세부적으로 변수를 분류할 것


class GenshinDMGCalculator:
    def __init__(self):
        pass

    # 최종 HP 계산
    def setHP(self, hp, hp_increase):
        hp = float(hp + hp_increase)
        return hp

    # 최종 공격력 계산
    def setAttack(self, attack, attack_increase):
        attack = float(attack + attack_increase)
        return attack

    # 최종 방어력 계산
    def setDefense(self, defense, def_increase):
        defense = float(defense + def_increase)
        return defense

    # 원소 반응 계수 계산
    def ElementalReaction(self, mastery):
        element_reaction = float((((1601 * mastery) / (mastery + 2001)) / 100)) # 추후 인게임 실험을 통해 계산 식 도출 후 변경할 것
        return element_reaction

    # 방어 계수 계산
    def Defense(self, level, enemylevel, defreduction):
        self.defense = float(((level + 100) /(((1 - defreduction) * (enemylevel + 100)) + (level + 100))))
        return self.defense

    # 스킬 계수 세팅
    def setskillDMG(self, skilldmg):
        return skilldmg

    # 내성 계수 계산
    def Resist(self, resist, enemy_resist):
        if enemy_resist < 0:
            resist = 1 - (enemy_resist / 2)
        elif 0 <= enemy_resist < 0.75:
            resist = 1 - enemy_resist
        elif enemy_resist >= 0.75:
            resist = 1 / (4 * enemy_resist + 1)
        return resist

    # 기본 데미지[= (최종 공격력 x 스킬 계수) + (최종 체력 x 체비례 데미지 보너스) + (최종 방어력 x 방비례 데미지 보너스)] 계산
    def baseDMG(self, finalattack, skilldmg, finalhp, hpdmgbonus, finaldefense, defdmgbonus):
        basedmg = (finalattack * skilldmg) + (finalhp * hpdmgbonus) + (finaldefense * defdmgbonus)
        return basedmg

    # 최종 데미지[기본 데미지 x 피해 증가 x 치명타 x 원소 반응 계수 x 방어 계수 x 내성 계수] 계산
    def FinalDMG(self, basedmg, dmgincrease, criticaldmg, elementalreaction, defense, resist):
        finaldmg = basedmg * dmgincrease * criticaldmg * elementalreaction * defense * resist
        return finaldmg

def main():
    g = GenshinDMGCalculator()
    mastery_input = int(input("원소 마스터리를 입력하세요: "))
    elemental_calculate = g.ElementalReaction(mastery_input)
    print("원소 반응 계수: ", elemental_calculate)

    hp_input = int(input("캐릭터 체력을 입력하세요: "))
    hp_calculate = g.setHP(hp_input)
    print("최종 체력: ", hp_calculate)

    attack_input = int(input("최종 공격력을 입력하세요: "))
    attack_calculate = g.setAttack(attack_input)
    print("최종 공격력: ", attack_calculate)

    finaldefense_input = int(input("최종 방어력을 입력하세요: "))
    finaldefense_calculate = g.setDefense(finaldefense_input)
    print("최종 방어력: ", finaldefense_calculate)

    skill_input = float(input("스킬 계수를 입력하세요: "))
    print("스킬 계수: ", skill_input)

    critical_input = float(input("치명타 계수를 입력하세요: "))
    print("치명타 데미지: ", critical_input)

    dmgincrease_input = float(input("피해 증가를 입력하세요: "))
    print("피해 증가: ", dmgincrease_input)

    defense_input = float(input("방어 계수를 입력하세요: "))
    Defense_calculate = g.Defense(defense_input)
    print("방어 계수: ", Defense_calculate)
    resist_input = float(input("내성 계수를 입력하세요: "))
    Resist_calculate = g.Resist(resist_input)
    print("내성 계수: ", Resist_calculate)

    hpdmgbonus_input = float(input("체력 데미지 보너스를 입력하세요: "))
    print("체력 데미지 보너스: ", hpdmgbonus_input)

    defdmgbonus_input = float(input("방어력 데미지 보너스를 입력하세요: "))
    print("방어력 데미지 보너스: ", defdmgbonus_input)

    level_input = int(input("캐릭터 레벨을 입력하세요: "))
    print("캐릭터 레벨: ", level_input)

    enemylevel_input = int(input("적 레벨을 입력하세요: "))
    print("적 레벨: ", enemylevel_input)


if __name__ == "__main__":
    main()