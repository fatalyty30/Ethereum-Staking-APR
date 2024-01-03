import math
def compute_staking_apr(X):
  # Constants
  InclusionDelay = 0.7
  StakingRatio = X
  EthSupply = 120000000000000000
  BlocksPerYear = 2584918
  EpochsPerYear = BlocksPerYear // 32

  # Compute ProposerRewardAPR
  ActiveBalance = EthSupply * StakingRatio
  BaseReward = 64 * 32000000000 / (4 * math.sqrt(ActiveBalance))
  NumberOfAttestors = ActiveBalance / (32000000000 * 32)
  ProposerReward = (BaseReward * NumberOfAttestors) / 8
  ProposerRewardAPR = ProposerReward * BlocksPerYear * 32 / ActiveBalance
  
  # Compute AttesterRewardAPR
  AttesterReward = 3*BaseReward+(7*BaseReward*InclusionDelay)/8
  AttesterRewardAPR = AttesterReward * EpochsPerYear * 100 / 32000000000
  
  # Compute StakingAPR
  TransactionFeesAPR = 1
  MevAPR = 1
  StakingAPR = ProposerRewardAPR + AttesterRewardAPR + TransactionFeesAPR + MevAPR
  return StakingAPR

staking_apr = compute_staking_apr(0.5)
print('The Staking APR is approximatively', round(staking_apr,2),'%')
