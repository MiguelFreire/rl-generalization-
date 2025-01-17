from experiments.experiment import Experiment

class BaseExperimentNature(Experiment):
    def __init__(self, name="CoinRunNatureLevels-default", num_levels=500, batchNorm=False, dropout=0.0, l2_penalty=0, entropy_bonus = 0.01, augment_obs=None, attention=None, num_steps=25_000_000, hidden_sizes=[512], max_pooling=False, arch="original", env="coinrun", gpu=0):
      self.num_levels = num_levels
      self.batchNorm = batchNorm
      self.dropout = dropout
      self.name = name
      self.l2_penalty = l2_penalty
      self.entropy_bonus = entropy_bonus
      self.augment_obs = augment_obs
      self.attention = attention
      self.num_steps = num_steps
      self.max_pooling = max_pooling
      self.hidden_sizes = hidden_sizes
      self.arch = arch
      self.env = env
      self.gpu = gpu
    def getConfig(self):
        return {
            "name": self.name,
            "discount": 0.999,
            "lambda": 0.95,
            "timesteps_per_rollout": 256,
            "epochs_per_rollout": 3,
            "minibatches_per_epoch": 8,
            "entropy_bonus": self.entropy_bonus,
            "ppo_clip": 0.2,
            "learning_rate": 5e-4,
            "workers": 8,
            "envs_per_worker": 64,
            "total_timesteps": self.num_steps,
            "l2_penalty": self.l2_penalty,
            "dropout": self.dropout,
            "batchNorm": self.batchNorm,
            "num_levels": self.num_levels,
            "model": "nature",
            "augment_obs": self.augment_obs,
            "attention": self.attention,
            "maxpool": self.max_pooling,
            "hidden_sizes": self.hidden_sizes,
            "arch": self.arch,
            "env": self.env,
            "gpu": self.gpu,
        }

