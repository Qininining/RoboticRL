'''
 @Author: Prince Wang 
 @Date: 2024-02-22 
 @Last Modified by:   Prince Wang 
 @Last Modified time: 2023-10-24 23:04:04 
'''
import sys
import os # 确保导入了 os 模块

# 获取当前脚本 (Fr5_test.py) 所在的目录的绝对路径
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# 假设项目的根目录是 'FR5_Reinforcement-learning-master'
# 从 'FR_Gym/test' 向上退两级，即回到项目根目录
project_root = os.path.abspath(os.path.join(current_script_dir, "..", ".."))

# 将项目根目录添加到 sys.path
sys.path.append(project_root)

sys.path.append(os.path.join(project_root, "FR_Gym")) # 添加 FR_Gym 目录
sys.path.append(os.path.join(project_root, "utils")) # 添加 utils 目录

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

from stable_baselines3 import A2C,PPO,DDPG,TD3
from Fr5_env import FR5_Env
import time
from utils.arguments import get_args

if __name__ == '__main__':
    args, kwargs = get_args()
    env = FR5_Env(gui=args.gui)
    env.render()
    model = PPO.load(args.model_path)
    test_num = args.test_num  # 测试次数
    success_num = 0  # 成功次数
    print("测试次数：",test_num)
    for i in range(test_num):
        state,_ = env.reset()
        done = False 
        score = 0
        # time.sleep(3)
        
        while not done:
            # action = env.action_space.sample()     # 随机采样动作
            action, _ = model.predict(observation=state,deterministic=True)
            # print("state:",state)
            # print("action:",action)
            state, reward, done, _,info = env.step(action=action)
            score += reward
            # env.render()
            time.sleep(0.01)

        if info['is_success']:
            success_num += 1
        print("奖励：",score)
    success_rate = success_num/test_num
    print("成功率：",success_rate)
    env.close()

