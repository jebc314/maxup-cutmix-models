Based on https://github.com/elis2496/maxup_implementation
which is based on https://arxiv.org/pdf/2002.09024v1.pdf

Changes made (labeled by a MODIFICATION comment):
- In model.py, changed model to resnet50 and made the necessary adaptations

Refer to commands_ran.txt for the commands ran for the experiments.

The four experiments finished after letting them run overnight on a PC with a GeForce GTX 1650 gpu.

Library used and versions are in requirements.txt. This was kept the same from the original git repo.

Data:
The imagenette dataset found here: https://github.com/fastai/imagenette.
Determined that elis2496 in their code used the 320 px download of imagenette.