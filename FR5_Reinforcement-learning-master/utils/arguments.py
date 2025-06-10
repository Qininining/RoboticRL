import argparse
import time
import os # 导入 os 模块

now = time.strftime('%m%d-%H%M%S', time.localtime())

def get_args():
    parser = argparse.ArgumentParser(description="Running time configurations")

    # 获取当前 arguments.py 脚本文件所在的目录
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    # 从 'utils' 目录向上退一级，回到项目根目录 (假设你的项目根目录是 FR5_Reinforcement-learning-master)
    project_root = os.path.abspath(os.path.join(current_script_dir, ".."))

    # 使用 os.path.join 构建绝对路径
    # 注意：Stable Baselines3 在保存模型时会自动添加 '.zip'，
    # 因此加载时通常不需要在 model_path 中包含 '.zip'，除非你的文件名本身就包含。
    # 假设你的最佳模型保存为 'best_model.zip'
    parser.add_argument('--model_path', type=str,
                        default=os.path.join(project_root,"FR5_Reinforcement-learning", "models", "PPO", "0609-000114", "best_model.zip"), # 修正模型加载路径
                        help='Path to the trained model')

    parser.add_argument('--test_num', type=int, default=100)
    parser.add_argument('--gui', type=bool, default=True)

    # 训练/日志目录也使用绝对路径构建
    parser.add_argument('--models_dir', type=str,
                        default=os.path.join(project_root, "models", "PPO", now),
                        help='Directory to save trained models')
    parser.add_argument('--logs_dir', type=str,
                        default=os.path.join(project_root, "logs", "PPO", now),
                        help='Directory to save training logs')
    parser.add_argument('--checkpoints', type=str,
                        default=os.path.join(project_root, "checkpoints", "PPO", now),
                        help='Directory to save model checkpoints')
    parser.add_argument('--test', type=str,
                        default=os.path.join(project_root, "logs", "test", now),
                        help='Directory to save test logs')
    parser.add_argument('--timesteps', type=int, default=30000)

    args = parser.parse_args()

    kwargs = vars(args)

    return args, kwargs