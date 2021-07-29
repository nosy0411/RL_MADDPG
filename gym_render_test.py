import matplotlib.pyplot as plt
import gym
from IPython import display

env = gym.make('CartPole-v0')
env.reset()

plt.imshow(env.render(mode='rgb_array'))
display.display(plt.gcf())    
display.clear_output(wait=True)
env.step(env.action_space.sample()) # take a random action

env.close()