from pathlib import Path
from glob import glob
from matplotlib import pyplot as plt
import numpy as np
from tqdm import tqdm
import random
import torch
import pickle

if __name__ == '__main__':
    dest_path1 = Path(f'/common/users/dm1487/legged_manipulation/rollout_data/exploration_6_single_trajectories1')
    dest_path2 = Path(f'/common/users/dm1487/legged_manipulation/rollout_data/exploration_3_single_trajectories1')
    dest_path3 = Path(f'/common/users/dm1487/legged_manipulation/rollout_data/exploration_4_single_trajectories1')


    dest_path = Path(f'/common/users/dm1487/legged_manipulation/rollout_data/random_seed_5_single_trajectories')

    while True:
        lin_vel = []
        plt.figure(figsize=(20, 8))
        plt.xlim(-1.0, 4.0)   
        plt.ylim(-1.0, 1.0)
        print(len(glob(str(dest_path/'*/*.npz'))))
        files = glob(str(dest_path/'*/*.npz')) # [:10000]  + glob(str(dest_path1/'*/*.npz'))[:10000] + glob(str(dest_path2/'*/*.npz'))[:10000] + glob(str(dest_path3/'*/*.npz'))[:10000]
        for i in range(2):
            # print(len(files))
            # exit()
            file = random.choice(files)
            data = np.load(file)
            # actions = data['actions']
            # lin_vel.extend((np.clip(actions[:, 0], -0.65, 0.65)).tolist())
            dones = data['done']
            last_idx = (~dones).nonzero()[0]
            # print(last_idx)
            if len(last_idx) > 0:
                last_idx = last_idx[0]
            else:
                # print(len(dones))
                last_idx = len(dones)
            # print(last_idx)
            pos = data['target'][1:last_idx, :2]
            plt.plot(pos[:, 0]/0.33, pos[:, 1])
        # print(len(lin_vel))
        # plt.scatter(np.arange(0, len(lin_vel)), lin_vel)
        plt.show()