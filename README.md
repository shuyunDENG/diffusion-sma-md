# Diffusion-SMA-MD: From Generative Diffusion to MD Trajectories

This repository demonstrates a minimal, research-oriented pipeline to test whether an AI-based molecular dynamics surrogate can generalize to small molecules beyond the original training setup.
A central open question is whether such surrogate approaches can be **more efficient**(or even more effective) than classical molecular dynamics for generating physically plausible conformational ensembles.
This repo provides a simplified environment to explore that idea on toy systems.
It is inspired by *Generation of conformational ensembles of small molecules via surrogate model-assisted molecular dynamics* (papaer reference).

Pipeline overview: 
1. **Diffusion (SMA)** training on simple molecular data (alanine dipeptide, 'alanine.pdb)
2. **Boltzmann correction** to enforce physical plausibility
3. **PDB generation** from sampled structures
4. **MD trajectory** initialized from generated PDB.

<p align="center">
  <img src="results/loss_curve.png" width="320">
  <img src="results/energy_before_after.png" width="320">
</p>

## Quickstart

```bash
conda env create -f environment.yml
conda activate diff-sma-md
jupyter notebook demo.ipynb
