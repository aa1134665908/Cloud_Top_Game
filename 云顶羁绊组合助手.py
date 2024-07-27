import time
from typing import Dict, Set, Tuple, List, Generator, Optional

# 定义英雄及其属性（羁绊和价格）
heroes = {
    '战争女神 希维尔': {'synergies': ['剪纸仙灵', '迅捷射手'], 'price': 1},
    '武器大师 贾克斯': {'synergies': ['墨之影', '护卫'], 'price': 1},
    '虚空恐惧 科加斯': {'synergies': ['山海绘卷', '擎天卫'], 'price': 1},
    '皮城女警 凯特琳': {'synergies': ['幽魂', '狙神'], 'price': 1},
    '熔岩巨兽 墨菲特': {'synergies': ['天将', '擎天卫'], 'price': 1},
    '德玛西亚之力 盖伦': {'synergies': ['剪纸仙灵', '护卫'], 'price': 1},
    '深渊巨口 克格莫': {'synergies': ['山海绘卷', '神谕者', '狙神'], 'price': 1},
    '九尾妖狐 阿狸': {'synergies': ['灵魂莲华', '法师'], 'price': 1},
    '虚空掠夺者 卡兹克': {'synergies': ['天将', '死神'], 'price': 1},
    '诺克萨斯之手 德莱厄斯': {'synergies': ['夜幽', '决斗大师'], 'price': 1},
    '疾风剑豪 亚索': {'synergies': ['灵魂莲华', '决斗大师'], 'price': 1},
    '虚空遁地兽 雷克塞': {'synergies': ['永恒之森', '斗士'], 'price': 1},
    '可酷伯 可酷伯': {'synergies': ['吉星', '斗士'], 'price': 1},
    '迅捷斥候 提莫': {'synergies': ['吉星', '迅捷射手'], 'price': 2},
    '风暴之怒 迦娜': {'synergies': ['天龙之子', '神谕者'], 'price': 2},
    '牧魂人 约里克': {'synergies': ['夜幽', '擎天卫'], 'price': 2},
    '放逐之刃 锐雯': {'synergies': ['剪纸仙灵', '武仙子', '斗士'], 'price': 2},
    '暮光之眼 慎': {'synergies': ['幽魂', '擎天卫'], 'price': 2},
    '光辉女郎 拉克丝': {'synergies': ['青花瓷', '法师'], 'price': 2},
    '荆棘之兴 婕拉': {'synergies': ['剪纸仙灵', '圣贤'], 'price': 2},
    '迷失之牙 纳尔': {'synergies': ['永恒之森', '护卫'], 'price': 2},
    '永猎双子 千珏': {'synergies': ['灵魂莲华', '永恒之森', '死神'], 'price': 2},
    '涤魂圣枪 赛娜': {'synergies': ['墨之影', '狙神'], 'price': 2},
    '元素女皇 奇亚娜': {'synergies': ['天将', '决斗大师'], 'price': 2},
    '暗裔剑魔 亚托克斯': {'synergies': ['幽魂', '墨之影', '斗士'], 'price': 2},
    '万花通灵 妮蔻': {'synergies': ['山海绘卷', '天将', '法师'], 'price': 2},
    '众星之子 索拉卡': {'synergies': ['天将', '武仙子'], 'price': 3},
    '麦林炮手 崔丝塔娜': {'synergies': ['吉星', '决斗大师'], 'price': 3},
    '殇之木乃伊 阿木木': {'synergies': ['青花瓷', '护卫'], 'price': 3},
    '不灭狂雷 沃利贝尔': {'synergies': ['墨之影', '决斗大师'], 'price': 3},
    '皎月女神 黛安娜': {'synergies': ['天龙之子', '圣贤'], 'price': 3},
    '暮光星灵 佐伊': {'synergies': ['吉星', '剪纸仙灵', '法师'], 'price': 3},
    '河流之王 塔姆': {'synergies': ['山海绘卷', '斗士'], 'price': 3},
    '魂锁典狱长 锤石': {'synergies': ['灵魂莲华', '擎天卫'], 'price': 3},
    '海兽祭司 俄洛伊': {'synergies': ['幽魂', '法师', '护卫'], 'price': 3},
    '星界游神 巴德': {'synergies': ['山海绘卷', '迅捷射手'], 'price': 3},
    '残月之肃 厄斐琉斯': {'synergies': ['灵魂莲华', '狙神'], 'price': 3},
    '封魔剑魂 永恩': {'synergies': ['夜幽', '死神'], 'price': 3},
    '拉露恩 拉露恩': {'synergies': ['夜幽', '神谕者'], 'price': 3},
    '黑暗之女 安妮': {'synergies': ['吉星', '神谕者'], 'price': 4},
    '正义巨像 加里奥': {'synergies': ['剪纸仙灵', '斗士'], 'price': 4},
    '寒冰射手 艾希': {'synergies': ['青花瓷', '狙神'], 'price': 4},
    '堕落天使 莫甘娜': {'synergies': ['幽魂', '圣贤'], 'price': 4},
    '盲僧 李青': {'synergies': ['天龙之子', '决斗大师'], 'price': 4},
    '深海泰坦 诺提勒斯': {'synergies': ['山海绘卷', '护卫'], 'price': 4},
    '暗黑元首 辛德拉': {'synergies': ['灵魂莲华', '法师'], 'price': 4},
    '影流之镰 凯隐': {'synergies': ['幽魂', '死神'], 'price': 4},
    '虚空之女 卡莎': {'synergies': ['墨之影', '迅捷射手'], 'price': 4},
    '山隐之焰 奥恩': {'synergies': ['永恒之森', '擎天卫'], 'price': 4},
    '解脱者 塞拉斯': {'synergies': ['夜幽', '斗士'], 'price': 4},
    '含羞蓓蕾 莉莉娅': {'synergies': ['山海绘卷', '神谕者'], 'price': 4},
    '刀锋舞者 艾瑞莉娅': {'synergies': ['剪纸仙灵', '决斗大师'], 'price': 5},
    '齐天大圣 孙悟空': {'synergies': ['齐天大圣', '天将', '圣贤'], 'price': 5},
    '兽灵行者 乌迪尔': {'synergies': ['墨之影', '灵魂行者', '擎天卫'], 'price': 5},
    '冰霜女巫 丽桑卓': {'synergies': ['青花瓷', '法师'], 'price': 5},
    '沙漠皇帝 阿兹尔': {'synergies': ['永恒之森', '神谕者'], 'price': 5},
    '腕豪 瑟提': {'synergies': ['灵魂莲华', '夜幽', '护卫'], 'price': 5},
    '异画师 彗': {'synergies': ['山海绘卷', '画圣'], 'price': 5},
    '霞与洛 霞洛': {'synergies': ['天龙之子', '仙侣', '武仙子', '迅捷射手'], 'price': 5},
}

# 定义羁绊及其效果
synergies_info = {
    '剪纸仙灵': {3: '选择一个辅助型效果。60生命值', 5: '选择一个战斗型效果。100生命值', 7: '选择一个战斗型效果。150生命值', 10: '登神。250生命值'},
    '迅捷射手': {2: '1次弹射；45%的先前伤害', 4: '2次弹射；60%的先前伤害'},
    '墨之影': {3: '获得第1件【墨之影】装备和5%的额外伤害加成和伤害减免', 5: '获得第2件【墨之影】装备和16%的额外伤害加成和伤害减免', 7: '再获得2件【墨之影】装备和22%的额外伤害加成和伤害减免'},
    '护卫': {2: '10%伤害减免', 4: '22%伤害减免', 6: '35%伤害减免'},
    '山海绘卷': {3: '10%生命值，11%法术强度和攻击力。', 5: '16%生命值，22%法术强度和攻击力。', 7: '24%生命值，35%法术强度和攻击力。', 10: '立即变成史诗级。此加成转而提升250%。'},
    '擎天卫': {2: '25护甲和魔抗', 4: '55护甲和魔抗', 6: '85护甲和魔抗'},
    '幽魂': {2: '每个幽魂5%', 4: '每个幽魂10%', 6: '每个幽魂16%', 8: '每个幽魂36%'},
    '狙神': {2: '每格8%伤害。', 4: '每格18%伤害。', 6: '每格35%伤害。【狙神】们获得额外的2攻击距离。'},
    '天将': {2: '100%加成', 3: '110%加成', 4: '125%加成', 5: '145%加成', 6: '170%加成', 7: '200%加成'},
    '神谕者': {2: '所有己方弈子获得5法力值', 4: '【神谕者】们获得30法力值；其它弈子们获得5法力值', 6: '【神谕者】们获得45法力值；其它弈子们获得15法力值'},
    '灵魂莲华': {3: '该组合获得100%的莲华加成。', 5: '所有【灵魂莲华】弈子获得180%的莲华加成。', 7: '所有【灵魂莲华】弈子获得250%的莲华加成。',
             10: '所有【灵魂莲华】弈子获得300%的每种莲华加成。'},
    '法师': {2: '为所有友军提供20法术强度。', 4: '为【法师】们提供50法术强度；为其他单位提供20法术强度', 6: '为【法师】们提供90法术强度；为其他单位提供50法术强度',
           8: '为【法师】们提供135法术强度；为其他单位提供135法术强度'},
    '死神': {2: '【死神】的技能可以暴击，并且他们获得25%暴击几率。', 3: '此外，【死神】们会对敌人施加流血效果，在2秒里持续造成50%额外真实伤害。'},
    '夜幽': {2: '200护盾值；低于10%生命值时触发处决', 4: '450护盾值；低于18%生命值时触发处决。更多格子被照亮。', 6: '900护盾值；低于25%生命值时触发处决并照亮整个棋盘',
           9: '被处决的敌人有100%几率掉落战利品；低于60%生命值时触发处决'},
    '决斗大师': {2: '5%攻击速度', 4: '9%攻击速度', 6: '13%攻击速度；【决斗大师】们获得15%伤害减免', 8: '18%攻击速度；【决斗大师】们获得18%伤害减免'},
    '永恒之森': {2: '15法术强度； 每次敌人阵亡获得3生命值', 4: '30法术强度； 每次敌人阵亡获得7生命值', 6: '55法术强度； 每次敌人阵亡获得10生命值'},
    '斗士': {2: '20%生命值', 4: '40%生命值', 6: '60%生命值', 8: '75%生命值；每4秒，【斗士】们的下次攻击将造成6%生命值额外物理伤害。'},
    '吉星': {3: '投掷一颗骰子；经过相当于掷出点数的玩家对战回合之后，进行一次庆典。你在庆典中可以将吉运兑换为奖励。', 5: '每场玩家对战开始时，治疗2玩家生命值。',
           7: '吉星高照！每回合无论如何都会获得额外奖励和额外吉运，并且每回合举办一次庆典。'},
    '青花瓷': {2: '30%攻击速度；20%伤害减免', 4: '55%攻击速度；33%伤害减免', 6: '100%攻击速度；50%伤害减免'},
    '武仙子': {2: '10护甲和魔抗', 3: '20护甲和魔抗', 4: '40护甲和魔抗'},
    '天龙之子': {2: '5%生命值伤害，20%攻击速度。', 3: '10%生命值伤害，30%攻击速度。', 4: '10%生命值伤害和1.5秒晕眩。', 5: '15%生命值伤害，40%攻击速度。'},
    '圣贤': {2: '12%全能吸血，15法术强度', 3: '20%全能吸血，30法术强度', 4: '30%全能吸血，45法术强度', 5: '45%全能吸血，70法术强度'},
    '灵魂行者': {1: '【灵魂行者】首次降至50%生命值以下时，会释放体内的怒火，治疗至满额生命值，获得移动速度提升，并将技能从【蛮羊冲击】变更为【猛虎爪击】。'},
    '齐天大圣': {1: '每进行3次技能施放，【孙悟空】的武器就会变大，技能也会随之改变。'},
    '仙侣': {1: '根据【仙侣】部署的位置(前两排或后两排)，切换登场的英雄。在已登场的那个【仙侣】施放技能时，另一个会提供一个额外效果。前排：【武仙子】【洛】后排：【迅捷射手】【霞】'},
    '画圣': {1: '完成回合数 = 弈子的费用'},

}

# 预处理英雄数据，将价格和羁绊信息合并
heroes_data: Dict[str, Tuple[Set[str], int]] = {name: (set(info['synergies']), info['price']) for name, info in
                                                heroes.items()}

# 预处理羁绊信息，找出每个羁绊的最低生效人数
min_synergy_counts: Dict[str, int] = {synergy: min(levels.keys()) for synergy, levels in synergies_info.items()}

# 预处理每个羁绊对应的英雄列表
synergy_to_heroes: Dict[str, List[str]] = {}
for hero, (synergies, _) in heroes_data.items():
    for synergy in synergies:
        if synergy not in synergy_to_heroes:
            synergy_to_heroes[synergy] = []
        synergy_to_heroes[synergy].append(hero)


def generate_combinations_with_max_synergy(
        heroes_data: Dict[str, Tuple[Set[str], int]],
        exact_size: int,
        required_heroes: Optional[List[str]] = None,
        required_synergies: Optional[Dict[str, int]] = None
) -> Tuple[Tuple[str, ...], int, Dict[str, int], int]:
    required_heroes = required_heroes or []
    required_synergies = required_synergies or {}

    sorted_heroes = sorted(
        heroes_data.keys(),
        key=lambda h: sum(1 for s in heroes_data[h][0] if s in required_synergies),
        reverse=True
    )

    max_synergy_count = 0
    max_synergy_combo = None
    max_synergy_levels = None
    max_synergy_price = 0

    def can_satisfy_synergies(current_count: Dict[str, int], required: Dict[str, int], remaining: int) -> bool:
        return all(current_count.get(synergy, 0) + remaining >= count for synergy, count in required.items())

    def calculate_levels(synergy_count: Dict[str, int]) -> Dict[str, int]:
        levels = {}
        for synergy, count in synergy_count.items():
            if synergy in synergies_info:
                for level in sorted(synergies_info[synergy].keys(), reverse=True):
                    if count >= level:
                        levels[synergy] = level
                        break
        return levels

    def all_heroes_in_synergy(combo: List[str], levels: Dict[str, int]) -> bool:
        return all(any(synergy in levels for synergy in heroes_data[hero][0]) for hero in combo)

    def backtrack(combo: List[str], start: int, synergy_count: Dict[str, int], total_price: int):
        nonlocal max_synergy_count, max_synergy_combo, max_synergy_levels, max_synergy_price

        if len(combo) == exact_size:
            levels = calculate_levels(synergy_count)
            if levels and all_heroes_in_synergy(combo, levels):
                if all(synergy_count.get(synergy, 0) >= count for synergy, count in required_synergies.items()):
                    current_synergy_count = sum(levels.values())
                    if current_synergy_count > max_synergy_count:
                        max_synergy_count = current_synergy_count
                        max_synergy_combo = tuple(combo)
                        max_synergy_levels = levels
                        max_synergy_price = total_price
            return

        for i in range(start, len(sorted_heroes)):
            hero = sorted_heroes[i]
            new_synergy_count = synergy_count.copy()
            new_total_price = total_price + heroes_data[hero][1]

            for synergy in heroes_data[hero][0]:
                new_synergy_count[synergy] = new_synergy_count.get(synergy, 0) + 1

            if can_satisfy_synergies(new_synergy_count, required_synergies, exact_size - len(combo) - 1):
                combo.append(hero)
                backtrack(combo, i + 1, new_synergy_count, new_total_price)
                combo.pop()

    initial_combo = required_heroes.copy()
    initial_synergy_count = {}
    initial_price = 0
    for hero in initial_combo:
        for synergy in heroes_data[hero][0]:
            initial_synergy_count[synergy] = initial_synergy_count.get(synergy, 0) + 1
        initial_price += heroes_data[hero][1]

    backtrack(initial_combo, 0, initial_synergy_count, initial_price)
    return max_synergy_combo, max_synergy_price, max_synergy_levels, max_synergy_count


def select_heroes():
    selected_heroes = []

    for i in range(5):
        while True:
            try:
                price = int(input(f"请输入第 {i + 1} 个英雄的价格 (1-5): "))
                if price not in range(1, 6):
                    raise ValueError
                break
            except ValueError:
                print("请输入有效的价格 (1-5)。")

        price_heroes = [hero for hero, info in heroes.items() if info['price'] == price]

        print(f"\n价格为 {price} 的英雄：")
        for idx, hero in enumerate(price_heroes, 1):
            print(f"{idx}. {hero}")

        while True:
            try:
                choice = int(input("请选择一个英雄 (输入序号): "))
                if choice not in range(1, len(price_heroes) + 1):
                    raise ValueError
                selected_hero = price_heroes[choice - 1]
                selected_heroes.append(selected_hero)
                print(f"你选择了: {selected_hero}\n")
                break
            except ValueError:
                print("请输入有效的序号。")

    return selected_heroes


# 使用示例
exact_size = 8  # 英雄组合数量
required_synergies = {'迅捷射手': 2}  # 可选指定羁绊，如果不需要则将下方函数改为None
print("请选择 5 个尊者英雄：")
final_selection = select_heroes()
print("\n你的最终选择是:")
print(final_selection)
required_heroes = final_selection  # 指定英雄
start_time = time.time()

max_combo, max_price, max_levels, max_count = generate_combinations_with_max_synergy(
    heroes_data, exact_size, required_synergies=required_synergies, required_heroes=required_heroes
)

print("\n羁绊最多的组合:")
print(f"组合: {max_combo}, 总价格: {max_price}, 羁绊效果: {max_levels}")
print(f"羁绊数量: {len(max_levels)}")

print(f"执行时间: {int(time.time() - start_time)} 秒")
