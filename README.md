# Diffusion-SMA-MD: From Generative Diffusion to MD Trajectories

This repository demonstrates a minimal, research-oriented pipeline to test whether 
an AI-based molecular dynamics surrogate can generalize to small molecules beyond 
the original training setup.  

A central open question is whether such surrogate approaches can be **more efficient**
(or even more effective) than classical molecular dynamics for generating physically
plausible conformational ensembles. This repo provides a simplified environment to explore that idea on toy systems.

It is inspired by *Generation of conformational ensembles of small molecules via surrogate model-assisted molecular dynamics* (paper reference).

Pipeline overview:
1. **Diffusion (SMA)** training on simple molecular data (alanine dipeptide, `alanine.pdb`)
2. **Boltzmann correction** to enforce physical plausibility
3. **PDB generation** from sampled structures
4. **MD trajectory** initialized from generated PDB

The following diagram summarizes the training and sampling workflow.  
This is the most important part to realize the whole pipeline: connecting an AI-based model with biological data is never trivial. One must decide:
- **Which data** to use (here: torsional angles φ, ψ extracted from MD trajectories of alanine dipeptide)
- **What to provide as input** (noisy torsions τ_t and timestep t)
- **What to expect as output** (predicted score, eventually new torsional pairs leading to novel conformations)

<p align="center">
  <img src="docs/diagram.png" width="600" alt="Diffusion->Boltzmann->PDB->MD workflow“>
</p>

### Extensions
Although this demo focuses on torsional angles, the same design principal applies more broadly: 1) 3D Cartesian coordinates as input/output for full-atom modeling; 2) Contact maps or distance matrices for coarse-grained representations; 3) Residue-level features (sequence, secondary structure) to couple with structural learning ex.Alphafold).

These choices define how well AI models can interact with physical reality, and illustrate the key challenge: translatinge biological complexity into learnable machine representations.


**Note.** This project does not aim to replace classical MD. It serves as a prototype to study the trade-offs between AI-based generative surrogates and physics-based simulations on toy datasets.

<p align="center">
  <img src="results/loss_curve.png" width="320">
  <img src="results/energy_before_after.png" width="320">
</p>

## References
- Sohl-Dickstein et al., Diffusion Probabilistic Models (2015).
- Song et al., Score-Based Generative Modeling (2021).
- *Generation of conformational ensembles of small molecules via surrogate model-assisted molecular dynamics*, [authors/year/journal—fill in].


## Quickstart

```bash
conda env create -f environment.yml
conda activate diff-sma-md
jupyter notebook demo.ipynb



