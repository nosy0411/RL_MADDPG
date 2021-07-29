# RL_MADDPG

## Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments
  
<br>
1. To run the code, please use the command "./run_training.sh". The bash script cleans up and DELETE previous runs. The script is necessary because we need an extra command to ensure image rendering is possible remotely. Training takes about two hour. If you run locally on your own computer. Be sure to increase the number of parallel agents to the number of cores your computer have in main.py. GPU does not help that much in the computation.
<br>
<br>
2. To see a visualization of the results, run the script "./run_tensorboard.sh". A link will appear, and direct your browser to that link to see rewards over time and other statistics
<br>
<br>
3. The trained models are stored in "model_dir" by default. You can also find .gif animations that show how the agents are performing! The gif file contains a grid of separate parallel agents.
<br>
<br>
4. To understand the goal of the environment: blue dots are the "good agents", and the Red dot is an "adversary". All of the agents' goals are to go near the green target. The blue agents know which one is green, but the Red agent is color-blind and does not know which target is green/black! The optimal solution is for the red agent to chase one of the blue agent, and for the blue agents to split up and go toward each of the target.
<br>
<br>

## Learning
![alt text](https://github.com/nosy0411/RL_MADDPG/blob/main/running%20process.png?raw=true)
<br>
<br>
## Result

![alt text](https://github.com/nosy0411/RL_MADDPG/blob/main/learning%20results.png?raw=true)
