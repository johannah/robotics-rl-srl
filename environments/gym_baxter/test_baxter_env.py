import time

from environments.gym_baxter.baxter_env import BaxterEnv

BaxterEnv.RECORD_DATA = True
# Reduce max distance to have more negative rewards for srl
BaxterEnv.MAX_DISTANCE = 0.65

env = BaxterEnv(renders=True, is_discrete=True, log_folder="baxter_recorder_data_log")
timesteps = 500
episodes = 50
env.seed(0)
i = 0

print('Starting episodes...')
start_time = time.time()
for _ in range(episodes):
    observation = env.reset()
    for t in range(timesteps):
        try:
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            env.render()  # render() requires first the observation to be obtained
            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                break
            i += 1
        except KeyboardInterrupt:
            pass
env.closeServerConnection()
print("Avg. frame rate: {:.2f} FPS".format(i / (time.time() - start_time)))