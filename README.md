# fracturedPorousMedia
hybrid-mixed FEM for flow in fractured porous media

+ 4 2D benchmark tests:  [hydrocoin.ipynb](hydrocoin.ipynb), 
[geiger.ipynb](geiger.ipynb), [complex.ipynb](complex.ipynb), 
[real.ipynb](real.ipynb).
+ 4 3D benchmark tests: 
[single3D.ipynb](single3D.ipynb), 
  [regular3D.ipynb](regular3D.ipynb), 
  [small_features3D.ipynb](small_features3D.ipynb), 
[field3D.ipynb](field3D.ipynb).

HDG for fractured porous media flow in unfitted meshes
+ [complex network in 2D](complex2D-HDG.ipynb)
+ [single fracture in 3D](single3Dhex-HDG.ipynb)

## Running the tutorials
There are at least two ways you can run the tutorials:
1. Run the tutorials from your host machine which has a recent `ngsxfem` installed with 
``` {.shell}
jupyter notebook *.ipynb
```

2. or run `ngsxfem` interactively in the cloud without any local installation through 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gridfunction/fracturedPorousMedia/HEAD?filepath=complex2D-HDG.ipynb
)

