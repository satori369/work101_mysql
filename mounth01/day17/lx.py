class SkillManager:
    """
        技能管理器     可迭代对象
    """
    def __init__(self):
        self.__skills = []

    def add_skill(self,str_skill):
        self.__skills.append(str_skill)

    def __iter__(self):
        return self.__skills

s=SkillManager()
s.add_skill(456)
print(type(s))
# for i in s:
#     print(i)
