# 1. 在main.py中调用skill_deployer.py。
# 2. 在skill_deployer.py中调用skill_manager.py。
# 3. 在skill_manager.py中调用double_list_helper.py。
# 4. 在list_helper.py中调用main.py。
# 要求：在所有的调用过程中，要包含函数、类、实例方法、静态方法。

# from my_project.skill_system.skill_deployer import s01
from skill_system import skill_deployer

skill_deployer.s01()